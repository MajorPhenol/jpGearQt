from helper import invF
from PopupWindow import PopupWindow

from numpy import pi, sin, cos, tan, arcsin, arccos, arctan, sqrt
from numpy import linspace, rad2deg, deg2rad
# why isn't this in numpy???
tau = 2*pi

import matplotlib.pyplot as pyplot
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import matplotlib.collections as mcollections
import matplotlib.transforms as mtransforms
import matplotlib.animation as manimation
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

from PySide6.QtWidgets import QFileDialog

import copy

import ezdxf
from ezdxf.math import UCS
from ezdxf import zoom

def layoutGear(_jpgear, _gear, save=False):
    G = _gear

    if G.N < 1:
        return

    curveList = []
    curveColor = 'b'
    curveWidth = 2

    # Involute
    # find staring point of involute
    Rjfi = G.Rb/(cos(G.phi_JFI))
    theta_JFI = G.tts/(2*G.Rs) + invF(_jpgear.PA) - invF(G.phi_JFI)
    Rjfi_x = Rjfi*sin(theta_JFI)
    Rjfi_y = Rjfi*cos(theta_JFI)
    # create vectors of points along the involute
    RA = linspace(Rjfi, G.Roe, 20)
    phi_A = arccos(G.Rb/RA)
    theta_A = (G.tts/(2*G.Rs)) + invF(_jpgear.PA) - invF(phi_A)
    RAx = RA*sin(theta_A)
    RAy = RA*cos(theta_A)
    # add right side
    invPath = mpath.Path( list(map(list, zip(*[RAx, RAy]))) )
    invPatch = mpatch.PathPatch(invPath, color=curveColor, linewidth=curveWidth, fill=False)
    curveList.append(invPatch)
    # add left side
    invPath = mpath.Path( list(map(list, zip(*[-RAx, RAy]))) )
    invPatch = mpatch.PathPatch(invPath, color=curveColor, linewidth=curveWidth, fill=False)
    curveList.append(invPatch)

    # Root fillet radius
    if G.Rf > 0:
        # find center of fillet circle
        Fx = (G.Rr + G.Rf)*sin(G.theta_F)
        Fy = (G.Rr + G.Rf)*cos(G.theta_F)
        # find arc angles
        filletStartAngle = 180 + rad2deg(G.phi_JFI - theta_JFI);
        filletEndAngle = 360 - 90 - rad2deg(G.theta_F);
        curveList.append(mpatch.Arc(
                                    (Fx,Fy),
                                    G.Rf*2, G.Rf*2,
                                    theta1=filletStartAngle, theta2=filletEndAngle,
                                    color=curveColor,
                                    linewidth=curveWidth
                                    )
                        )
        curveList.append(mpatch.Arc(
                                    (-Fx,Fy),
                                    G.Rf*2, G.Rf*2,
                                    theta1=180-filletEndAngle, theta2=180-filletStartAngle,
                                    color=curveColor,
                                    linewidth=curveWidth
                                    )
                        )

    # add straight line segment if undercut
    if G.undercut == True:
        theta_A = G.tts/(2*G.Rs) + invF(_jpgear.PA)
        Rjfi = (G.Rr + G.Rf) * cos(G.theta_F - theta_A)
        Rjfi_x = Rjfi*sin(theta_A)
        Rjfi_y = Rjfi*cos(theta_A)

        Rb_x = G.Rb*sin(theta_A)
        Rb_y = G.Rb*cos(theta_A)

        line = mpath.Path([[Rjfi_x, Rjfi_y], [Rb_x, Rb_y]])
        linePatch = mpatch.PathPatch(line, color=curveColor, linewidth=curveWidth, fill=False)
        curveList.append(linePatch)
        line = mpath.Path([[-Rjfi_x, Rjfi_y], [-Rb_x, Rb_y]])
        linePatch = mpatch.PathPatch(line, color=curveColor, linewidth=curveWidth, fill=False)
        curveList.append(linePatch)

    # Root Radius
    if G.Rf < G.Rff:
        RRStartAngle1 = rad2deg(G.theta_F) + 90
        RREndAngle1 = rad2deg(pi/G.N) + 90
        RRStartAngle2 = -rad2deg(pi/G.N) + 90
        RREndAngle2 = -rad2deg(G.theta_F) + 90
        curveList.append(mpatch.Arc(
                                    (0, 0),
                                    G.Rr*2, G.Rr*2,
                                    theta1=RRStartAngle1, theta2=RREndAngle1,
                                    color=curveColor,
                                    linewidth=curveWidth
                                    )
                        )
        curveList.append(mpatch.Arc(
                                    (0, 0),
                                    G.Rr*2, G.Rr*2,
                                    theta1=RRStartAngle2, theta2=RREndAngle2,
                                    color=curveColor,
                                    linewidth=curveWidth
                                    )
                        )

    # Tip Radius
    if G.Rtip > 0:
        # point where tip touches involute
        phi_Atip = arccos(G.Rb/G.Roe);
        theta_Atip = (G.tts/(2*G.Rs)) + invF(_jpgear.PA) - invF(phi_Atip);
        # point where tip touches OD
        CF = G.Ro - G.Rtip; # distance from gear center to fillet center
        phi_Otip = arccos(G.Rb/CF);
        theta_Otip = theta_Atip - phi_Atip + phi_Otip;
        # Center point
        Rtip_x = CF*sin(theta_Otip);
        Rtip_y = CF*cos(theta_Otip);
        # find arc angles
        tipStartAngle = rad2deg(phi_Atip - theta_Atip);
        tipEndAngle = 90 - rad2deg(theta_Otip);
        curveList.append(mpatch.Arc(
                                    (Rtip_x,Rtip_y),
                                    G.Rtip*2, G.Rtip*2,
                                    theta1=tipStartAngle, theta2=tipEndAngle,
                                    color=curveColor,
                                    linewidth=curveWidth
                                    )
                        )
        curveList.append(mpatch.Arc(
                                    (-Rtip_x,Rtip_y),
                                    G.Rtip*2, G.Rtip*2,
                                    theta1=180-tipEndAngle, theta2=180-tipStartAngle,
                                    color=curveColor,
                                    linewidth=curveWidth
                                    )
                        )

    # Outer Radius
    if G.Rtip < G.Rtip_max:
        if 'theta_Otip' in locals():
                theta_O = theta_Otip
        else:
                phi_O = arccos(G.Rb/G.Roe)
                theta_O = (G.tts/(2*G.Rs)) + invF(_jpgear.PA) - invF(phi_O)
        ODStartAngle = -rad2deg(theta_O) + 90
        ODEndAngle = rad2deg(theta_O) + 90
        curveList.append(mpatch.Arc(
                                    (0,0),
                                    G.Ro*2, G.Ro*2,
                                    #angle=90,
                                    theta1=ODStartAngle, theta2=ODEndAngle,
                                    color=curveColor,
                                    linewidth=curveWidth
                                    )
                        )

    if save == True:
        if G.ID == 1:
            defaultName = 'gear1.dxf'
        else:
            defaultName = 'gear2.dxf'

        savePath, selectedFilter = QFileDialog.getSaveFileName(_jpgear, 'Save Gear'+str(G.ID), defaultName)

        if savePath == '':
            return

        doc = ezdxf.new()
        if _jpgear.units.lenName == "mm":
            doc.units = ezdxf.units.MM
        elif _jpgear.units.lenName == "in":
            doc.units = ezdxf.units.IN

        scale = 1 / _jpgear.units.lenMult

        msp = doc.modelspace()

        for n in range(G.N):
            angle = (n/G.N)*tau
            ucs = UCS(origin=(0,0,0)).rotate_local_z(angle)

            # involute
            msp.add_lwpolyline(list(zip(RAx, RAy))).transform(ucs.matrix).scale(scale, scale, scale)
            msp.add_lwpolyline(list(zip(-RAx, RAy))).transform(ucs.matrix).scale(scale, scale, scale)

            # root fillet
            if G.Rf > 0:
                msp.add_arc((Fx, Fy), radius=G.Rf, start_angle=filletStartAngle, end_angle=filletEndAngle).transform(ucs.matrix).scale(scale, scale, scale)
                msp.add_arc((-Fx, Fy), radius=G.Rf, start_angle=180-filletEndAngle, end_angle=180-filletStartAngle).transform(ucs.matrix).scale(scale, scale, scale)

            # add straight line segment if undercut
            if G.undercut == True:
                msp.add_line((Rjfi_x, Rjfi_y), (Rb_x, Rb_y)).transform(ucs.matrix).scale(scale, scale, scale)
                msp.add_line((-Rjfi_x, Rjfi_y), (-Rb_x, Rb_y)).transform(ucs.matrix).scale(scale, scale, scale)

            # root radius
            if G.Rf < G.Rff :
                msp.add_arc((0, 0), radius=G.Rr, start_angle=RRStartAngle1, end_angle=RREndAngle1).transform(ucs.matrix).scale(scale, scale, scale)
                msp.add_arc((0, 0), radius=G.Rr, start_angle=RRStartAngle2, end_angle=RREndAngle2).transform(ucs.matrix).scale(scale, scale, scale)

            # tip radius
            if G.Rtip > 0:
                msp.add_arc((Rtip_x,Rtip_y), radius=G.Rtip, start_angle=tipStartAngle, end_angle=tipEndAngle).transform(ucs.matrix).scale(scale, scale, scale)
                msp.add_arc((-Rtip_x,Rtip_y), radius=G.Rtip, start_angle=180-tipEndAngle, end_angle=180-tipStartAngle).transform(ucs.matrix).scale(scale, scale, scale)

            # outer radius
            if G.Rtip < G.Rtip_max:
                msp.add_arc((0, 0), radius=G.Ro, start_angle=ODStartAngle, end_angle=ODEndAngle).transform(ucs.matrix).scale(scale, scale, scale)

        # rim radius
        if _gear.type == "internal":
            msp.add_circle((0, 0), radius=G.Rrim).transform(ucs.matrix).scale(scale, scale, scale)

        zoom.extents(msp)
        doc.saveas(str(savePath))

    # save == False
    else:
        # make copies of all the teeth
        fullList = []
        for n in range(G.N):
            angle = (n/G.N)*tau
            for curve in curveList:
                newCurve = copy.copy(curve)
                newCurve.set_transform(mtransforms.Affine2D().rotate(angle))
                fullList.append(newCurve)
        # rim radius
        if _gear.type == "internal":
            fullList.append(pyplot.Circle((0, 0), _gear.Rrim, color=curveColor, linewidth=curveWidth, fill=False))

        curveCollection = mcollections.PatchCollection(fullList, match_original=True)
        return curveCollection

def addCircles(_jpgear, _gear, _canvas, _legend=True):
    if _gear.Rb < 0:
        return None

    circleList = []
    # base circle
    circleList.append(pyplot.Circle((0, 0), _gear.Rb / _jpgear.units.lenMult, color='c', ls='--', fill=False, label='Base Circle'))
    # # pitch circle
    circleList.append(pyplot.Circle((0, 0), _gear.Rp / _jpgear.units.lenMult, color='y', ls='--', fill=False, label='Pitch Circle'))
    # # outer circle
    circleList.append(pyplot.Circle((0, 0), _gear.Roe / _jpgear.units.lenMult, color='g', ls='--', fill=False, label='Outer Circle'))
    # # root cirlce
    circleList.append(pyplot.Circle((0, 0), _gear.Rr / _jpgear.units.lenMult, color='r', ls='--', fill=False, label='Root Circle'))

    # adding a legend only works if the circles are added individually, instead of as a collection
    if _legend == True:
        for circle in circleList:
            _canvas.axes.add_patch(circle)

        legendCircle = _canvas.axes.legend(loc='upper right', framealpha=1.0)
        _canvas.axes.add_artist(legendCircle)

    else:
        circleCollection = mcollections.PatchCollection(circleList, match_original=True)
        return circleCollection

def drawHelper(_jpgear):
    try:
        if _jpgear.units.modMult == "M":
            mod = float(_jpgear.ui.le_targetMod.text())
        elif _jpgear.units.modMult == "T":
            mod = 25.4 / float(_jpgear.ui.le_targetMod.text())
        N1 = int(_jpgear.ui.le_pN.text())
    except:
        return

    radio_button_list = [
                       _jpgear.ui.rb_1,
                       _jpgear.ui.rb_2,
                       _jpgear.ui.rb_3,
                       _jpgear.ui.rb_4,
                       _jpgear.ui.rb_5
                       ]
    N2_label_list = [
                    _jpgear.ui.lb_gN1,
                    _jpgear.ui.lb_gN2,
                    _jpgear.ui.lb_gN3,
                    _jpgear.ui.lb_gN4,
                    _jpgear.ui.lb_gN5
                    ]
    N2 = -1
    for N, radioButton in zip(N2_label_list, radio_button_list):
        if radioButton.isChecked():
            N2 = int(N.text())
            break

    Rs1 = (N1 * mod) / 2
    Rs2 = (N2 * mod) / 2

    Ro1 = ((N1 + 2) * mod) / 2

    if _jpgear.G2.type == "external":
        Ro2 = mod * (N2 + 2)/2
        CD = Rs1 + Rs2
    elif _jpgear.G2.type == "internal":
        Ro2 = mod * (N2 + 2 + 3)/2 # add an addition 3*mod for the rim thickness
        CD = Rs1 - Rs2

    circleList = []
    # pitch circle
    circleList.append(pyplot.Circle((0, 0), Rs1, color='y', ls='--', fill=False))
    circleList.append(pyplot.Circle((CD, 0), Rs2, color='y', ls='--', fill=False))
    # outer circle
    circleList.append(pyplot.Circle((0, 0), Ro1, color='g', ls='--', fill=False))
    circleList.append(pyplot.Circle((CD, 0), Ro2, color='g', ls='--', fill=False))

    circleCol = mcollections.PatchCollection(circleList, match_original=True)

    _jpgear.canvasHelper.axes.cla()

    sizeBuffer = 0.1 * Ro2
    if _jpgear.G2.type == "external":
        leftLimit = -(Ro1 + sizeBuffer) / _jpgear.units.lenMult
        rightLimit = (CD + Ro2 + sizeBuffer) / _jpgear.units.lenMult
    elif _jpgear.G2.type == "internal":
        leftLimit = (CD - (Ro2 + sizeBuffer)) / _jpgear.units.lenMult
        rightLimit = (Ro1 + sizeBuffer) / _jpgear.units.lenMult

    yLimit = (Ro2 + sizeBuffer) / _jpgear.units.lenMult
    _jpgear.canvasHelper.axes.set_xlim(left=leftLimit, right=rightLimit)
    _jpgear.canvasHelper.axes.set_ylim(bottom=-yLimit, top=yLimit)
    _jpgear.canvasHelper.axes.set_aspect('equal')

    circleCol.set_transform(mtransforms.Affine2D().scale(1/_jpgear.units.lenMult) + _jpgear.canvasHelper.axes.transData)
    _jpgear.canvasHelper.axes.add_collection(circleCol)

    _jpgear.canvasHelper.draw()

def drawGear(_jpgear, _gear, _updateAxes = False):
    if _gear.Rb < 0:
        return

    if _gear.ID == 1:
        canvas = _jpgear.canvasG1
        cb_singleTooth = _jpgear.ui.cb_singleViewG1
        cb_circles = _jpgear.ui.cb_circlesG1
    else:
        canvas = _jpgear.canvasG2
        cb_singleTooth = _jpgear.ui.cb_singleViewG2
        cb_circles = _jpgear.ui.cb_circlesG2

    if _updateAxes == False:
        leftLimit, rightLimit, bottomLimit, topLimit = canvas.axes.axis()
    else:
        # single tooth view
        if cb_singleTooth.isChecked():
            rightLimit = (_gear.Rp*sin(tau/_gear.N)) / _jpgear.units.lenMult
            leftLimit = -rightLimit
            topLimit = (_gear.Rp / _jpgear.units.lenMult) + rightLimit
            bottomLimit = (_gear.Rp / _jpgear.units.lenMult) - rightLimit
        # full gear view
        else:
            if _gear.type == "external":
                rightLimit = (_gear.Ro * 1.1) / _jpgear.units.lenMult
            elif _gear.type == "internal":
                rightLimit = (_gear.Rrim * 1.1) / _jpgear.units.lenMult
            leftLimit = -rightLimit
            topLimit = rightLimit
            bottomLimit = leftLimit

    canvas.axes.cla()

    canvas.axes.set_aspect('equal')
    canvas.axes.set_box_aspect(1)
    canvas.fig.tight_layout()

    canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
    canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

    curveCol = layoutGear(_jpgear, _gear)
    curveCol.set_transform(mtransforms.Affine2D().scale(1/_jpgear.units.lenMult) + canvas.axes.transData)
    if _gear.ID == 2:
        curveCol.set_edgecolor('r')
    canvas.axes.add_collection(curveCol)

    if cb_circles.isChecked():
        addCircles(_jpgear, _gear, canvas, _legend=True)

    canvas.draw()

def drawStress(_jpgear, _gear, _canvas, _lewisParams):
    dir = 1 if _gear.type == "external" else -1

    # setup canvas
    rightLimit = _gear.Rp*sin(tau/_gear.N)
    leftLimit = -rightLimit
    topLimit = _gear.Rp + rightLimit
    bottomLimit = _gear.Rp - rightLimit

    _canvas.axes.cla()

    _canvas.axes.set_aspect('equal')
    _canvas.axes.set_box_aspect(1)
    _canvas.fig.tight_layout()

    _canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
    _canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

    # add teeth
    curveCol = layoutGear(_jpgear, _gear)
    if _gear.ID == 2:
        curveCol.set_edgecolor('r')
        if _gear.type == "internal":
            curveCol.set_transform(mtransforms.Affine2D().scale(1/_jpgear.units.lenMult).rotate(pi/_gear.N) + _canvas.axes.transData)
    _canvas.axes.add_collection(curveCol)
    # add parabola
    Rd, gamma, x_Lewis, y_Lewis, a_Lewis = _lewisParams
    x_span = linspace(-x_Lewis*1.1, x_Lewis*1.1, 25)
    y_span = a_Lewis*x_span**2 + Rd

    paraPath = mpath.Path( list(map(list, zip(*[x_span, y_span]))) )
    paraPatch = mpatch.PathPatch(paraPath, color='g', linestyle='--', linewidth=1, fill=False, label='Lewis Parabola')
    _canvas.axes.add_patch(paraPatch)
    # add fillet circle
    # Fx = (_gear.Rr + _gear.Rf)*sin(_gear.theta_F)   # center of fillet circle
    # Fy = (_gear.Rr + _gear.Rf)*cos(_gear.theta_F)
    # _canvas.axes.add_patch(pyplot.Circle((Fx, Fy), _gear.Rf, color='c', ls='--', fill=False))
    # add intersection points
    _canvas.axes.plot([x_Lewis], [y_Lewis], color='tab:orange', marker='o', linewidth=2)
    _canvas.axes.plot([-x_Lewis], [y_Lewis], color='tab:orange', marker='o', linewidth=2)
    # Highest point of single tooth contact
    phi_hp = arccos(_gear.Rb/_gear.Rhp)
    theta_hp = (_gear.tts/(2*_gear.Rs)) + invF(_jpgear.PA) - invF(phi_hp)
    Rhp_x = dir*_gear.Rhp*sin(theta_hp)
    Rhp_y = _gear.Rhp*cos(theta_hp)
    _canvas.axes.plot([Rhp_x, 0], [Rhp_y, Rd], color='k', linestyle='--', linewidth=1)
    # _canvas.axes.plot([Rhp_x], [Rhp_y], color='r', marker='*', markersize=10, linestyle='', linewidth=3)
    # force vector arrow
    arrowSlope = (Rhp_y - Rd)/Rhp_x                 # rise over run
    tail_y = Rhp_y + (Rhp_y - Rd)*2                 # pick an arbitrary tail height
    tail_x = (tail_y - Rhp_y)/arrowSlope + Rhp_x    # calc tail_x to match slope
    dx = Rhp_x - tail_x
    dy = Rhp_y - tail_y
    arrowLength = sqrt(dx**2 + dy**2)
    tailWidth = arrowLength / 50
    arrow = mpatch.FancyArrow(tail_x, tail_y, dx, dy, width=tailWidth, length_includes_head=True, color='k')
    _canvas.axes.add_patch(arrow)

    _canvas.axes.legend(loc='upper right', framealpha=1.0)
    _canvas.draw()

def drawMesh(_jpgear, _updateAxes = False):
    G1 = _jpgear.G1
    G2 = _jpgear.G2
    lenMult = _jpgear.units.lenMult

    if G1.Rb < 0 or G2.Rb < 0:
        return

    canvas = _jpgear.canvasMesh
    cb_singleTooth = _jpgear.ui.cb_singleViewMesh
    cb_circles = _jpgear.ui.cb_circlesMesh

    if _updateAxes == False:
        leftLimit, rightLimit, bottomLimit, topLimit = canvas.axes.axis()
    else:
        # tight mesh view
        if cb_singleTooth.isChecked():
            topLimit = (G1.Rp*sin(tau/G1.N)) / lenMult
            bottomLimit = -topLimit
            leftLimit = (G1.Rp / lenMult) - topLimit
            rightLimit = (G1.Rp / lenMult) + topLimit
        # full gear view
        else:
            if _jpgear.G2.type == "external":
                sizeBuffer = 0.1 * G2.Ro
                leftLimit = (-G1.Ro - sizeBuffer) / lenMult
                rightLimit = (_jpgear.CD + G2.Ro + sizeBuffer) / lenMult
            elif _jpgear.G2.type == "internal":
                sizeBuffer = 0.1 * G2.Rrim
                leftLimit = (-_jpgear.CD - G2.Rrim - sizeBuffer) / lenMult
                rightLimit = (G2.Rrim - _jpgear.CD + sizeBuffer) / lenMult

            topLimit = (max(G1.Ro, G2.Ro) + sizeBuffer) / lenMult
            bottomLimit = -topLimit

    canvas.axes.cla()

    canvas.axes.set_aspect('equal')
    canvas.axes.set_box_aspect(1)
    canvas.fig.tight_layout()

    canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
    canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

    # Points for line of contact
    dir = 1 if G2.type == "external" else -1
    # pitch point
    x0 = G1.Rp
    y0 = 0
    if G2.type == "external":
        # tangent to gear 1 at base circle
        x1 = G1.Rb*cos(_jpgear.OPA)
        y1 = G1.Rb*sin(_jpgear.OPA)
        # tangent to gear 2 at base circle
        x2 = (_jpgear.CD - G2.Rb*cos(_jpgear.OPA)) * dir
        y2 = (-G2.Rb*sin(_jpgear.OPA)) * dir
        # find end of contact on LoC at Roe
        # law of sines => A/sin(a) = B/sin(b)
        a = _jpgear.OPA + deg2rad(90)
        b = arcsin( (G1.Rp/G1.Roe) * sin(a) )
        c = deg2rad(180) - a - b
        x3 = G1.Roe * cos(c)
        y3 = -G1.Roe * sin(c)
        b = arcsin( (G2.Rp/G2.Roe) * sin(a) )
        c = deg2rad(180) - a - b
        x4 = _jpgear.CD - (G2.Roe * cos(c))
        y4 = G2.Roe * sin(c)
    elif G2.type == "internal":
        # tangent to gear 2 at base circle
        x1 = (_jpgear.CD - G2.Rb*cos(_jpgear.OPA)) * dir
        y1 = (-G2.Rb*sin(_jpgear.OPA)) * dir
        # intersect gear 2 at rim
        # law of sines => A/sin(a) = B/sin(b)
        a = _jpgear.OPA + deg2rad(90)
        b = arcsin( (G2.Rp/G2.Rrim) * sin(a) )
        c = deg2rad(180) - a - b
        x2 = -_jpgear.CD + (G2.Rrim * cos(c))
        y2 = -G2.Rrim * sin(c)
        # find end of contact on LoC at Roe
        b = arcsin( (G1.Rp/G1.Roe) * sin(a) )
        c = deg2rad(180) - a - b
        x3 = G1.Roe * cos(c)
        y3 = -G1.Roe * sin(c)
        b = arcsin( (G2.Rp/G2.Rr) * sin(a) )
        c = deg2rad(180) - a - b
        x4 = -_jpgear.CD + (G2.Rr * cos(c))
        y4 = -G2.Rr * sin(c)
    # scale to the right units
    x1 = x1 / lenMult
    x2 = x2 / lenMult
    x3 = x3 / lenMult
    x4 = x4 / lenMult
    y1 = y1 / lenMult
    y2 = y2 / lenMult
    y3 = y3 / lenMult
    y4 = y4 / lenMult

    # config slider
    slider = _jpgear.ui.hSlider_Mesh
    # pitch point happens at slider=1
    # find overshoot for gear two
    if G2.type == "external":
        sliderMin = 0
        over_angle = arctan(-y2/x2)
        overshoot = over_angle / _jpgear.OPA
    elif G2.type == "internal":
        under_angle = arctan(y1/x1)
        sliderMin = 1 - under_angle / _jpgear.OPA
        over_angle = arctan(-y2/x2)
        overshoot = over_angle / _jpgear.OPA
    sliderMax = 1 + overshoot

    slider.setMinimum(int(sliderMin * _jpgear.sliderScale))
    slider.setMaximum(int(sliderMax * _jpgear.sliderScale))

    # make the teeth mesh nicely
    ratio = G1.N / G2.N
    # profile angle at pitch circle
    phi_P1 = arccos(G1.Rb/G1.Rp)
    phi_P2 = arccos(G2.Rb/G2.Rp)
    # angle from tooth centerline to pitchpoint
    theta_P1 = G1.tt/(2*G1.Rp)
    theta_P2 = G2.tt/(2*G2.Rp)
    # angle where teeth meet at pitchpoint
    startAngle1 = -pi/2 + theta_P1
    startAngle2 = (pi/2 * dir) + theta_P2
    # roll back to where LoC meets the base circle
    curveStartAngle1 = startAngle1 + _jpgear.OPA + invF(_jpgear.OPA)
    curveStartAngle2 = startAngle2 - dir * ratio * (_jpgear.OPA + invF(_jpgear.OPA))

    phi_A = float(slider.value() / _jpgear.sliderScale) * _jpgear.OPA
    updateAngle = phi_A + invF(phi_A)

    angle1 = curveStartAngle1 - (updateAngle)
    angle2 = curveStartAngle2 + (updateAngle * ratio * dir)

    # draw everything
    curveCol1 = layoutGear(_jpgear, G1)
    curveCol2 = layoutGear(_jpgear, G2)
    curveCol2.set_edgecolor('r')

    curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1).scale(1/lenMult) + canvas.axes.transData)
    curveCol2.set_transform(mtransforms.Affine2D().rotate(angle2).scale(1/lenMult).translate(dir * _jpgear.CD/lenMult, 0) + canvas.axes.transData)
    canvas.axes.add_collection(curveCol1)
    canvas.axes.add_collection(curveCol2)

    if cb_circles.isChecked():
        addCircles(_jpgear, G1, canvas, _legend=True)

        circleCol2 = addCircles(_jpgear, G2, canvas, _legend=False)
        circleCol2.set_transform(mtransforms.Affine2D().translate((_jpgear.CD*dir)/lenMult, 0) + canvas.axes.transData)
        canvas.axes.add_collection(circleCol2)

    if _jpgear.ui.cb_LoC.isChecked():
        # line of contact
        canvas.axes.plot([x1,x2],[y1,y2], color='k', marker='x', linestyle='--', linewidth=1)
        loc, = canvas.axes.plot([x3,x4],[y3,y4], color='k', marker='x', linewidth=2, label='Line of Contact')
        # contact point
        traceAngle = _jpgear.OPA - phi_A
        R = (G1.Rb/cos(phi_A)) / lenMult
        traceX = R*cos(traceAngle)
        traceY = R*sin(traceAngle)
        tracePoint, = canvas.axes.plot([traceX], [traceY], color='tab:orange', marker='o', linestyle='', linewidth=2, label='Point of Contact')
        legendPoint = canvas.axes.legend(handles=[loc, tracePoint], loc='lower left', framealpha=1.0)
        canvas.axes.add_artist(legendPoint)

        # HP_angle = arcsin((G1.Rp/G1.Rhp)*sin(_jpgear.OPA + deg2rad(90)))
        # HP_X = G1.Rhp*cos(deg2rad(180) - HP_angle - _jpgear.OPA - deg2rad(90))
        # HP_Y = -G1.Rhp*sin(deg2rad(180) - HP_angle- _jpgear.OPA - deg2rad(90))
        # HP_Point, = canvas.axes.plot([HP_X], [HP_Y], color='r', marker='o', linestyle='', linewidth=2, label='HPSTC')
        # canvas.axes.add_artist(HP_Point)

    canvas.draw()
def createAnimWindow(_jpgear):
    G1 = _jpgear.G1
    G2 = _jpgear.G2
    lenMult = _jpgear.units.lenMult

    if G1.Rb < 0 or G2.Rb < 0:
        return

    window = PopupWindow(_jpgear)
    window.setWindowTitle("Mesh Animation")

    window.ui.vLayout_popup.insertWidget(0, window.canvas)
    toolbar = NavigationToolbar2QT(window.canvas, _jpgear)
    window.ui.hLayout_toolbarAnim.insertWidget(0, toolbar)

    window.updateAnimAxes()
    window.canvas.axes.set_aspect('equal')
    window.canvas.fig.tight_layout()

    curveCol1 = layoutGear(_jpgear, G1)
    curveCol2 = layoutGear(_jpgear, G2)
    curveCol2.set_edgecolor('r')

    window.canvas.axes.add_collection(curveCol1)
    window.canvas.axes.add_collection(curveCol2)

    # animation specs
    slider = window.ui.hSlider_Speed
    maxSpeed = slider.maximum()             # RPM
    msPerRev = (60*1000)/maxSpeed           # milliseconds per revolution
    interval = 30                           # ms per frame
    framesPerRev = int(msPerRev / interval)	# frames for one rev
    ratio = G1.N / G2.N
    # starting position
    dir = 1 if G2.type == "external" else -1
    offset = pi/G2.N if G2.type == "external" else 0
    startAngle1 = -pi/2
    startAngle2 = (pi/2 - 0.5*_jpgear.bkl/G2.Rs) * dir + offset

    def animFunc(frame, _maxSpeed, _slider):
        speed = float(_slider.value())
        updateAngle = (speed/_maxSpeed) * (tau*frame)/framesPerRev

        angle1 = startAngle1 - updateAngle
        angle2 = startAngle2 + (ratio*updateAngle*dir)

        curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1).scale(1/lenMult) + window.canvas.axes.transData)
        curveCol2.set_transform(mtransforms.Affine2D().rotate(angle2).scale(1/lenMult).translate(dir*_jpgear.CD/lenMult, 0) + window.canvas.axes.transData)

    window.anim = manimation.FuncAnimation(window.canvas.fig, animFunc, fargs=[maxSpeed, slider], frames=framesPerRev, interval=interval)

    window.canvas.draw()

    window.show()
