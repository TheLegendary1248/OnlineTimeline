# TODO: Create static function for getting all subclasses via https://stackoverflow.com/questions/3862310/how-to-find-all-the-subclasses-of-a-class-given-its-name
from __future__ import annotations
import argparse
import ast
import json
from pprint import pprint

class ValueConverter():
    """This class is for value conversions, usually for parsing strings"""
    registered:dict = {}
    hasCachedConverters = False
    name = "base"
    def __init__(self) -> None:
        pass
    
    def LoadConfig(self) -> None:
        pass

    def ConvertValue(self, val) -> None:
        raise NotImplementedError("Base cannot be used for conversion")

    @staticmethod
    def RegisterConverters(name: str, c: ValueConverter):
        """Registers converters"""
        ValueConverter.registered[name] = c
        pass

    @staticmethod
    def ConvertValue(name: str, val, config: dict):
        """Convert the value with said config"""
        all_subclasses = ValueConverter.__subclasses__()
        converter = ValueConverter.registered[str]
        pass

class TimeConverter(ValueConverter):
    def ConvertValue(self, val) -> None:
        
        return
    def LoadConfig(self, val: dict) -> None:
        return super().LoadConfig()
        # return super().ConvertValue(val)
    pass

class EnumConverter(ValueConverter):
    def ConvertValue(self, val) -> None:
        values: dict = None
        return values["val"]
        # return super().ConvertValue(val)
    pass

class ValueConverterArgs(argparse.Namespace):
    value: any
    config: dict
    type: str

if __name__ == '__main__':
    #Setup cmd line parsing
    parser = argparse.ArgumentParser(description=__doc__)
    #Input value
    parser.add_argument('-value', type=ast.literal_eval, required=True, help="The path to the input file")
    #Input config 
    parser.add_argument('-config', type=json.loads, required=True, help="Config for this converter")
    #Input type
    parser.add_argument('-type', type=str, required=True, help="Type of converter")

    namespace = ValueConverterArgs()
    #If send to timeline
    arguments = parser.parse_args(namespace=namespace)

    
    # Count how many arguments have a non-None value
    argCount = [v != None for v in vars(arguments).values()].count(True)
    onlyOneArg = argCount == 1
    
    pprint(arguments)