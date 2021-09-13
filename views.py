from os import error, replace
from utils import  load_data, load_template, build_response, add_notes
from urllib.parse import unquote_plus

def params_(request):
    request = request.replace('\r', '') # Remove caracteres indesejados
     # Cabeçalho e corpo estão sempre separados por duas quebras de linha
    partes = request.split('\n\n')
    corpo = partes[1]
    params = {}
    # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        #titulo=Sorvete+de+banana 
        #detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D
    for chave_valor in corpo.split('&'):
        titulo = unquote_plus(chave_valor.split('=')[0])
        detalhes = unquote_plus(chave_valor.split('=')[1])
        params[titulo] = detalhes
    return params

def index(request):

    note_template = load_template('components/note.html')

    if request.startswith('POST'):
        params = params_(request)
        add_notes(params, 'notes.json')
        return build_response(code=303, reason='See Other', headers='Location: /')

    elif request.startswith('GET'):
        # Cria uma lista de <li>'s para cada anotação
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        notes_li = [
            note_template.format(title=dados['titulo'], details=dados['detalhes'])
            for dados in load_data('notes.json')
        ]
        notes = '\n'.join(notes_li)
        return build_response() + load_template('index.html').format(notes=notes).encode()
    
    