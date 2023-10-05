# TODO: Create static function for getting all subclasses via https://stackoverflow.com/questions/3862310/how-to-find-all-the-subclasses-of-a-class-given-its-name
from __future__ import annotations
import argparse
import ast
import json
from pprint import pprint

isMain = __name__ == '__main__'
# ---BASE CONVERTER DEFINITION---
class ValueConverter():
    """This class is for value conversions, usually for parsing strings"""
    registered:dict[str, ValueConverter.__class__] = {}
    hasCachedConverters = False
    name = "base"
    def __init__(self) -> None:
        self.config = {}
        pass
    
    def LoadConfig(self, config: dict) -> None:
        if config != None:
            self.config.update(config)

    def ConvertValue(self, val) -> None:
        raise NotImplementedError("Base cannot be used for conversion")

    @staticmethod
    def RegisterConverters():
        """Registers converters"""
        ValueConverter.hasCachedConverters = True
        all_subclasses = ValueConverter.__subclasses__()
        for subClass in all_subclasses:
            ValueConverter.registered[subClass.name] = subClass
        pass

    @staticmethod
    def ConvertValue(type: str, value, config: dict):
        """Convert the value with said config. Instances a new ValueConverter"""
        if not ValueConverter.hasCachedConverters:
            ValueConverter.RegisterConverters()
        try:
            converter:ValueConverter = ValueConverter.registered[type]()
        except BaseException:
            raise KeyError(f"Value Converter '{type}' is not registered")
        converter.LoadConfig(config)
        if isMain:
            pprint(converter.config)
        return converter.ConvertValue(value)
    
    @staticmethod
    def GetConverter(type:str)-> ConversionConfig:
        pass

class ConversionConfig(dict, ValueConverter):
    type: str
    """The type of converter to be used"""
    converter: ValueConverter
    config: dict | None
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.type = self["type"]
        self.converter = 0
        self.config = self.setdefault("config", None)
    def __repr__(self):
        return f"{self.__class__.__name__}(\n{super(type(self), self).__repr__()})"

# ---BUILTIN CONVERTERS---
class TimeConverter(ValueConverter):
    import datetime
    name = "time"
    methods:dict[str, function] = {
        "strptime": datetime.datetime.strptime,
        "fromiso": datetime.datetime.fromisoformat, 
        "parse" : lambda: None
    }
    def ConvertValue(self, val) -> None:
        func = self.methods[self.config["method"]]
        #TEMP: Tried https://stackoverflow.com/questions/24463202/typeerror-get-takes-no-keyword-arguments. Will fix later
        # return func(val, **self.config)
        return func(val, self.config["format"]).timestamp()
    def LoadConfig(self, config: dict) -> None:
        return super().LoadConfig(config)
    pass

class EnumConverter(ValueConverter):
    name = "enum"
    def __init__(self) -> None:
        super().__init__()
        self.config = {"keepOnKeyError": False}

    def ConvertValue(self, val) -> None:
        values: dict = self.config["values"]
        #Change to enum value
        if val in values:
            return values[val]
        #If value should be kept if it's not found
        if self.config["keepOnKeyError"]:
            return val
        #Default value if not found
        if "default" in self.config:
            return self.config["default"]
        raise KeyError(f"Value '{val}' not found for EnumConverter") 
    def LoadConfig(self, val: dict) -> None:
        super().LoadConfig(val)


class NumberConverter(ValueConverter):
    name = "number"
    def ConvertValue(self, val: str) -> None:
        if not val:
            return None
        return float(val)


class EnumTableConverter(ValueConverter):

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
    argumentsVars = vars(arguments)
    # Count how many arguments have a non-None value
    argCount = [v != None for v in vars(arguments).values()].count(True)
    onlyOneArg = argCount == 1
    
    pprint(ValueConverter.ConvertValue(**argumentsVars))