def chatbot_resposta(mensagem):
    mensagem = mensagem.lower()

    if 'oi' in mensagem or 'olá' in mensagem:
        return "Olá! Como posso ajudar você?"
    elif 'tudo bem' in mensagem or 'como vai' in mensagem:
        return "Estou bem, obrigado! E você?"
    elif 'qual seu nome' in mensagem:
        return "Eu sou um chatbot simples feito em Python."
    elif 'adeus' in mensagem or 'tchau' in mensagem:
        return "Até logo! Foi bom conversar com você."
    else:
        return "Desculpa, não entendi. Pode repetir?"

# Loop para conversar com o chatbot
while True:
    user_input = input("Você: ")
    if user_input.lower() in ['sair', 'exit', 'quit']:
        print("Chatbot: Até mais!")
        break

    resposta = chatbot_resposta(user_input)
    print(f"Chatbot: {resposta}")
