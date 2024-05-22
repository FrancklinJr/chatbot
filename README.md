# Chatbot com Processamento de Linguagem Natural (NLP)

Este projeto é um chatbot simples que utiliza processamento de linguagem natural para responder a perguntas básicas. O chatbot é implementado usando a biblioteca `nltk` para NLP e `Flask` para criar uma interface web.

## Estrutura do Projeto

- `app.py`: Script principal que configura e inicia o servidor Flask.
- `chatbot.py`: Contém a lógica do chatbot e as respostas predefinidas.
- `templates/`
  - `index.html`: Interface web para interagir com o chatbot.
- `README.md`: Arquivo de documentação do projeto.

## Requisitos

- Python 3.6+
- Bibliotecas Python:
  - flask
  - nltk

## Instalação

1. Clone o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/seu-usuario/chatbot_project.git
    cd chatbot_project
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install flask nltk
    ```

4. Baixe os recursos necessários do NLTK:

    ```python
    python -c "import nltk; nltk.download('punkt')"
    ```

## Como Executar

1. Execute o aplicativo Flask:

    ```bash
    python app.py
    ```

2. Abra o seu navegador e vá para `http://127.0.0.1:5000/` para acessar o chatbot.

## Uso

- Digite uma mensagem na caixa de texto e clique em "Enviar" ou pressione Enter para interagir com o chatbot.
- O chatbot responderá com respostas predefinidas baseadas nas entradas do usuário.

## Exemplos de Interação

- Usuário: "oi"
- Chatbot: "Olá, como posso ajudar?"

- Usuário: "qual é o seu nome?"
- Chatbot: "Eu sou um chatbot, prazer em conhecê-lo!"

- Usuário: "como você está?"
- Chatbot: "Estou bem, obrigado por perguntar!"

- Usuário: "tchau"
- Chatbot: "Tchau, foi bom falar com você!"
