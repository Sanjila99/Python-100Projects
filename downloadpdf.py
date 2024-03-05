import requests
from bs4 import BeautifulSoup

#URL from which pdfs to be download
url="https://hamrocsit.com/"

#Requests URL and get response object
response=requests.get(url)

#Parse text obtaibed
soup=BeautifulSoup(response.text,'html.parser')

#Find all hyperlinks present on webpage
links=soup.find_all('a')

i=0

#from all links check for pdf link and if present  download file:
for link in links:
  if('.pdf' in link.get('href',[])):
        i+=1
        print("Downloading File:",i)

        #get response object for link
        response=requests.get(link.get('href'))

        #write content in pdf file
        pdf=open("pdf"+str(i)+".pdf",'wb')
        pdf.write(response.content)
        pdf.close()
        print("File",i,"downloaded")
print("All PDF files downloaded")

