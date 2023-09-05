class ValueConverter():
    """Base class for converters for individual values"""
    def __init__(self) -> None:
        self.config: dict = None
        pass
    def LoadConfig(self) -> None:
        pass
    def ConvertValue(self, val) -> None:
        pass

class TimeConverter(ValueConverter):
    def ConvertValue(self, val) -> None:
        return
        # return super().ConvertValue(val)
    pass

class EnumConverter(ValueConverter):
    def ConvertValue(self, val) -> None:
        values: dict = None
        return values["val"]
        # return super().ConvertValue(val)
    pass