import spacy
import PyPDF2
import fitz
from PyPDF2 import PdfFileReader
from data import raw_text

FILE_NAME = '16871flo.pdf'


def read_document_and_its_metadata():
    doc = fitz.open(FILE_NAME)
    print("number of pages: %i" % doc.pageCount)
    print(doc.metadata)
    return doc


def display_tokens(doc):
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


def read_pdf():
    pdf_file = open(FILE_NAME, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    print(page_content.encode('utf-8'))
    nlp = spacy.load("en_core_web_sm")
    for words in page_content:
        if words == '\n':
            words = ' '
        page_content = page_content + words
    print('not divide')
    text = page_content
    doc = nlp(text)
    display_tokens(doc)


def read_page_at_index(index: int):
    doc = read_document_and_its_metadata()
    page1 = doc.loadPage(index)
    page1text = page1.getText("text")
    print(page1text)
    nlp = spacy.load("en_core_web_sm")

    text = page1text
    doc = nlp(text)
    display_tokens(doc)


def read_pdf2_page1():
    read_page_at_index(0)


def read_pdf2_page2():
    read_page_at_index(1)


def read_pdf2_page3():
    read_page_at_index(2)


def read_pdf2_page4():
    read_page_at_index(3)


def read_raw_text_direct():
    print('NOT DIVIDE')
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(raw_text)
    display_tokens(doc)


def read_pdf3():
    with open(FILE_NAME, "rb") as filehandle:
        pdf = PdfFileReader(filehandle)
        page1 = pdf.getPage(0)
        textPage1 = page1.extractText()
        return textPage1


def divide_string(string_to_divide: str):
    """
        take the last 30% of a string
    """
    str_char_count = len(string_to_divide)
    char_index_to_split = int(0.7 * str_char_count)
    return string_to_divide[char_index_to_split:]

'''

def divide_data(str):
    """
        str -> array
    """
    df = pd.DataFrame(str.split('\n'))
    train, test = train_test_split(df, test_size=0.3)
    return [train, test]


def unify_data(dataset):
    """
        array -> str
    """
    one_string = ''
    data = dataset[0].astype(str, )
    for row in data:
        one_string += row + '\n'
    return one_string

'''


if __name__ == '__main__':

    read_pdf()

    read_pdf2_page1()
    read_pdf2_page2()
    read_pdf2_page3()
    read_pdf2_page4()

    test = read_pdf3()

    print('début')
    read_raw_text_direct()
