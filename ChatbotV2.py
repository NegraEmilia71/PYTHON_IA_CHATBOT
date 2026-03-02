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

mensagem1 = 'OlÃ¡, como posso ajudar?'
mensagem2 = 'Qual Ã© o seu nome?'
mensagem3 = 'Onde posso encontrar informaÃ§Ãµes sobre o produto?'

resposta1 = enviar_mensagem(mensagem1)
resposta2 = enviar_mensagem(mensagem2)
resposta3 = enviar_mensagem(mensagem3)

print(f'Resposta 1: {resposta1}')
print(f'Resposta 2: {resposta2}')
print(f'Resposta 3: {resposta3}')
