# Gerador de Senhas Seguras

O **Gerador de Senhas Seguras** é uma aplicação web desenvolvida em Python com Flask e JavaScript. O objetivo do projeto é permitir que os usuários gerem senhas seguras de forma fácil e personalizável..

## Funcionalidades

- **Personalização de Senhas**: Escolha o comprimento da senha e os tipos de caracteres (letras maiúsculas, números e caracteres especiais).
- **Validação Dinâmica**: Limite de comprimento máximo de 60 caracteres.
- **Geração Aleatória**: As senhas são geradas de forma aleatória no backend.
- **Interface Intuitiva**: Exibição direta da senha gerada ao usuário.

## Tecnologias Utilizadas

- **Backend**: Python com Flask
- **Frontend**: HTML, CSS (TailwindCSS) e JavaScript
- **Outras Dependências**: Veja o arquivo [`requirements.txt`](requirements.txt) para a lista completa.



## Como Executar o Projeto

1. **Clone o repositório**:
    ```bash
   git clone <URL_DO_REPOSITORIO>
   cd PasswordGenerator

**Crie um ambiente virtual**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows: .venv\Scripts\activate

**Instale as dependências:**
    ```bash
    pip install -r requirements.txt

**Inicie o servidor Flask:**
    ```bash
    python password_generator.py

Acesse a aplicação: Abra o navegador e vá para http://127.0.0.1:5000.

## Como Usar

1- Escolha o comprimento da senha desejada (entre 6 e 60 caracteres).
2 - Marque as opções de personalização (letras maiúsculas, números e caracteres especiais).
3 - Clique no botão "Gerar Senha".
4 - A senha gerada será exibida na tela.