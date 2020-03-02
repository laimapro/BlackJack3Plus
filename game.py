import random


def start(input_number):

	if input_number in range(18, 21):
		print("Minha jogada: 21")
		print("Você perdeu, playboy!")
		print("Digite um número, de um a três, para jogar novamente.")

	elif input_number == 21:
		print("Você ganhou, espertinho!")
		print("Digite um número, de um a três, para jogar novamente.")

	elif input_number > 21:
		print("O jogo é 21, mané! Game over para você!")
		print("Digite um número, de um a três, para jogar novamente.")

	else:
		output_number = input_number + random.randrange(1, 4)
		if output_number == 21:
			print("Você perdeu, playboy!")
		else:
			print("Minha jogada:", output_number)


print("Bem-vindo ao jogo Black Jack 3+!")
print("Digite um número, de um a três, para iniciar o jogo.")

while True:
	input_number = int(input("Sua vez, carinha: "))
	start(input_number)