class Units:
    def __init__(self, _modName, _modMult, _lenName, _lenMult, _lenFormat, _torqueName, _torqueMult, _pressureName, _pressureMult, _velName, _velMult):
        self.modName = _modName
        self.modMult = _modMult # "M" for metric, "T" for TPI
        self.lenName = _lenName
        self.lenMult = _lenMult
        self.lenFormat = _lenFormat
        self.torqueName = _torqueName
        self.torqueMult = _torqueMult
        self.pressureName = _pressureName
        self.pressureMult = _pressureMult
        self.velName = _velName
        self.velMult = _velMult

unitsMM_NMM = Units("mm", "M", "mm", 1.0, "{:.3f}", "Nmm", 1.0, "MPa", 1.0, "m/s", 1.0) # everything is calculate based on these values
unitsMM_NM =  Units("mm", "M", "mm", 1.0, "{:.3f}", "Nm", 1000, "MPa", 1.0, "m/s", 1.0)
unitsIN_OZ =  Units("TPI", "T", "in", 25.4, "{:.4f}", "in-oz", 7.061552, "ksi", 6.894757, "ft/s", 0.3048)
unitsIN_LBS = Units("TPI", "T", "in", 25.4, "{:.4f}", "in-lbs", 112.98483333, "ksi", 6.894757, "ft/s", 0.3048)
unitsFT_LBS = Units("TPI", "T", "in", 25.4, "{:.4f}", "ft-lbs", 1355.818, "ksi", 6.894757, "ft/s", 0.3048)

unitsList = [unitsMM_NMM, unitsMM_NM, unitsIN_OZ, unitsIN_LBS, unitsFT_LBS]
