print(f'Bem vindo ao meu ChatBot *digite x para sair*\n')
pergunta = input(f'Digite sua pergunta: ')

while True:
  print('ChatBot: Aqui colocarei a resposta do Bot.')
  pergunta = input('Usuário: ')
  if pergunta.lower() == 'x':
    break

print('Muito obrigado por testar o ChatBot')
