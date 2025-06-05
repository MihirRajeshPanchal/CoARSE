from typing import Dict, Any
from pydantic import RootModel, field_validator
from coarse.models.sections import SectionLabel


class SectionMap(RootModel[Dict[SectionLabel, str]]):

    @field_validator("root", mode="before")
    @classmethod
    def convert_keys(cls, value: Any):
        if not isinstance(value, dict):
            raise TypeError("Expected a dictionary")

        converted = {}
        for k, v in value.items():
            try:
                converted[SectionLabel[k]] = v  # Convert "ABS" → SectionLabel.ABS
            except KeyError:
                raise ValueError(f"Invalid key '{k}'. Must be one of: {list(SectionLabel.__members__.keys())}")
        return converted
