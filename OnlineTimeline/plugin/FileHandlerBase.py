import json
import argparse
class FileHandlerBase:
    """Base class for all file type handlers that """
    def __init__(self, config: dict=None) -> None:
        if config != None:
            self.LoadConfig(config)
        pass
    def UseCmdArguments(self) -> None:
        """Use command arguments, usually for testing the handler separate of the program"""
        #Setup cmd line parsing
        parser = argparse.ArgumentParser(description=__doc__)
        #Input file
        parser.add_argument('file', type=open,help="The path to the input file")
        #Input config (if not the default dialect)
        parser.add_argument('-config', type=open,help="The path to the input config file")
        #Output file
        parser.add_argument('-output', help="The output file")
        #Output limit
        parser.add_argument('-limit',type=int)
        #If send to timeline
        arguments = parser.parse_args()
        #Create handler instance
        if arguments.config != None:
            self.LoadConfig(arguments.config)
        #Run logic
        self.CreateEvents(arguments.file)
        pass
    def HandleFile() -> dict:
        """Parses content of the file into"""
        pass
    def LoadConfig(self, config: dict) -> None:
        """Loads the configuration for this handler"""
        #Ensure type here
        self.config = json.load(config)
        pass