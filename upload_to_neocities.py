#!/usr/bin/python3
import neocities
from glob import glob
import os, json

f = open("credentials.txt") # Credentials file
credentials = json.loads(f.read())
USERNAME = credentials["username"]
PASSWORD = credentials["password"]
LOCAL_DIRECTORY = "public" # Hugo generates the site in the public directory

file_extensions = [
    '.html','.htm',
    '.jpg','.png','.gif','.svg','.ico',
    '.js','.json','.css','.txt','.csv','.xml',
    '.eot','.ttf','.woff','.woff2']

def push(d):
    ''' recursive directory upload, adapted from https://github.com/neoslaughter/python-neo '''
    files = glob(d + '/**', recursive=True)
    for file_name in files:
        if os.path.splitext(file_name)[1] in file_extensions:
            destination_path = file_name.replace(LOCAL_DIRECTORY,'').replace("\\","/")
            nc.upload((file_name, destination_path))
            print("Uploaded {} as {}".format(file_name, destination_path))

nc = neocities.NeoCities(USERNAME, PASSWORD)
push(LOCAL_DIRECTORY)
