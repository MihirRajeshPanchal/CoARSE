from pydantic import BaseModel, RootModel, field_validator
from coarse.models.sections import SectionLabel
from coarse.models.purpose import PurposeLabel
from typing import Optional, List, Any
from coarse.models.sentiments import Sentiment

class SectionAnnotation(BaseModel):
    SEC: SectionLabel
    PRT: str
    PUR: PurposeLabel
    APR: Optional[Sentiment] = None
    NOV: Optional[Sentiment] = None
    IMP: Optional[Sentiment] = None
    CMP: Optional[Sentiment] = None
    PNF: Optional[Sentiment] = None
    REC: Optional[Sentiment] = None
    EMP: Optional[Sentiment] = None
    SUB: Optional[Sentiment] = None
    CLA: Optional[Sentiment] = None

class AspectPurposeOutput(RootModel[List[SectionAnnotation]]):
    pass