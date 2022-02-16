import pyttsx3
import PyPDF2

book = open("BUHARI_speech.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(1, pages + 1):
    page_Obj = pdfReader.getPage(1)
    text = page_Obj.extractText()
    print(text)
    speaker.say(text)
    speaker.runAndWait()

