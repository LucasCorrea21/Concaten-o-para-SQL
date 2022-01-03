from twilio.rest import Client

account_sid = "" #Este dado é fornecido na página inicial do seu perfil do Twilio
token = "" #Também é fornecido na página inicial do perfil do Twilio.

client = Client(account_sid, token)

remetente = ''#Coloque o número de remetente.
destino = '' #Coloque o número de destino

message = client.messages.create( #Criando uma mensagem
    to =destino,
    from_ =remetente,
    body = "Eae meu parceiro, parabéns tu criou uma API de mensagem"
)

print(message.sid) #Após o Print da mensagem, sinaliza que o código deu certo.
