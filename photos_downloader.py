import csv
import requests 
from PIL import Image 
import urllib3
import zipfile

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with zipfile.ZipFile("photos.zip", mode="w") as archive:
    with open('photo_script_test.csv') as photos_csv:
        photos_csv = list(csv.reader(photos_csv, delimiter = ';'))
        filenames = []

        for row in photos_csv[1:]:
            url = row[1]
            if url:
                data = requests.get(url, verify=False).content
                file_name = f'{row[0]}.jpg'
                filenames.append(file_name)
                archive.writestr(file_name, data)
    
