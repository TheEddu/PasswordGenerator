from flask import Flask, request, jsonify, render_template
import random
import string
# - `Flask`: é a ferramenta que cria o servidor web.
# - `request`: pega os dados enviados do formulário (como o comprimento da senha).
# - `jsonify`: transforma uma resposta Python em JSON (um formato que o navegador entende).
# - `render_template`: serve páginas HTML.
# - `random` e `string`: usados para montar a senha aleatória (com letras, números e símbolos).

# Inicializando o app Flask.
app = Flask(__name__)

# Função principal para gerar a senha.
# Essa função monta um conjunto de caracteres com base nas opções marcadas pelo usuário e gera uma senha aleatória do tamanho especificado.

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    #Essa função recebe 4 parâmetros:
        # - `length`: comprimento da senha.
        # - `include_uppercase`: letras maiúsculas
        # - `include_numbers`: números?
        # - `include_special_chars`: símbolos como @, #, %
    characters = string.ascii_lowercase # Começamos com letras minúsculas, a base padrão.
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    # Aqui ele monta a senha escolhe, aleatoriamente (usando random.choice), um caractere por vez (for _ in range) do conjunto de permitido baseado no que o usuário escolheu até atingir o comprimento (length) desejado.

    # Tudo isso é reunido em `password` e retornado.
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Essa rota exibe a interface principal, index.html é o “HTML principal” (no caso desse projeto, é o único HTML).
@app.route('/')
def index():
    return render_template('index.html')

# Esta rota responde a uma requisição feita pelo JavaScript no frontend, gera a senha e a retorna em formato JSON.
@app.route('/generate_password', methods=['POST'])
def generate_password_endpoint():
    data = request.json # Aqui o app Flask recebe uma requisição POST, que é enviada pelo JavaScript da página quando o usuário clica em "Gerar Senha".
    
    # Pega os dados enviados no corpo da requisição em formato JSON.
    # Essas linhas extraem os dados do JSON e guardam nas variáveis.
    length = data.get('length', 12)
    include_uppercase = data.get('include_uppercase', True)
    include_numbers = data.get('include_numbers', True)
    include_special_chars = data.get('include_special_chars', True)

    # Aqui o backend chama a função que gera a senha, com base nas opções recebidas.
    password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
    # Retorna a senha gerada no formato JSON de modo que o navegador possa exibir ao usuário.
    return jsonify({'password': password})

# Roda o servidor
if __name__ == '__main__':
    app.run(debug=True)
# Essa linha faz com que o servidor Flask seja iniciado **apenas quando você roda esse arquivo diretamente**, e não quando ele é importado por outro.

# O `debug=True` ativa o modo desenvolvedor (útil para testes e ver erros mais facilmente).