from enum import Enum

class SignificanceLabel(str, Enum):
    MAJ = "Major Comment"
    MIN = "Minor Comment"
    GEN = "General Comment"