import openai
import requests

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

def obter_resposta_da_api(pergunta):
  resposta = requests.get(f'https://api.example.com/perguntas?pergunta={pergunta}')
  return resposta.json()['resposta']

mensagem_usuario = 'Qual a capital da França?'

if mensagem_usuario.starrtswitch('/api'):
  pergunta = mensagem_usuario[5:]
  resposta = obter_resposta_da_api(pergunta)
else:
  resposta = enviar_mensagem(mensagem_usuario)
