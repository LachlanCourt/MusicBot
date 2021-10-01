import json
class GlobalConfig():
    def __init__(self):
        self.OAuthToken = None

    # Parse all configs
    def parseAll(self, configFilePath):   
        self._parseConfig(configFilePath)

    # Parse main config
    def _parseConfig(self, filePath):
        try:
            f = open(filePath)
        except Exception as e:
            raise Exception(e)
        try:
            data = json.load(f)
            self.OAuthToken = data["OAuthToken"]
            f.close()
        except Exception as e:
            raise Exception(f"Error: Cannot parse {filePath}: " + str(e))

    def getRole(self, roleName, guild):
        for i in guild.roles:
            if i.name == roleName:
                return i
        return None
