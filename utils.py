from pathlib import Path
import json
import os
from database import Database,Note

def extract_route(request):
    return request.split()[1][1:]

def read_file(path):
    str_path = str(path)
    if str_path.split(".") in ["txt", "html", "css", "js"]:
        with open(path, "r") as file:
            conteudo = file.read()
    else:
        with open(path, "rb") as file:
            conteudo = file.read()

    return conteudo

def load_data(path):
    with open ("data/{}".format(path), "r") as arquivo:
        conteudo = arquivo.read()
    return json.loads(conteudo)

def load_template(path):
    with open ("templates/{}".format(path), "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def add_notes(data):
    path = "data/notes.json"
    with open(path,'r', encoding ='utf-8') as file:
        write = json.load(file)
        write.append(data)
    with open(path, 'w', encoding ='utf-8') as file:
        json.dump(write, file, ensure_ascii=False, indent=4) 


def build_response(body='', code=200, reason='OK', headers=''):
    response = "HTTP/1.1 " + str(code) + " " + reason
    if headers != '':
        response += f"\n{headers}"
    response += f"\n\n{body}"
    return (response).encode()




