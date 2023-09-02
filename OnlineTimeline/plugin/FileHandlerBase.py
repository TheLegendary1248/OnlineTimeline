import json

class FileHandlerBase:
    """Base class for all file type handlers that """
    def __init__(self, config: dict=None) -> None:
        if config != None:
            self.LoadConfig(config)
        pass
    def HandleFile() -> dict:
        """Parses content of the file into"""
        pass
    def LoadConfig(self, config: dict) -> None:
        """Loads the configuration for this handler"""
        #Ensure type here
        self.config = json.load(config)
        pass