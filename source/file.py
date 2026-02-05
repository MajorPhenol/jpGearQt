from PySide6.QtWidgets import QFileDialog, QMessageBox

from helper import Type, errorBox, showMessage
from draw import layoutGear

import json

def openJSON(_jpgear):
    loadPath, selectedFilter = QFileDialog.getOpenFileName(None, 'Load Design')

    if loadPath == '':
        return

    _jpgear.savePath = loadPath
    _jpgear.setWindowTitle(loadPath)

    try:
        loadJSON(_jpgear, loadPath)
    except Exception as e:
        errorBox(e, "Could not open file")

def loadJSON(_jpgear, _filePath):
    with open(_filePath, 'r', encoding='utf-8') as f:
        dictFull = json.load(f)

    dictG1 = dictFull.get("Gear1")
    dictG2 = dictFull.get("Gear2")
    dictG3 = dictFull.get("Gear3")
    dictM = dictFull.get("Mesh")

    # start with a clean slate
    _jpgear.ui.tabW_main.setCurrentIndex(1)
    _jpgear.G1.reset()
    _jpgear.G2.reset()
    _jpgear.G3.reset()
    _jpgear.setType(dictM["type"])
    _jpgear.ui.cb_input_GD.setCurrentIndex(dictM["planet_input"])
    _jpgear.ui.cb_output_GD.setCurrentIndex(dictM["planet_output"])

    # set mesh parameters
    _jpgear.setUnits(int(dictM["units"]))
    actionsList = _jpgear.groupUnits.actions()
    actionsList[int(dictM["units"])].setChecked(True)

    _jpgear.mod = dictM["mod"]
    _jpgear.PA_deg = dictM["PA_deg"]

    if dictM["set_CD_bkl"] == 0:
        # use backlash
        _jpgear.ui.cb_CD_bkl.setCurrentIndex(0)
    else:
        # use center distance
        _jpgear.ui.cb_CD_bkl.setCurrentIndex(1)

    _jpgear.bkl1 = dictM["bkl1"] * _jpgear.units.lenMult
    _jpgear.bkl2 = dictM["bkl2"] * _jpgear.units.lenMult
    _jpgear.CD = dictM["CD"] * _jpgear.units.lenMult

    # set gear parameters
    for gear, dict in zip([_jpgear.G1, _jpgear.G2, _jpgear.G3], [dictG1, dictG2, dictG3]):
        gear.N = dict["N"]
        gear.x = dict["x"]
        gear.Ro = dict["Ro"] * _jpgear.units.lenMult
        gear.Rtip = dict["Rtip"] * _jpgear.units.lenMult
        gear.Rr = dict["Rr"] * _jpgear.units.lenMult
        gear.Rf = dict["Rf"] * _jpgear.units.lenMult
        gear.Rrim = dict["Rrim"] * _jpgear.units.lenMult
        gear.FW = dict["FW"] * _jpgear.units.lenMult
        gear.E = dict["E"] * _jpgear.units.pressureMult
        gear.nu = dict["nu"]

    _jpgear.rtcl1 = dictM["rtcl1"] * _jpgear.units.lenMult
    _jpgear.rtcl2 = dictM["rtcl2"] * _jpgear.units.lenMult
    _jpgear.rtcl3 = dictM["rtcl3"] * _jpgear.units.lenMult

    _jpgear.NPlanets = dictM["planets"]
    _jpgear.RPM = dictM["speed"]
    _jpgear.torque = dictM["torque"] * _jpgear.units.torqueMult

    _jpgear.initGearDesignFields()
    _jpgear.updateGears()

def saveAsJSON(_jpgear):
    if _jpgear.savePath == '':
        defaultName = 'gear_design.json'
    else:
        defaultName = _jpgear.savePath

    savePath, selectedFilter = QFileDialog.getSaveFileName(None, 'Save Design', defaultName)

    if savePath != '':
        _jpgear.savePath = savePath
        _jpgear.setWindowTitle(savePath)
        saveJSON(_jpgear)

def saveJSON(_jpgear):
    if _jpgear.savePath == '':
        saveAsJSON(_jpgear)
    else:
        dictFull = {}
        gearList = [_jpgear.G1, _jpgear.G2, _jpgear.G3]
        for gear in gearList:
            dictFull.update({"Gear" + str(gear.ID) : createJSONGear(gear, _jpgear.units)})

        dictFull.update({"Mesh" : createJSONMesh(_jpgear)})

        with open(_jpgear.savePath, 'w', encoding='utf-8') as f:
            json.dump(dictFull, f, ensure_ascii=False, indent=4)

        text = 'File saved: ' + str(_jpgear.savePath) + '\n'
        showMessage(_jpgear, _text=text)

def createJSONGear(_gear, _units):
    return {
        "N" : _gear.N,
        "x" : _gear.x,
        "Ro" : _gear.Ro / _units.lenMult,
        "Rtip" : _gear.Rtip / _units.lenMult,
        "Rr" : _gear.Rr / _units.lenMult,
        "Rf" : _gear.Rf / _units.lenMult,
        "Rrim" : _gear.Rrim / _units.lenMult,
        "FW" : _gear.FW / _units.lenMult,
        "E" : _gear.E / _units.pressureMult,
        "nu" : _gear.nu,
    }

def createJSONMesh(_jpgear):
    return {
        "type" : _jpgear.type,
        "planet_input" : _jpgear.ui.cb_input_GD.currentIndex(),
        "planet_output" : _jpgear.ui.cb_output_GD.currentIndex(),
        "units": _jpgear.unitsList.index(_jpgear.units),
        "mod" : _jpgear.mod,
        "PA_deg" : _jpgear.PA_deg,
        "set_CD_bkl" : _jpgear.ui.cb_CD_bkl.currentIndex(),
        "bkl1" : _jpgear.bkl1 / _jpgear.units.lenMult,
        "bkl2" : _jpgear.bkl2 / _jpgear.units.lenMult,
        "CD" : _jpgear.CD / _jpgear.units.lenMult,
        "rtcl1" : _jpgear.rtcl1 / _jpgear.units.lenMult,
        "rtcl2" : _jpgear.rtcl2 / _jpgear.units.lenMult,
        "rtcl3" : _jpgear.rtcl3 / _jpgear.units.lenMult,
        "planets" : _jpgear.NPlanets,
        "speed" : _jpgear.RPM,
        "torque" : _jpgear.torque / _jpgear.units.torqueMult
    }

def exportDXF(_jpgear):
    for gear in _jpgear.gearList:
        if gear.Rb < 0 :
            messageBox = QMessageBox.critical(None, "Error exporting", "Could not export geometry for gear "+str(gear.ID))
        else:
            layoutGear(_jpgear, gear, save=True)
