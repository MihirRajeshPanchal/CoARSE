from enum import Enum

class SectionLabel(str, Enum):
    ABS = "Abstract"
    INT = "Introduction"
    RWK = "Related Works"
    PDI = "Problem Definition/Idea"
    DAT = "Data/Datasets"
    MET = "Methodology"
    EXP = "Experiments"
    RES = "Results"
    TNF = "Tables & Figures"
    ANA = "Analysis"
    FWK = "Future Work"
    OAL = "Overall"
    BIB = "Bibliography"
    EXT = "External"
