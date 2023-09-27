import json
import argparse
from pprint import pprint
from io import TextIOWrapper
from OnlineTimeline.OTPlugin.Config import ConfigRoot
from OnlineTimeline.globals import CONFIG
from typing import TypeVar, Generic, Type
from pathlib import Path
from datetime import datetime
import pickle
from OnlineTimeline.Utils import EnsurePath
inputType = TypeVar('inputType')
outputType = TypeVar('outputType')


class DataHandlerBase(Generic[inputType, outputType]):
    """Base class for all data handlers"""
    def __init__(self, config: dict=None) -> None:
        self.config = dict()
        if config != None:
            self.LoadConfig(config)
        pass
    def UseCmdArguments(self) -> None:
        """Use command arguments, usually for testing the handler separate of the program"""
        #Setup cmd line parsing
        parser = argparse.ArgumentParser(description=__doc__)

        
        #Input file
        parser.add_argument('-file', type=open,help="The path to the input file")
        #Input config (if not the default dialect)
        parser.add_argument('-config', type=open,help="The path to the input config file")
        #Output file
        parser.add_argument('-output', type=Path, help="The output file")

        namespace = DataHandlerArgs()
        #If send to timeline
        arguments = parser.parse_args(namespace=namespace)
        # Count how many arguments have a non-None value
        argCount = [v != None for v in vars(arguments).values()].count(True)
        onlyOneArg = argCount == 1
        #Create handler instance
        if arguments.config != None:
            self.LoadConfig(arguments.config)
            if onlyOneArg: 
                pprint(self.config)
                return

        if arguments.file != None:
            data = self.ProcessData(arguments.file)
            pprint(data)
            if arguments.output != None:
                raise NotImplementedError("Code is missing")
                arguments.output.open('w')
            else:
                # Default output function
                now = datetime.now()
                hashname = f"{self.__class__.__name__}.{now.date()}.pickle"
                path = Path(CONFIG["OnlineTimelineCore"]["TempLocation"])/hashname
                print("Output will be written to temp location at " + str(path))
                EnsurePath(path)
                with open(path, "wb") as file:
                    pickle.dump(data, file)
                    file.close()

    def ProcessData(self, data: inputType) -> outputType:
        """Process the data given"""
        pass

    def LoadConfig(self, config: dict) -> None:
        """Loads the configuration for this handler"""
        #Ensure type here
        self.config = json.load(config)
        """Configuration of this file handler as a dictionary"""
        pass

class DataHandlerArgs(argparse.Namespace):
    config: TextIOWrapper
    file: TextIOWrapper
    output: Path

def _SaveToTemp():
    pass
    
