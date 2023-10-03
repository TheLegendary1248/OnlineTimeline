# type: ignore
from __future__ import annotations
from typing import TypeVar, Generic, Type

configType = TypeVar('configType')

class ConfigRoot(Generic[configType], dict):
    """A given base for all configuration files for all file readers"""
    def __init__(self, configType: Type[configType], *args) -> None:
        super().__init__(*args)
        self.schema : str = self["$schema"]
        """Path to the schema for this JSON file"""
        self.config: configType = configType(self["config"])
        """Actual configuration for this file handler"""

class DataHandlerConfig():
    pass
