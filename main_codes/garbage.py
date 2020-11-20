file_doc = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110\APCATA_17035.docx'
import docx
def test(file_doc):
    doc = docx.Document(file_doc)
    paragraph = doc.paragraphs
    for i in range(len(paragraph)):
        print(i)
    # print(paragraph)
    
print(test(file_doc))