import csv
import requests 
from PIL import Image 
import urllib3
import zipfile

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with zipfile.ZipFile("photos.zip", mode="w") as photos_zip:
    with open('photo_script_test.csv','r') as photos_csv:
        photos_csv_reader = list(csv.reader(photos_csv, delimiter = ';'))
        lines_to_update = {}

        for line, row in enumerate(photos_csv_reader[1:]):
            url = row[1]
            if url:
                data = requests.get(url, verify=False).content
                file_name = f'{row[0]}.jpg'
                photos_zip.writestr(file_name, data)
                lines_to_update[line+2] = [row[0], f'/{file_name}']
    
    with open('photo_script_test.csv', 'w', newline='') as photos_csv:
        photos_csv_writer = csv.writer(photos_csv)

        for line, row in enumerate(photos_csv_reader):
            data = lines_to_update.get(line+1, row)
            photos_csv_writer.writerow(data)
