from __future__ import annotations
from typing import TypeVar, Generic, Type

configType = TypeVar('configType')

class ConfigRoot(Generic[configType]):
    """A given base for all configuration files for all file readers"""
    def __init__(self, config: dict, configType: Type[configType]) -> None:
        self.schema : str = config["$schema"]
        """Path to the schema for this JSON file"""
        self.config: configType = configType(config["config"])
        """Actual configuration for this file handler"""

class DataHandlerConfig():
    pass