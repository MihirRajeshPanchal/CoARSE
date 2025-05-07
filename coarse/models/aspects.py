from enum import Enum

class EvaluationLabel(str, Enum):
    APR = "Appropriateness"
    NOV = "Originality or Novelty"
    IMP = "Significance or Impact"
    CMP = "Meaningful Comparison"
    PNF = "Presentation & Formatting"
    REC = "Recommendation"
    EMP = "Empirical & Theoretical Soundness"
    SUB = "Substance"
    CLA = "Clarity"
