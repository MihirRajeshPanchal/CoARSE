from enum import Enum
from typing import List
from pydantic import BaseModel
from coarse.models.sections import SectionLabel

class ErrorEntry(BaseModel):
    INC: str
    SEC: SectionLabel
    CRT: str

class Errors(BaseModel):
    TYP: List[ErrorEntry]
    GMR: List[ErrorEntry]