import openai
openai.api_key = 'chave'

def enviar_mensagem(mensagem):
  resposta = openai.Completion.create(
    engine='text-davinci-003',
    prompt=mensagem,
    max_tokens=50,
    temperature=0.7,
    n=1,
    stop=None      
  )
  return resposta.choices[0].text.strip()

conversa_anterior = """
Você: Olá, como posso te ajudar?
Modelo: Eu sou um assistente virtual treinado para responder suas perguntas sobre produtos.
Você: Qual é o seu nome?
Modelo: Meu nome é ChatGPT. Como posso ajudar hoje?
"""
mensagem_usuario = input("Como posso ajudá-lo?")
conversa_atual = conversa_anterior + 'Você:' + mensagem_usuario

resposta = enviar_mensagem(conversa_atual)
print(f'Resposta do Chat GPT: {resposta}')
