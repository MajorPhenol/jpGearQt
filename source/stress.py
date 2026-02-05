import draw
from helper import tau, Type, invF, setText

from numpy import pi, sin, cos, tan, arccos, arctan
from numpy import sqrt, real

from scipy.optimize import least_squares

def calcPitchLineVelocity(_jpgear):
    velocity = (tau * _jpgear.G1.Rp * (_jpgear.RPM / 60)) / 1000
    setText(_jpgear.ui.lb_pitchLineVel, velocity, _jpgear.units.velMult)

def calcContactStress(_G1, _G2, _OPA, _w):
    Cp = 1/sqrt( (pi*(1-_G1.nu**2)/_G1.E) + (pi*(1-_G2.nu**2)/_G2.E) )

    # max contact stress occurs at lowest point of single tooth contact
    rho1 = sqrt(_G1.Roe**2 - _G1.Rb**2) - _G1.Pb       # AGMA C2
    rho2 = _G1.Rb * _G2.Rb * tan(_OPA) - rho1  # AGMA C6 - C2

    stress = Cp * sqrt(_w * ( (rho1+rho2)/(rho1*rho2) ))
    return stress

def calcBendingStress(_jpgear, _gear, _force, _lewisParams, _mesh):
    if _mesh == 1:
        OPA = _jpgear.OPA1_deg
        CR = _jpgear.CR1
    elif _mesh ==2:
        OPA = _jpgear.OPA2_deg
        CR = _jpgear.CR2

    # Constants for stress concentration factor Kf
    # from GOIG 11.24 - 11.26
    # Note that GOIG uses degrees while AGMA 908 uses radians
    k1 = 0.3054 - 0.00489*OPA - 0.000069*OPA**2
    k2 = 0.3620 - 0.01268*OPA + 0.000104*OPA**2
    k3 = 0.2934 + 0.00609*OPA + 0.000087*OPA**2

    # Lewis parabola key points
    if _gear.type == "external":
        R = _gear.Rf
    elif _gear.type == "internal":
        R = _gear.Rtip

    Rc, gamma, x_Lewis, y_Lewis, a_Lewis = _lewisParams

    # Lewis parabola dimensions
    tt_LP = 2*x_Lewis           # tooth thickness at critical section
    h_LP = abs(Rc - y_Lewis)    # height of Lewis parabola

    # please don't divide by zero
    if R < 0.001:
        R = 0.001

    # Stress concentration factor from GOIG 11.23
    Kf = k1 + ( (tt_LP/R)**k2 ) * ( (tt_LP/h_LP)**k3 )

    # GOIG 11.28, reworked
    # Note that I factored out the 'm' and split the equation into
    # pieces to make it more legible

    # bending stress = Mx/I, where:
    #   M: moment, f_tan * height
    #   I: second moment of inertia for rectangluar beam, bt^3/12, where:
    #       b: depth, or face width
    #       t: thickness
    #       substitute t = 2*x_lewis:
    #       => I = FW*x_lewis^3/1.5
    f_tan = _force * cos(gamma)
    M_tan = f_tan * h_LP
    I_bend = (_gear.FW * x_Lewis**3) / 1.5
    stressB = M_tan*x_Lewis/I_bend
    # radial stress = f_rad / area
    f_rad = _force * sin(gamma)
    stressR = f_rad/(tt_LP*_gear.FW)
    # total stress is bending stress minus radial stress
    stress = Kf*(stressB - stressR)

    # TODO: calculate this properly
    if CR >= 2:
        stress = stress * 0.65

    return stress

def lewisParabolaExternal(_jpgear, _gear):
    """
    Find the intersection point of the Lewis parabola and the root fillet circle

    Parameters:
    Fx, Fy - centerpoint of root fillet circle
    Rf - root fillet radius
    Rc - intersection of tooth centerline and force vector; the apex of the Lewis
      parabola

    Output variables:
    x, y - point of intersection between the Lewis parabola and the root fillet
    a - scale of parabola, => y = ax^2 + bx + c
    -------------------------------------------------------------------------------

    Equation of a circle: (y-v)^2 + (x-h)^2 = r^2
    Substitute values for fillet circle: (y-Fy)^2 + (x-Fx)^2 = Rf^2
    Rearrange: y = +/-sqrt(Rf^2 - (x-Fx)^2) + Fy
    We are only interested in the bottom half of the circle:
    [1] y = -sqrt(Rf^2 - (x-Fx)^2) + Fy
    Implicit differentiation of [1]:
    [2] dy/dx = -(x-Fx)/(y-Fy)

    Equation of a parabola: y = ax^2 + bx + c
    Substitute values of Lewis parabola, and note that the parabola is
    centered on the y-axis, i.e. b=0:
    [3] y = ax^2 + Rc
    Differentiate [3]:
    [4] dy/dx = 2ax

    At the tangent intersection of the parabola and circle, the derivatives
    are equal:
    [5] -(x-Fx)/(y-Fy) = 2ax
    Rearrange [5]:
    [6] a = -(x-Fx)/(2x)(y-Fy)
    Substitute [6] into [3]:
    y = -(x)(x-Fx)/(2)(y-Fy) + Rc
    y^2 - Fy*y - Rc*y = (-x^2 + Fx*x)/2 - Rc*Fy
    Complete the square:
    [y^2 -(Fy+Rc)*y + (Fy+Rc)^2/4] - (Fy+Rc)^2/4 = (-x^2 + Fx*x)/2 - Rc*Fy
    [y - (Fy+Rc)/2]^2  = (-x^2 + Fx*x)/2 - Rc*Fy + (Fy+Rc)^2/4
    y - (Fy+Rc)/2 = +/-sqrt[(-x^2 + Fx*x)/2 - Rc*Fy + (Fy+Rc)^2/4]
    [7] y = +/-sqrt[(-x^2 + Fx*x)/2 - Rc*Fy + (Fy+Rc)^2/4] + (Fy+Rc)/2
    We are only interested in the bottom half of the circle:
    [8] y = -sqrt[(-x^2 + Fx*x)/2 - Rc*Fy + (Fy+Rc)^2/4] + (Fy+Rc)/2
    Eq [8] must intersect Eq [1]:
    -sqrt[(-x^2 + Fx*x)/2 - Rc*Fy + (Fy+Rc)^2/4] + (Fy+Rc)/2 = -sqrt(Rf^2 - (x-Fx)^2) + Fy
    Rearrange to find the zero:
    [9] -sqrt[(-x^2 + Fx*x)/2 - Rc*Fy + (Fy+Rc)^2/4] + (Fy+Rc)/2 +
      sqrt(Rf^2 - (x-Fx)^2) - Fy = 0
    """

    # Highest point of single tooth contact
    phi_hp = arccos(_gear.Rb/_gear.Rhp)
    theta_hp = (_gear.tts/(2*_gear.Rs)) + invF(_jpgear.PA) - invF(phi_hp)
    # Rhp_x = _gear.Rhp*sin(theta_hp)
    # Rhp_y = _gear.Rhp*cos(theta_hp)

    # angle between force normal direction and
    # perpendicular to tooth centerline
    gamma = phi_hp - theta_hp

    # apex of Lewis parabola
    Rc = _gear.Rb / cos(gamma)
    # alternately, Rc = Rhp_y - Rhp_x*tan(gamma) (GOIG 11.22)

    # find center of fillet circle
    Fx = (_gear.Rr + _gear.Rf)*sin(_gear.theta_F)
    Fy = (_gear.Rr + _gear.Rf)*cos(_gear.theta_F)

    if _gear.Rf == 0:
        x = Fx
        y = Fy
        a = (y-Rc)/(x**2)
    else:
        # Eq [9] above
        def func(x):
            return real(-sqrt( (-(x**2) + Fx*x)/2 - Rc*Fy + ((Fy+Rc)**2)/4) + (Fy+Rc)/2 +
                    sqrt(_gear.Rf**2 - (x-Fx)**2) - Fy)

        # starting point is between the JFI and fillet center
        initialGuess = Fx - _gear.Rf/2

        sol = least_squares(func, x0=initialGuess)
        x = sol.x.item()
        y = -sqrt(_gear.Rf**2 - (x-Fx)**2) + Fy 	# Eq [1] above
        a = (y-Rc)/(x**2)                               # Eq [3] above

    return [Rc, gamma, x, y, a]

def lewisParabolaInternal(_jpgear, _gear):
    """
    Find the intersection point of the Lewis parabola and the tooth involute

    Math is taken from NASA technical memo 107012:
        "Bending Strength Model for Internal Spur Gear Teeth"

    Parameters:
    d - angle between the internal tooth centerline and the start of the involute
        at the base circle (called 'delta' in the NASA paper)
    Rc - intersection of tooth centerline and force vector; the apex of the Lewis
        parabola
    theta - roll angle to the point where the Lewis parabola is tangent to the involute

    Output variables:
    x, y - point of intersection between the Lewis parabola and the involute
    a - scale of parabola, => y = ax^2 + bx + c
    -------------------------------------------------------------------------------

    """
    # profile angle at highest point of single tooth contact
    phi_hp = arccos(_gear.Rb/_gear.Rhp)
    # delta angle
    d = ((_gear.Ps-_gear.tts)/(2*_gear.Rs)) - invF(_jpgear.PA)
    # angle between force normal direction and
    # perpendicular to tooth centerline
    gamma = phi_hp + invF(phi_hp) + d
    # apex of Lewis parabola
    Rc = _gear.Rb / cos(tan(phi_hp) + d)

    def funcInv(theta):
        # Eq (9) in the NASA paper
        x = _gear.Rb*sin(theta+d) - _gear.Rb*theta*cos(theta+d)
        # Eq (10) in the NASA paper
        y = _gear.Rb*cos(theta+d) + _gear.Rb*theta*sin(theta+d)

        # Eq (11) and Eq (12) in the NASA paper must be equal,
        # i.e. H1 - H2 = 0
        return (x/tan(theta+d)) - 2*(y-Rc)

    # Eq (8) in the NASA paper
    initial_guess = 1.5*tan(phi_hp)

    sol = least_squares(funcInv, x0=initial_guess)
    theta = sol.x.item()

    # check if the Lewis parabola hits the involute

    # profile angle at intersection point
    phi_E = theta - d
    Re = _gear.Rb/cos(phi_E)

    if Re <= _gear.Roe: # parabola hits involute
        # intersection point
        x = _gear.Rb*sin(theta+d) - _gear.Rb*theta*cos(theta+d)
        y = _gear.Rb*cos(theta+d) + _gear.Rb*theta*sin(theta+d)
        # y = ax^2 + bx + c
        a = (y-Rc)/(x**2)
    else: # parabola hits tip radius
        # find center of fillet circle
        # distance from gear center to center of tip fillet
        Rcf = _gear.Ro - _gear.Rtip
        # tangent distance from base circle to center to tip fillet
        EF = sqrt(Rcf**2 - _gear.Rb**2)
        # profile angle at center of tip fillet
        phi_F = arccos(_gear.Rb/Rcf)

        # tangent distance from base circle to intersection of fillet and involute
        EA = EF + _gear.Rtip
        # distance from gear center to to intersection of fillet and involute
        Ra = sqrt(EA**2 + _gear.Rb**2)
        # profile angle at intersection of fillet and involute
        phi_A = arccos(_gear.Rb/Ra)
        # angle between center of internal tooth and center of tip fillet
        theta_F = d + invF(phi_A) + phi_A - phi_F

        Fx = Rcf*sin(theta_F)
        Fy = Rcf*cos(theta_F)

        if _gear.Rtip == 0:
            x = Fx
            y = Fy
            a = (y-Rc)/(x**2)
        else:
            # Eq [9] above
            # [9] sqrt[(x^2 - Fx*x)/2 - Rc*Fy + (Fy+Rc)^2/4] + (Fy+Rc)/2 -
            #   sqrt(Rf^2 - (x-Fx)^2) - Fy = 0
            def funcF(x):
                return real(sqrt( (-(x**2) + Fx*x)/2 - Rc*Fy + ((Fy+Rc)**2)/4) + (Fy+Rc)/2 -
                        sqrt(_gear.Rtip**2 - (x-Fx)**2) - Fy)

            # starting point is between the JFI and fillet center
            # initialGuess = Fx - _gear.Rtip
            # initialGuess = Ra * sin(d + invF(phi_A))
            initialGuess = Ra * sin(theta_F)

            sol = least_squares(funcF, x0=initialGuess)
            x = sol.x.item()
            y = sqrt(_gear.Rtip**2 - (x-Fx)**2) + Fy 	# Eq [1] above
            a = (y-Rc)/(x**2)                           # Eq [3] above

    return [Rc, gamma, x, y, a]


