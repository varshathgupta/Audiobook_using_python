import pyttsx3  #python library for text to speech
import PyPDF2   #python file for reading pdf file
book=open('python.pdf','rb') #rb denotes read in binary formats. "pthon.pdf" is pdf document that going to be read
pdfReader = PyPDF2.PdfFileReader(book)
pages =  pdfReader.numPages
print(pages) #Prints the total number of pages in pdf
speaker = pyttsx3.init()
for num in range(1,pages): #Inorder to read full book the for loop is  used. If you need particular page remove for loop
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
