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
resposta = enviar_mensagem(mensagem_usuario)

if 'Desculpe, não entendi' in resposta:
  mensagem_usuario = 'Você pode fornecer mais detalhes?'
  resposta = enviar_mensagem(mensagem_usuario)

print(f'Respoata do ChatGPT: {resposta}')
