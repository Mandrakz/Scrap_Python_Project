import requests, zipfile 
from io import BytesIO
print('Downloading ZIP started')

#Defining the zip file URL
url = 'http://ergast.com/downloads/f1db_csv.zip'
# Downloading the file by sending the request to the URL
req = requests.get(url)


# Split URL to get the file name
filename = "archive.zip"
 

# Writing the file to the local file system
with open(filename,'wb') as output_file:
     output_file.write(req.content)

    
print('Downloading ZIP Completed')


print('Extracting CSV from ZIP started')
# extracting the zip file contents
zip = zipfile.ZipFile(BytesIO(req.content))
zip.extractall('C:/Users/Carlos Franco/Desktop/Scrap_Python_Project/3_fileSaver')
print('Extracting CSV from ZIP Completed')
