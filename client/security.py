import os, json, re, subprocess

# A class to save the user's PC information.
class PCIdentifiers():
    def __init__(self, hwid, cpuID, biosID):
        self.hwid = hwid
        self.cpuID = cpuID
        self.biosID = biosID

# A class to register the user's ID to a remote database.
class RegisterUser():
    def __init__(self):
        url=None

# A class to get all of the user's PC identifiers.
class Secure():
    def __init__(self):
        # All of the user's PC's identifiers stored in variables for readability.
        hwid = Secure.GetHWID(self)
        cpuID = Secure.getCPUID(self)
        biosID = Secure.getBIOSID(self)
        
        # Saves the user's security identifiers in an object for easy accessibility.
        securityIdentifiers = PCIdentifiers(hwid, cpuID, biosID)


    #Gets user's HWID and returns it.
    def GetHWID(self):
        try:
            systemhwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
            return systemhwid
        except Exception as e:
            return str("Failed to get HWID")

    
    #Gets user's CPU ID and returns it.
    def getCPUID(self):
        try:
            cpuID = str(subprocess.check_output('wmic cpu get ProcessorId')).split('\\r\\n')[1].strip('\\r').strip()
            return cpuID
        except Exception as e:
            return str("Failed to get CPU ID")

    
    #Gets user's BIOS Serial Number and returns it.
    def getBIOSID(self):
        try:
            biosID = str(subprocess.check_output('wmic bios get serialnumber')).split('\\r\\n')[1].strip('\\r').strip()
            return biosID
        except Exception as e:
            return str("Failed to get BIOS ID")


    
    
Secure()