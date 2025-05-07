from enum import Enum

class PurposeLabel(str, Enum):
    SMY = "Summary"
    SUG = "Suggestion"
    DFT = "Deficit"
    APC = "Appreciation"
    DIS = "Discussion"
    QSN = "Question"
    CRT = "Criticism"
    FBK = "Feedback"