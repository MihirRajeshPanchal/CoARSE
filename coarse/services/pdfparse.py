from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import JsonOutputParser
from fastapi import UploadFile
import os
from coarse.constants.pdfparse import PDF_PARSER_PROMPT
from coarse.constants.coarse import llm
from coarse.models.sections import Section
from coarse.utils.pdfparse import extract_paper_content, save_to_file
from coarse.models.sections_map import SectionMap

async def extract_sections_from_paper(file: UploadFile):
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as temp_file:
        content = await file.read()
        temp_file.write(content)

    text = extract_paper_content(temp_file_path)
    save_to_file(temp_file_path + ".txt", text)
    
    chain = PDF_PARSER_PROMPT | llm | OutputFixingParser.from_llm(parser=JsonOutputParser(pydantic_object=SectionMap), llm=llm)
    
    result = chain.invoke({"text": text})
    
    print(result)
    os.remove(f"temp_{file.filename}")
    return result