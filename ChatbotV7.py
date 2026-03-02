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

mensagem_usuario = input('Em que posso ajudar?')

if mensagem_usuario.startswith('/'): 
  comando = mensagem_usuario[1:]
  if comando == 'ajuda':
    resposta = 'Eu sou um assistente virtual que pode responder suas perguntas sobre os produtos. Como posso te ajudar?'
  else:
    resposta = 'Desculpe, não entendi o comando. Por favor, tente novamente'
else:
  resposta = enviar_mensagem(mensagem_usuario)

print(f'Resposta do ChatGPT: {resposta}')
