import requests, zipfile 
from io import BytesIO
print('Downloading ZIP started')

#Defining the zip file URL
#url = 'https://storage.googleapis.com/kaggle-data-sets/468218/4670928/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230105%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230105T232327Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=a0f1f65706297b309504e0152dd57a510d05aa3457adc1db55107d05690f42e3a7ca16bdfdfcfcf09970357c089db7fc02e440c57f19cc81812a5ae386da9038e2ad0c4b41393ba139bd0ac2fb48dc36f95998c7b301d183781dadccc29b2d45d8d6cda4d3226353013366b643dd1278ab570a11030efedff9c54daca8042591c02a15a630c3efc75a7dd9b1b786358bdb5b71f8813ffb484d11f3656101e86d46c6c31d13b6348c43d3b70b9d4f5af4d8f7979bac0f6fb37dd19995b503bbaa017111395ab45f3e5654aa1d1c7ab3fdb57ade6278223f3ee3da6857bd713491d2a00ffdcba9900646c3a46cd1a519dbc2b7415c1a64c625a250da213d25dc84'
url = 'https://storage.googleapis.com/kaggle-data-sets/468218/4670928/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230203%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230203T235235Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=707d1b601f3bedec7fc487aea73c9e760bf7f7591d69aeb4f758e03af6cc2cbe5001d0e21262815a6371dea4066ded07dcf6f7e1a1dcc4df683b8ecf9cf8d367fd4469959f89caab6e1d690b309f2baa634d6001a9ffab140a25f1ac57bffa7f1e11964a58bf35421b33c424d6cef68cb8af7ef58e22b046f1390dcbc625195279920413d0daa5b0818e2e293050746a223fe3a57eace8e513a63086e6f1e3e5cf4f80bfa10538b147018b6d8809332df32a5ce1f35dc78b8bca987d679862bfbdca6ee3595c5e9ed3547fdb7031cf64f5ad7b21ccfa2a3984cc03db26c672aeade7c0797d3e72fd8827600db64a91f96846c9d563b205bfe064741fb32f3160'

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
zip.extractall('C:/Users/Carlos Franco/Desktop/TaskAutom/Scrap_Python_Project/fileSaver')
print('Extracting CSV from ZIP Completed')