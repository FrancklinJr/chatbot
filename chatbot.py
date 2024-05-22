import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"oi|olá|ei",
        ["Olá, como você está?", "Oi, como posso te ajudar?", "Oi, tudo bem?"]
    ],
    [
        r"qual é o seu nome?",
        ["Meu nome é Chatbot, prazer em conhecê-lo!"]
    ],
    [
        r"como você está?",
        ["Estou bem, obrigado por perguntar!", "Estou ótimo, e você?"]
    ],
    [
        r"adeus|tchau",
        ["Tchau, foi bom falar com você!", "Adeus, até a próxima!"]
    ]
]

chatbot = Chat(pairs, reflections)

def chatbot_response(text):
    return chatbot.respond(text)