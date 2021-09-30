from database import Database
from utils import  load_data, load_template, build_response
from urllib.parse import unquote_plus
from database import Database, Note

db = Database('banco')

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            key, value = chave_valor.split("=")
            value = unquote_plus(value)
            params[key] = value
        
        if params['action'] == 'create':

            if params["title"] and params["content"]:
                note = Note(title = params["title"], content = params["content"])
                db.add(note)
            
        elif params['action'] == 'update':
            note = Note(title = params["new_title"], content = params["new_content"], id = params["id"])
            db.update(note)
            
        elif params['action'] == 'delete':
            db.delete(params["id"])
           
        response = build_response(code=303, reason='See Other', headers='Location: /')
        return response

    note_template = load_template('./components/note.html')
    notes_li = [
        note_template.format(id= dados.id, title=dados.title, details=dados.content)
        for dados in db.get_all()]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))



