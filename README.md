# Gerador de Senhas Seguras

O **Gerador de Senhas Seguras** é uma aplicação web desenvolvida em Python com Flask no backend e JavaScript no frontend. O objetivo do projeto é permitir que os usuários gerem senhas seguras de forma fácil e personalizável, garantindo maior segurança para suas contas e dados.

## Funcionalidades

- **Personalização de Senhas**: Escolha o comprimento da senha e os tipos de caracteres (letras maiúsculas, números e caracteres especiais).
- **Validação Dinâmica**: Limite de comprimento máximo de 60 caracteres.
- **Geração Aleatória**: As senhas são geradas de forma aleatória no backend.
- **Interface Intuitiva**: Exibição direta da senha gerada ao usuário.

## Tecnologias Utilizadas

- **Backend**: Python com Flask
- **Frontend**: HTML, CSS (TailwindCSS) e JavaScript
- **Outras Dependências**: Veja o arquivo [`requirements.txt`](requirements.txt) para a lista completa.

## Estrutura do Projeto
PasswordGenerator/ ├── .gitignore ├── password_generator.py # Código principal do backend Flask ├── README.md # Documentação do projeto ├── requirements.txt # Dependências do projeto ├── static/ │ └── script.js # Código JavaScript para interação com o backend ├── templates/ │ └── index.html # Página principal da aplicação └── .dist/ # Diretório para arquivos gerados (ignorado pelo Git)



## Como Executar o Projeto

1. **Clone o repositório**:
    ```bash
   git clone <URL_DO_REPOSITORIO>
   cd PasswordGenerator





**Crie um ambiente virtual**:
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

**Instale as dependências:**
pip install -r requirements.txt

**Inicie o servidor Flask:**
python password_generator.py

Acesse a aplicação: Abra o navegador e vá para http://127.0.0.1:5000.

## Como Usar

1- Escolha o comprimento da senha desejada (entre 6 e 60 caracteres).
2 - Marque as opções de personalização (letras maiúsculas, números e caracteres especiais).
3 - Clique no botão "Gerar Senha".
4 - A senha gerada será exibida na tela.