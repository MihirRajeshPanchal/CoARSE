from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import JsonOutputParser
from coarse.constants.aspect_purpose import ASPECT_PURPOSE_PROMPT
from coarse.constants.coarse import llm
from coarse.models.sections import SectionLabel
from coarse.models.purpose import PurposeLabel
from coarse.models.sentiments import Sentiment
from coarse.models.aspect_purpose import SectionAnnotation, AspectPurposeOutput
import pprint

def enum_value(enum_cls, value):
    try:
        return enum_cls[value].value  # Convert "ABS" -> SectionLabel["ABS"].value -> "Abstract"
    except KeyError:
        return value  # fallback if already a full value

async def aspect_purpose(paper_obj):
    chain = ASPECT_PURPOSE_PROMPT | llm | OutputFixingParser.from_llm(
        parser=JsonOutputParser(pydantic_object=AspectPurposeOutput),
        llm=llm
    )

    raw_result = chain.invoke({"paper_obj": {k.name: v for k, v in paper_obj.root.items()}})

    for i in range(len(raw_result)):
        raw = raw_result[i]
        mapped = {
            "SEC": enum_value(SectionLabel, raw.get("SEC")),
            "PRT": raw.get("PRT"),
            "PUR": enum_value(PurposeLabel, raw.get("PUR")),
        }

        # Map each aspect if present
        for aspect in ["APR", "NOV", "IMP", "CMP", "PNF", "REC", "EMP", "SUB", "CLA"]:
            if aspect in raw:
                mapped[aspect] = enum_value(Sentiment, raw[aspect])

        raw_result[i] = SectionAnnotation(**mapped)

    pprint.pprint(raw_result)

    return AspectPurposeOutput(root=raw_result)
