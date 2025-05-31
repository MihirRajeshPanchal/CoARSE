from pydantic import BaseModel
from typing import List
from coarse.models.sections import Section

class PaperObj(BaseModel):
    sections: List[Section]
