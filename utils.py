from pathlib import Path
import json

def extract_route(request):
    return request.split()[1][1:]

request_test = ""\
"GET /img/logo-getit.png HTTP/1.1 \n"\
"Host: 0.0.0.0:8080 \n"\
"Connection: keep-alive \n"\
"Accept: image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5 \n"\
"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15 \n"\
"Accept-Language: en-us \n"\
"Referer: http://0.0.0.0:8080/ \n"\
"Accept-Encoding: gzip, deflate"

#print(extract_route(request_test))

def read_file(filepath):
    if filepath.suffix in ['.txt', '.html', '.css', '.js']:
        mode = 'r'
    else:
        mode = 'rb'
    with open(filepath, mode=mode) as f:
        return f.read()

#print(read_file(Path("img/logo-getit.png")))

def load_data(path):
    with open ("data/{}".format(path), "r") as arquivo:
        conteudo = arquivo.read()
    return json.loads(conteudo)
#print(load_data(Path("notes.json")))

def load_template(path):
    with open ("templates/{}".format(path), "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo


def build_response(body='', code=200, reason='OK', headers=''):
    #'HTTP/1.1 200 OK\n\n'.encode() + response)
    if headers:
        headers=f"\n{headers}"
    response = f"HTTP/1.1 {code} {reason}{headers}\n\n{body}".encode()
    return response
# print(build_response())

def directory_verify(string, directory):
    j = 0
    string = str(string)
    for i in string:
        if i == '/':
            j += 1
    if j > 1:
        return str(string)
    else:
        return str(f'./{directory}/{string}')
    
def add_notes(data, filename):
    path = directory_verify(filename, 'data')
    with open(path,'r', encoding ='utf-8') as file:
        write = json.load(file)
        write.append(data)
    with open(path, 'w', encoding ='utf-8') as file:
        json.dump(write, file, ensure_ascii=False, indent=4) 