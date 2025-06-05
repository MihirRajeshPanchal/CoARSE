from enum import Enum
from typing import List, Union
from pydantic import BaseModel, validator
from coarse.models.sections import SectionLabel

# Mapping short codes to full SectionLabel enum names
SHORT_CODE_MAP = {
    "ABS": "Abstract",
    "INT": "Introduction",
    "RWK": "Related Works",
    "PDI": "Problem Definition/Idea",
    "DAT": "Data/Datasets",
    "MET": "Methodology",
    "EXP": "Experiments",
    "RES": "Results",
    "TBF": "Tables & Figures",
    "ANA": "Analysis",
    "FWR": "Future Work",
    "OVR": "Overall",
    "BIB": "Bibliography",
    "EXT": "External"
}

class ErrorEntry(BaseModel):
    SEC: SectionLabel
    INC: str
    CRT: str

    # Validator for SEC field: convert short code to full enum value
    @validator("SEC", pre=True)
    def convert_short_code_to_enum(cls, v):
        if isinstance(v, str):
            # If input is short code, map to full string
            full_label = SHORT_CODE_MAP.get(v, v)
            return full_label
        return v

class Errors(BaseModel):
    TYP: List[ErrorEntry]
    GMR: List[ErrorEntry]
