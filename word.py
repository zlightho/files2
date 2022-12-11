from docx import Document


def str_docx_replace(path, str1, str2):
    # открываем документ:
    document = Document(path)
    for p in document.paragraphs:
        if str1 in p.text:
            p.text = p.text.replace(str1, str2)

    document.save(path)


str_docx_replace(
    "doc_file.docx",
    "TestTESTtest.",
    "TESTTESTTESTTESTTESTTESTTEST.",
)
