from unstructured.partition.auto import partition


def extract_paper_content(file_path):
    elements = partition(file_path)
    paper_content = "\n\n".join([str(el) for el in elements])
    return paper_content

def save_to_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)