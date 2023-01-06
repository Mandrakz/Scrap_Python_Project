# importing necessary modules
import requests, zipfile
from io import BytesIO
print('Downloading ZIP started')

#Defining the zip file URL
url = 'https://storage.googleapis.com/kaggle-data-sets/468218/4670928/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230105%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230105T232327Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=a0f1f65706297b309504e0152dd57a510d05aa3457adc1db55107d05690f42e3a7ca16bdfdfcfcf09970357c089db7fc02e440c57f19cc81812a5ae386da9038e2ad0c4b41393ba139bd0ac2fb48dc36f95998c7b301d183781dadccc29b2d45d8d6cda4d3226353013366b643dd1278ab570a11030efedff9c54daca8042591c02a15a630c3efc75a7dd9b1b786358bdb5b71f8813ffb484d11f3656101e86d46c6c31d13b6348c43d3b70b9d4f5af4d8f7979bac0f6fb37dd19995b503bbaa017111395ab45f3e5654aa1d1c7ab3fdb57ade6278223f3ee3da6857bd713491d2a00ffdcba9900646c3a46cd1a519dbc2b7415c1a64c625a250da213d25dc84'

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
zipfile = zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall('/home/carlos/Scrap_Pyton/fileSaver')

print('Extracting CSV from ZIP Completed')














