#!/usr/bin/python3

"""this is the main file. a CLI application."""

from config import database_filename, first_table_name, hash_salt
from records import Records
from pprint import pprint
import crypts
import cryptography
import requests
import simplejpeg
import cv2
import sys
from getpass import getpass


# password = input('password:').encode()
password = getpass().encode()
cryptor = crypts.generate_fernet(password, hash_salt)
record = Records(database_filename, first_table_name, fernet_object=cryptor)
record.check_key()



data_type = sys.argv[1]
if data_type == 'text':
    text = sys.argv[2]
    record.add_record('text', text)

elif data_type == 'link':
    link = sys.argv[2]
    image_response = requests.get(link)
    image = image_response.content
    record.add_record('image', image)
    
elif data_type == 'image':
    filename = sys.argv[2]
    image = open(filename, 'rb').read()
    record.add_record('image', image)

elif data_type == 'show':
    a = record.return_all_records()

    for k in a:
        if k[1] == 'image':
            image = k[2]
            p = simplejpeg.decode_jpeg(image)
            q = cv2.cvtColor(p, cv2.COLOR_RGB2BGR)
            cv2.imshow(k[0][:10], q)
            cv2.waitKey(0)
            print(k[0][:10], 'IMAGE')
        elif k[1] == 'text':
            print(k[0][:10], k[2])
        else:
            print(k[0][:10], k[1], ': COULD NOT DECODE!')
