# type: ignore
from __future__ import annotations
from typing import TypeVar, Generic, Type

configType = TypeVar('configType')

class ConfigRoot(Generic[configType], dict):
    """A given base for all configuration files for all file readers"""
    def __init__(self, configType: Type[configType], *args) -> None:
        super().__init__(*args)
        self._configType = configType
        self.schema : str = self["$schema"]
        """Path to the schema for this JSON file"""
        config = configType(self["config"])
        self.config: configType = config
        self["config"] = config
        """Actual configuration for this file handler"""
    def __repr__(self):
        return f"{self.__class__.__name__}({self._configType.__name__},\n{super(type(self), self).__repr__()})"

class DataHandlerConfig(dict):
    pass
