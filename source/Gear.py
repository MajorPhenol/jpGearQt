class Gear:
    def __init__(self, _ID):
        self.ID = _ID

        self.N = -1                             # teeth

        self.x = 0				# profile shift
        self.tts = -1            		# standard tooth thickness
                                                # Note - this will get updated for any profile shift
        self.tt = -1    			# tooth thickness at effective pitch radius

        self.Rs = -1                            # standard pitch radius
        self.Rp = -1             		# pitch radius at OPA
        self.Rb = -1                            # base circle radius
        self.Pb = -1                     	# base pitch

        self.Ros = -1                    	# standard outer radius
        self.Ro = -1     			# actual outer radius
        self.Romax = -1     			# max outer radius, i.e. sharp
        self.Rtip = 0				# tip radius
        self.Rtip_max = 0 			# max possible tip radius
        self.Roe = 0    			# effective outer radius, considering tip radius

        self.Rr = -1                            # root radius
        self.Rf = 0				# root fillet radius
        self.Rff = 0				# root full fillet radius
        self.theta_F = 0			# angle between tooth centerline and root fillet center
        self.phi_JFI = 0			# profile angle at the junction of root fillet and involute, radians

        self.Rhp = 0				# highest point of single tooth contact

        self.undercut = False

        self.FW = 1				# face width
        self.E = 200000                         # Young's modulus
        self.nu = 0.3                           # Poisson's ratio
