from helper import tau, Type, invF, revInvF
from PopupWindow import PopupWindow

from numpy import pi, sin, cos, tan, arcsin, arccos, arctan, sqrt
from numpy import linspace, rad2deg, deg2rad

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
    # Rjfi = G.Rb/(cos(G.phi_JFI))
    theta_JFI = G.tts/(2*G.Rs) + invF(_jpgear.PA) - invF(G.phi_JFI)
    Rjfi_x = G.Rjfi*sin(theta_JFI)
    Rjfi_y = G.Rjfi*cos(theta_JFI)
    # create vectors of points along the involute
    RA = linspace(G.Rjfi, G.Roe, 20)
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
        elif G.ID == 2:
            defaultName = 'gear2.dxf'
        else:
            defaultName = 'gear3.dxf'

        savePath, selectedFilter = QFileDialog.getSaveFileName(None, 'Save Gear'+str(G.ID), defaultName)

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
    circleList.append(pyplot.Circle((0, 0), _gear.Roe / _jpgear.units.lenMult, color='limegreen', ls='--', fill=False, label='Outer Circle'))
    # # root cirlce
    circleList.append(pyplot.Circle((0, 0), _gear.Rr / _jpgear.units.lenMult, color='tomato', ls='--', fill=False, label='Root Circle'))

    # adding a legend only works if the circles are added individually, instead of as a collection
    if _legend == True:
        for circle in circleList:
            _canvas.axes.add_patch(circle)

        legendCircle = _canvas.axes.legend(loc='upper right', framealpha=1.0)
        _canvas.axes.add_artist(legendCircle)

    else:
        circleCollection = mcollections.PatchCollection(circleList, match_original=True)
        return circleCollection

def drawHelper(_jpgear, _N1, _N2, _N3, _p):
    try:
        if _jpgear.units.modMult == "M":
            mod = float(_jpgear.ui.le_targetMod.text())
        elif _jpgear.units.modMult == "T":
            mod = 25.4 / float(_jpgear.ui.le_targetMod.text())
    except:
        # print("[drawHelper] bad mod")
        return

    Rs1 = (_N1 * mod) / 2
    Rs2 = (_N2 * mod) / 2

    Ro1 = ((_N1 + 2) * mod) / 2

    if _jpgear.type == Type.external:
        Ro2 = mod * (_N2 + 2)/2
        CD = Rs1 + Rs2
    elif _jpgear.type == Type.internal:
        Ro2 = mod * (_N2 + 2 + 3)/2 # add an addition 3*mod for the rim thickness
        CD = Rs1 - Rs2
    elif _jpgear.type == Type.planetary:
        Ro2 = mod * (_N2 + 2 + 3)/2 # add an addition 3*mod for the rim thickness
        CD = 0
        Rs3 = (_N3 * mod) / 2
        Ro3 = mod * (_N3 + 2)/2

    circleList = []
    # pitch circle
    circleList.append(pyplot.Circle((0, 0), Rs1, color='y', ls='--', fill=False))
    circleList.append(pyplot.Circle((CD, 0), Rs2, color='y', ls='--', fill=False))
    # outer circle
    circleList.append(pyplot.Circle((0, 0), Ro1, color='g', ls='--', fill=False))
    circleList.append(pyplot.Circle((CD, 0), Ro2, color='g', ls='--', fill=False))

    if _jpgear.type == Type.planetary:
        circS = pyplot.Circle((0, Rs1+Rs3), Rs3, color='y', ls='--', fill=False)
        circO = pyplot.Circle((0, Rs1+Rs3), Ro3, color='g', ls='--', fill=False)

        for n in range(_p):
            angle = (n/_p)*tau - pi/2
            newCircS = copy.copy(circS)
            newCircS.set_transform(mtransforms.Affine2D().rotate(angle))
            circleList.append(newCircS)
            newCircO = copy.copy(circO)
            newCircO.set_transform(mtransforms.Affine2D().rotate(angle))
            circleList.append(newCircO)

    circleCol = mcollections.PatchCollection(circleList, match_original=True)

    _jpgear.canvasHelper.axes.cla()

    sizeBuffer = 0.1 * Ro2
    if _jpgear.type == Type.external:
        leftLimit = -(Ro1 + sizeBuffer) / _jpgear.units.lenMult
        rightLimit = (CD + Ro2 + sizeBuffer) / _jpgear.units.lenMult
    elif _jpgear.type == Type.internal:
        leftLimit = (CD - (Ro2 + sizeBuffer)) / _jpgear.units.lenMult
        rightLimit = (Ro1 + sizeBuffer) / _jpgear.units.lenMult
    elif _jpgear.type == Type.planetary:
        leftLimit = (-(Ro2 + sizeBuffer)) / _jpgear.units.lenMult
        rightLimit = (Ro2 + sizeBuffer) / _jpgear.units.lenMult

    yLimit = (Ro2 + sizeBuffer) / _jpgear.units.lenMult
    _jpgear.canvasHelper.axes.set_xlim(left=leftLimit, right=rightLimit)
    _jpgear.canvasHelper.axes.set_ylim(bottom=-yLimit, top=yLimit)
    _jpgear.canvasHelper.axes.set_aspect('equal')

    circleCol.set_transform(mtransforms.Affine2D().scale(1/_jpgear.units.lenMult) + _jpgear.canvasHelper.axes.transData)
    _jpgear.canvasHelper.axes.add_collection(circleCol)

    _jpgear.canvasHelper.draw()

def drawAllGears(_jpgear, _updateAxes=True):
    if _jpgear.updateGears():
        return
    for gear in _jpgear.gearList:
        drawGear(_jpgear, gear, _updateAxes=_updateAxes)
    drawMesh(_jpgear, _updateAxes=_updateAxes)

def drawGear(_jpgear, _gear, _updateAxes = False):
    if _gear.Rb < 0:
        return

    match _gear.ID:
        case 1:
            canvas = _jpgear.canvasG1
            cb_singleTooth = _jpgear.ui.cb_singleViewG1
            cb_circles = _jpgear.ui.cb_circlesG1
            color = 'b'
        case 2:
            canvas = _jpgear.canvasG2
            cb_singleTooth = _jpgear.ui.cb_singleViewG2
            cb_circles = _jpgear.ui.cb_circlesG2
            color = 'r'
        case 3:
            canvas = _jpgear.canvasG3
            cb_singleTooth = _jpgear.ui.cb_singleViewG3
            cb_circles = _jpgear.ui.cb_circlesG3
            color = 'g'

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
    curveCol.set_edgecolor(color)
    canvas.axes.add_collection(curveCol)

    if cb_circles.isChecked():
        addCircles(_jpgear, _gear, canvas, _legend=True)

    canvas.draw()

def drawMesh(_jpgear, _updateAxes = False):
    G1 = _jpgear.G1
    G2 = _jpgear.G2
    G3 = _jpgear.G3
    lenMult = _jpgear.units.lenMult

    if G1.Rb < 0 or G2.Rb < 0:
        # print("[drawMesh] bad Rb1 or Rb2")
        return

    if _jpgear.type == Type.planetary and G3.Rb < 0:
        # print("[drawMesh] bad Rb3")
        return

    # setup canvas
    canvas = _jpgear.canvasMesh
    if _updateAxes == False:
        leftLimit, rightLimit, bottomLimit, topLimit = canvas.axes.axis()
    else:
        tightView = _jpgear.ui.cb_singleViewMesh.isChecked()
        mesh = None
        if _jpgear.type == Type.planetary:
            mesh = 0 if _jpgear.ui.rb_sp.isChecked() else 1
        leftLimit, rightLimit, bottomLimit, topLimit = getMeshLimits(_jpgear, tightView, mesh)

    canvas.axes.cla()
    canvas.axes.set_aspect('equal')
    canvas.axes.set_box_aspect(1)
    canvas.fig.tight_layout()

    canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
    canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

    # get slider position
    slider = _jpgear.ui.hSlider_Mesh
    # 0 at base circle, 1 at pitch point
    updateAngle = float(slider.value() / _jpgear.sliderScale) * (_jpgear.OPA1 + invF(_jpgear.OPA1))

    # get LoC points and angles
    # pitch point happens at slider=1, find overshoot for gear two
    match _jpgear.type:
        case Type.external:
            x, y = getLoCPointsExternal(_jpgear, G1, G2)
            sliderMin = 0
            phi_over = arctan(-y[2]/x[2]) + _jpgear.OPA1
            sliderMax = tan(phi_over) / tan(_jpgear.OPA1)

            # roll back to where LoC meets the base circle
            startAngles = getStartAngles(_jpgear)
            angle1 = startAngles[0] - updateAngle
            angle2 = startAngles[1] + (updateAngle * (G1.N/G2.N))

        case Type.internal:
            x, y = getLoCPointsInternal(_jpgear, G1, G2, 1)
            sliderMin = -(G2.N/G1.N - 1)
            phi_over = arctan(-y[2]/x[2]) + _jpgear.OPA1
            sliderMax = tan(phi_over) / tan(_jpgear.OPA1)

            # roll back to where LoC meets the base circle
            startAngles = getStartAngles(_jpgear)
            angle1 = startAngles[0] - updateAngle
            angle2 = startAngles[1] - (updateAngle * (G1.N/G2.N))

        case Type.planetary:
            x, y = getLoCPointsExternal(_jpgear, G1, G3)
            xP, yP = getLoCPointsInternal(_jpgear, G3, G2, 2)
            sliderMin = -(G2.N/G1.N - 1)
            phi_over = arctan(-y[2]/x[2]) + _jpgear.OPA1
            sliderMax = tan(phi_over) / tan(_jpgear.OPA1)

            # roll back to where LoC meets the base circle
            startAngles = getStartAngles(_jpgear)
            angle1 = startAngles[0] - updateAngle
            angle2 = startAngles[1] + (updateAngle * (G1.N/G2.N))
            angle3 = startAngles[2] + (updateAngle * (G1.N/G3.N))

    # set slider limits
    slider.setMinimum(int(sliderMin * _jpgear.sliderScale))
    slider.setMaximum(int(sliderMax * _jpgear.sliderScale))

    # draw everything
    match _jpgear.type:
        case Type.external:
            curveCol1 = layoutGear(_jpgear, G1)
            curveCol2 = layoutGear(_jpgear, G2)
            curveCol2.set_edgecolor('r')

            curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1).scale(1/lenMult) + canvas.axes.transData)
            curveCol2.set_transform(mtransforms.Affine2D().rotate(angle2).scale(1/lenMult).translate(_jpgear.CD/lenMult, 0) + canvas.axes.transData)
            canvas.axes.add_collection(curveCol1)
            canvas.axes.add_collection(curveCol2)

            if _jpgear.ui.cb_circlesMesh.isChecked():
                addCircles(_jpgear, G1, canvas, _legend=True)
                circleCol2 = addCircles(_jpgear, G2, canvas, _legend=False)
                circleCol2.set_transform(mtransforms.Affine2D().translate((_jpgear.CD)/lenMult, 0) + canvas.axes.transData)
                canvas.axes.add_collection(circleCol2)

        case Type.internal:
            curveCol1 = layoutGear(_jpgear, G1)
            curveCol2 = layoutGear(_jpgear, G2)
            curveCol2.set_edgecolor('r')

            curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1).scale(1/lenMult) + canvas.axes.transData)
            curveCol2.set_transform(mtransforms.Affine2D().rotate(angle2).scale(1/lenMult).translate(-_jpgear.CD/lenMult, 0) + canvas.axes.transData)
            canvas.axes.add_collection(curveCol1)
            canvas.axes.add_collection(curveCol2)

            if _jpgear.ui.cb_circlesMesh.isChecked():
                addCircles(_jpgear, G1, canvas, _legend=True)
                circleCol2 = addCircles(_jpgear, G2, canvas, _legend=False)
                circleCol2.set_transform(mtransforms.Affine2D().translate((-_jpgear.CD)/lenMult, 0) + canvas.axes.transData)
                canvas.axes.add_collection(circleCol2)

        case Type.planetary:
            curveCol1 = layoutGear(_jpgear, G1)
            curveCol2 = layoutGear(_jpgear, G2)
            curveCol2.set_edgecolor('r')

            curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1).scale(1/lenMult) + canvas.axes.transData)
            curveCol2.set_transform(mtransforms.Affine2D().rotate(angle2).scale(1/lenMult) + canvas.axes.transData)

            canvas.axes.add_collection(curveCol1)
            canvas.axes.add_collection(curveCol2)

            if _jpgear.ui.cb_circlesMesh.isChecked():
                addCircles(_jpgear, G1, canvas, _legend=True)
                circleCol2 = addCircles(_jpgear, G2, canvas, _legend=False)
                canvas.axes.add_collection(circleCol2)

            curveCol3 = layoutGear(_jpgear, G3)
            curveCol3.set_edgecolor('g')
            curveCol3.set_transform(mtransforms.Affine2D().rotate(angle3).scale(1/lenMult).translate(_jpgear.CD/lenMult, 0) + canvas.axes.transData)

            NP = _jpgear.NPlanets
            for n in range(NP):
                revAngle = (n/NP)*tau
                rotAngle = revAngle * G1.N/G3.N
                newCC = copy.copy(curveCol3)
                newCC.set_transform(mtransforms.Affine2D().rotate(angle3+rotAngle).scale(1/lenMult).translate(_jpgear.CD/lenMult, 0).rotate(revAngle) + canvas.axes.transData)
                canvas.axes.add_collection(newCC)

                if _jpgear.ui.cb_circlesMesh.isChecked():
                    circleColP = addCircles(_jpgear, G3, canvas, _legend=False)
                    circleColP.set_transform(mtransforms.Affine2D().translate(_jpgear.CD/lenMult, 0).rotate(revAngle) + canvas.axes.transData)
                    canvas.axes.add_collection(circleColP)

    if _jpgear.ui.cb_LoC.isChecked():
        # line of contact
        canvas.axes.plot([x[1],x[2]],[y[1],y[2]], color='k', marker='x', linestyle='--', linewidth=1)
        loc, = canvas.axes.plot([x[3],x[4]],[y[3],y[4]], color='k', marker='x', linewidth=2, label='Line of Contact')
        # contact point
        phi = arctan(updateAngle)
        traceAngle = _jpgear.OPA1 - phi
        R = (G1.Rb/cos(phi)) / lenMult
        traceX = R*cos(traceAngle)
        traceY = R*sin(traceAngle)
        tracePoint, = canvas.axes.plot([traceX], [traceY], color='tab:orange', marker='o', linestyle='', linewidth=2, label='Point of Contact')
        legendPoint = canvas.axes.legend(handles=[loc, tracePoint], loc='lower left', framealpha=1.0)
        canvas.axes.add_artist(legendPoint)

        if _jpgear.type == Type.planetary:
            canvas.axes.plot([xP[1],xP[2]],[-yP[1],-yP[2]], color='k', marker='x', linestyle='--', linewidth=1)
            loc, = canvas.axes.plot([xP[3],xP[4]],[-yP[3],-yP[4]], color='k', marker='x', linewidth=2, label='Line of Contact')

            if G3.N%2 == 0:
                # angle from horizontal to centerline of imaginary tooth if it touched the pitch point
                alphaC1 = G3.tt/(2*G3.Rp)
                # gamma of tooth if it touched the pitch point, relative to horizontal
                gammaH = _jpgear.OPA2
                # gamma of pitch tooth relative to its own centerline
                gamma1 = gammaH - alphaC1
                # angle from horizontal to center of previous tooth
                alphaC2 = (tau/G3.N) - alphaC1
                # gamma of previous tooth relative to its own centerline
                gamma2 = gamma1 - (alphaC2 - alphaC1)
                # profile angle of previous tooth
                # GOIG 2.39
                phi2 = arctan((gamma2) + invF(_jpgear.PA) + (G3.tts/(2*G3.Rs)))
                theta = (G3.tts/(2*G3.Rs)) + invF(_jpgear.PA) - invF(phi2)
                # angle from base of tooth to horizontal when at pitch position (i.e. slider=1)
                base_offset = alphaC2 - theta - invF(phi2)

            else:
                base_offset = pi/G3.N - (G3.tt/(G3.Rp)) - invF(_jpgear.OPA2)

            # roll back to base circle
            base_start = base_offset + tan(_jpgear.OPA1)*(G1.N/G3.N)
            base_angle = updateAngle*(G1.N/G3.N) - base_start

            phi = arctan(base_angle + _jpgear.OPA2)
            R = G3.Rb/cos(phi)
            traceAngle = phi - _jpgear.OPA2
            traceX = R*cos(traceAngle) + _jpgear.CD
            traceY = R*sin(traceAngle)
            tracePointP, = canvas.axes.plot([traceX], [traceY], color='tab:orange', marker='o', linestyle='', linewidth=2, label='Point of Contact')

    canvas.draw()

def getMeshLimits(_jpgear, _tight, _mesh=0):
    if _jpgear.type == Type.external:
        if _tight:
            topLimit = (_jpgear.G1.Rp*sin(tau/_jpgear.G1.N)) / _jpgear.units.lenMult
            bottomLimit = -topLimit
            leftLimit = (_jpgear.G1.Rp / _jpgear.units.lenMult) - topLimit
            rightLimit = (_jpgear.G1.Rp / _jpgear.units.lenMult) + topLimit
        else:
            sizeBuffer = 0.1 * _jpgear.G2.Ro
            leftLimit = (-_jpgear.G1.Ro - sizeBuffer) / _jpgear.units.lenMult
            rightLimit = (_jpgear.CD + _jpgear.G2.Ro + sizeBuffer) / _jpgear.units.lenMult
            topLimit = (max(_jpgear.G1.Ro, _jpgear.G2.Ro) + sizeBuffer) / _jpgear.units.lenMult
            bottomLimit = -topLimit

    if _jpgear.type == Type.internal:
        if _tight:
            topLimit = (_jpgear.G1.Rp*sin(tau/_jpgear.G1.N)) / _jpgear.units.lenMult
            bottomLimit = -topLimit
            rightLimit = (_jpgear.G1.Rp / _jpgear.units.lenMult) + topLimit
            leftLimit = (_jpgear.G1.Rp / _jpgear.units.lenMult) - topLimit
        else:
            sizeBuffer = 0.1 * _jpgear.G2.Rrim
            leftLimit = (-_jpgear.CD - _jpgear.G2.Rrim - sizeBuffer) / _jpgear.units.lenMult
            rightLimit = (_jpgear.G2.Rrim - _jpgear.CD + sizeBuffer) / _jpgear.units.lenMult
            topLimit = (_jpgear.G2.Rrim + sizeBuffer) / _jpgear.units.lenMult
            bottomLimit = -topLimit

    if _jpgear.type == Type.planetary:
        if _tight:
            if _mesh == 0:
                topLimit = (_jpgear.G1.Rp*sin(tau/_jpgear.G1.N)) / _jpgear.units.lenMult
                bottomLimit = -topLimit
                rightLimit = (_jpgear.G1.Rp / _jpgear.units.lenMult) + topLimit
                leftLimit = (_jpgear.G1.Rp / _jpgear.units.lenMult) - topLimit
            elif _mesh == 1:
                sizeBuffer = 0.1 * _jpgear.G2.Rrim
                topLimit = (_jpgear.G3.Rp*sin(tau/_jpgear.G3.N)) / _jpgear.units.lenMult
                bottomLimit = -topLimit
                rightLimit = ((_jpgear.G1.Rp + 2*_jpgear.G3.Rp) / _jpgear.units.lenMult) + topLimit
                leftLimit = ((_jpgear.G1.Rp + 2*_jpgear.G3.Rp) / _jpgear.units.lenMult) - topLimit
        else:
            sizeBuffer = 0.1 * _jpgear.G2.Rrim
            topLimit = (_jpgear.G2.Rrim + sizeBuffer) / _jpgear.units.lenMult
            bottomLimit = -topLimit
            rightLimit = topLimit
            leftLimit = -rightLimit

    return leftLimit, rightLimit, bottomLimit, topLimit

def getLoCPointsExternal(_jpgear, _G1, _G2):
    # pitch point
    x0 = _G1.Rp
    y0 = 0
    # tangent to gear 1 at base circle
    x1 = _G1.Rb*cos(_jpgear.OPA1)
    y1 = _G1.Rb*sin(_jpgear.OPA1)
    # tangent to gear 2 at base circle
    x2 = (_jpgear.CD - _G2.Rb*cos(_jpgear.OPA1))
    y2 = (-_G2.Rb*sin(_jpgear.OPA1))
    # find end of contact on LoC at Roe
    # law of sines => A/sin(a) = B/sin(b)
    a = _jpgear.OPA1 + deg2rad(90)
    b = arcsin( (_G1.Rp/_G1.Roe) * sin(a) )
    c = deg2rad(180) - a - b
    x3 = _G1.Roe * cos(c)
    y3 = -_G1.Roe * sin(c)
    b = arcsin( (_G2.Rp/_G2.Roe) * sin(a) )
    c = deg2rad(180) - a - b
    x4 = _jpgear.CD - (_G2.Roe * cos(c))
    y4 = _G2.Roe * sin(c)

    # Cjfi = sqrt(_G1.Rp**2 - _G1.Rb**2) - sqrt(_G1.Rjfi**2 - _G1.Rb**2)
    # x5 = _G1.Rp - Cjfi*sin(_jpgear.OPA1)
    # y5 = Cjfi*cos(_jpgear.OPA1)

    # Cjfi = sqrt(_G2.Rp**2 - _G2.Rb**2) - sqrt(_G2.Rjfi**2 - _G2.Rb**2)
    # x6 = _G1.Rp + Cjfi*sin(_jpgear.OPA1)
    # y6 = -Cjfi*cos(_jpgear.OPA1)


    xList = [x0, x1, x2, x3, x4]
    xList[:] = [x / _jpgear.units.lenMult for x in xList]
    yList = [y0, y1, y2, y3, y4]
    yList[:] = [y / _jpgear.units.lenMult for y in yList]

    return xList, yList

def getLoCPointsInternal(_jpgear, _G1, _G2, _n):
    if _n == 1:
        OPA = _jpgear.OPA1
        shift = 0
    elif _n == 2:
        OPA = _jpgear.OPA2
        shift = _jpgear.CD

    # pitch point
    # x0 = _G1.Rp
    x0 = _G1.Rp + shift
    y0 = 0
    # tangent to gear 2 at base circle
    x1 = -_jpgear.CD + shift + _G2.Rb*cos(OPA)
    y1 = _G2.Rb*sin(OPA)
    # intersect gear 2 at rim
    # law of sines => A/sin(a) = B/sin(b)
    a = OPA + deg2rad(90)
    b = arcsin( (_G2.Rp/_G2.Rrim) * sin(a) )
    c = deg2rad(180) - a - b
    x2 = -_jpgear.CD + shift + (_G2.Rrim * cos(c))
    y2 = -_G2.Rrim * sin(c)
    # find end of contact on LoC at Roe
    b = arcsin( (_G1.Rp/_G1.Roe) * sin(a) )
    c = deg2rad(180) - a - b
    x3 = _G1.Roe * cos(c) + shift
    y3 = -_G1.Roe * sin(c)
    # find end of contact on LoC at JFI
    R_JFI = _G2.Rb/cos(_G2.phi_JFI)
    # b = arcsin( (_G2.Rp/_G2.Rr) * sin(a) )
    b = arcsin( (_G2.Rp/R_JFI) * sin(a) )
    c = deg2rad(180) - a - b
    x4 = -_jpgear.CD + shift + (R_JFI * cos(c))
    # x4 = -_jpgear.CD + (_G2.Rr * cos(c))
    y4 = -R_JFI * sin(c)
    # y4 = -_G2.Rr * sin(c)

    xList = [x0, x1, x2, x3, x4]
    xList[:] = [x / _jpgear.units.lenMult for x in xList]

    yList = [y0, y1, y2, y3, y4]
    yList[:] = [y / _jpgear.units.lenMult for y in yList]

    return xList, yList

def getPitchAngles(_jpgear, _G1, _G2, _n, _dir):
    # make the teeth mesh nicely
    ratio = _G1.N / _G2.N
    # angle from tooth centerline to pitchpoint
    theta_P1 = _G1.tt/(2*_G1.Rp)
    theta_P2 = _G2.tt/(2*_G2.Rp)
    # angle where teeth meet at pitchpoint
    pitchAngle1 = -pi/2 + theta_P1

    if _n == 1:
        pitchAngle2 = (pi/2*_dir) + theta_P2
    elif _n == 2:
        pitchAngle2 = (pi/2*_dir) - theta_P2 + ratio*(pi + 2*theta_P1)

    return [pitchAngle1, pitchAngle2]

def getStartAngles(_jpgear):
    startAngles = [0, 0, 0]

    match _jpgear.type:
        case Type.external:
            ratio = _jpgear.G1.N/_jpgear.G2.N
            pitchAngles = getPitchAngles(_jpgear, _jpgear.G1, _jpgear.G2, 1, 1)
            startAngles[0] = pitchAngles[0] + _jpgear.OPA1 + invF(_jpgear.OPA1)
            startAngles[1] = pitchAngles[1] - ratio*(_jpgear.OPA1 + invF(_jpgear.OPA1))

        case Type.internal:
            ratio = _jpgear.G1.N/_jpgear.G2.N
            pitchAngles = getPitchAngles(_jpgear, _jpgear.G1, _jpgear.G2, 1, -1)
            startAngles[0] = pitchAngles[0] + _jpgear.OPA1 + invF(_jpgear.OPA1)
            startAngles[1] = pitchAngles[1] + ratio*(_jpgear.OPA1 + invF(_jpgear.OPA1))

        case Type.planetary:
            ratio1 = _jpgear.G1.N/_jpgear.G3.N
            pitchAngles = getPitchAngles(_jpgear, _jpgear.G1, _jpgear.G3, 1, 1)
            startAngles[0] = pitchAngles[0] + _jpgear.OPA1 + invF(_jpgear.OPA1)
            startAngles[2] = pitchAngles[1] - ratio1*(_jpgear.OPA1 + invF(_jpgear.OPA1))

            ratio2 = _jpgear.G1.N/_jpgear.G2.N
            pitchAnglesP = getPitchAngles(_jpgear, _jpgear.G3, _jpgear.G2, 2, -1)
            startAngles[1] = pitchAnglesP[1] - ratio2*(_jpgear.OPA1 + invF(_jpgear.OPA1))

    return startAngles

def createAnimWindow(_jpgear):
    G1 = _jpgear.G1
    G2 = _jpgear.G2
    G3 = _jpgear.G3
    lenMult = _jpgear.units.lenMult

    if G1.Rb < 0 or G2.Rb < 0:
        # print("[createAnimWindow] bad Rb1 or Rb2")
        return

    if _jpgear.type == Type.planetary and G3.Rb < 0:
        # print("[createAnimWindow] bad Rb3")
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

    if _jpgear.type == Type.planetary:
        curveCol3 = layoutGear(_jpgear, G3)
        curveCol3.set_edgecolor('g')
        curveCol3List = []

        NP = _jpgear.NPlanets
        for n in range(NP):
            curveCol3List.append(copy.copy(curveCol3))
            window.canvas.axes.add_collection(curveCol3List[n])

    # animation specs
    slider = window.ui.hSlider_Speed
    maxSpeed = slider.maximum()                 # RPM
    msPerRev = (60*1000)/maxSpeed               # milliseconds per revolution
    interval = 30                               # ms per frame
    framesPerRev = int(msPerRev / interval)	# frames for one rev
    ratio = G1.N / G2.N

    # starting position
    startAngles = getStartAngles(_jpgear)

    def animFunc(frame, _maxSpeed, _slider, _type):
        speed = float(_slider.value())
        updateAngle = (speed/_maxSpeed) * (tau*frame)/framesPerRev

        match _type:
            case Type.external:
                angle1 = startAngles[0] - updateAngle
                angle2 = startAngles[1] + (updateAngle*(G1.N/G2.N))

                curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1).scale(1/lenMult) + window.canvas.axes.transData)
                curveCol2.set_transform(mtransforms.Affine2D().rotate(angle2).scale(1/lenMult).translate(_jpgear.CD/lenMult, 0) + window.canvas.axes.transData)

            case Type.internal:
                angle1 = startAngles[0] - updateAngle
                angle2 = startAngles[1] - (updateAngle*(G1.N/G2.N))

                curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1).scale(1/lenMult) + window.canvas.axes.transData)
                curveCol2.set_transform(mtransforms.Affine2D().rotate(angle2).scale(1/lenMult).translate(-_jpgear.CD/lenMult, 0) + window.canvas.axes.transData)

            case Type.planetary:
                angle1 = startAngles[0] - updateAngle
                angle2 = startAngles[1] + (updateAngle*(G1.N/G2.N))
                angle3 = startAngles[2] + (updateAngle*(G1.N/G3.N))

                curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1).scale(1/lenMult) + window.canvas.axes.transData)
                curveCol2.set_transform(mtransforms.Affine2D().rotate(angle2).scale(1/lenMult) + window.canvas.axes.transData)

                for n in range(NP):
                    revAngle = (n/NP)*tau
                    curveCol3List[n].set_transform(mtransforms.Affine2D().rotate(angle3).scale(1/lenMult).translate(_jpgear.CD/lenMult, 0).rotate(revAngle) + window.canvas.axes.transData)

    window.anim = manimation.FuncAnimation(window.canvas.fig, animFunc, fargs=[maxSpeed, slider, _jpgear.type], frames=framesPerRev, interval=interval)

    window.canvas.draw()

    window.show()

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
    if _gear.ID == 3:
        curveCol.set_edgecolor('g')

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
