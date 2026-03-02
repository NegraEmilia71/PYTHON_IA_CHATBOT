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

mensagem_inicial = """
Você: Olá, como posso te ajudar?
Modelo: Eu sou um assistente virtual treinado para responder suas perguntas sobre produtos.
"""

instrucao = 'Dá uma resposta detalhada sobre os recursos do produto'
mensagem_usuario = 'Quais são os recursos do produto?'
conversa_com_instrucao = mensagem_inicial + 'Você:' + mensagem_usuario + '\nInstrucao: ' + instrucao
resposta = enviar_mensagem(conversa_com_instrucao)
