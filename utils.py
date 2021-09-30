from pathlib import Path
import json
import os

def extract_route(request):
    return request.split()[1][1:]

# request_test = ""\
# "GET /img/logo-getit.png HTTP/1.1 \n"\
# "Host: 0.0.0.0:8080 \n"\
# "Connection: keep-alive \n"\
# "Accept: image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5 \n"\
# "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15 \n"\
# "Accept-Language: en-us \n"\
# "Referer: http://0.0.0.0:8080/ \n"\
# "Accept-Encoding: gzip, deflate"

# print(extract_route(request_test))

def read_file(path):
    str_path = str(path)
    if str_path.split(".") in ["txt", "html", "css", "js"]:
        with open(path, "r") as file:
            conteudo = file.read()
    else:
        with open(path, "rb") as file:
            conteudo = file.read()

    return conteudo

# print(read_file(Path("img/logo-getit.png")))

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
        json.dump(write, file, ensure_ascii=False, indent=4) \


def build_response(body='', code=200, reason='OK', headers=''):
    response = "HTTP/1.1 " + str(code) + " " + reason
    if headers != '':
        response += f"\n{headers}"
    response += f"\n\n{body}"
    return (response).encode()


