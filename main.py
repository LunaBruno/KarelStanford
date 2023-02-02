# AMB1430 - Programação para Engenharia Elétrica

# Atividade 01 - Documente as funções através do simbolo # (comentário)
# Atividade 02 - Escreva uma função que permita o robô Karel varrer o mundo diagonalmente.
#                Utilize a função put_beeper() ao entrar em uma nova posição
#                https://github.com/TylerYep/stanfordkarel
# Atividade 03 - Escreva uma função que permita o robô Karel varrer o mundo aleatoriamente.
#                Utilize a função random para obter um número inteiro entre 1 e 3

# Importar módulos e funções
# import random
from stanfordkarel import *


# Função principal
def main():

    move()
    move()
    move()

    # Escrever a função para varrer o mundo diagonalmente
    # varrer_diagonal()
    # Utilizar a função para inserir beep na posição
    put_beeper()

    # # Escrever a função para varrer o mundo aleatoriamente
    # varrer_aleatoriamente()
    #   # Utilizar a função random para obter um número inteiro entre 1 e 3
    #   random.randint(1, 3)
    #   # Utilizar o resultado do sorteio para
    #   # 1 - Mover
    #   # 2 - Girar a esquerda e mover
    #   # 3 - Girar a direita e mover
    #   # 4 - Girar até atingir o sentido contrário e mover
    #   # Observar


# Inicialização do programa
if __name__ == "__main__":
    run_karel_program()


# Girar para a direita
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# # Inserir a decrição da função
# def mover_fronteira():
#   # Documentar o corpo da função
#   while front_is_clear():
#     move()

# # Inserir a decrição da função
# def varrer_fronteira():
#   # Documentar o corpo da função
#   for contador in range(4):
#     mover_fronteira()
#     turn_left()

# # Inserir a decrição da função
# def varrer_horizontal():
#   # Documentar o corpo da função
#   while front_is_clear():
#     mover_fronteira()
#     turn_left()
#     if front_is_clear():
#       move()
#       turn_left()
#     mover_fronteira()
#     turn_right()
#     if front_is_clear():
#       move()
#       turn_right()

# # Inserir a decrição da função
# def varrer_vertical():
#   # Documentar o corpo da função
#   turn_right()
#   turn_right()
#   while front_is_clear():
#     mover_fronteira()
#     turn_left()
#     if front_is_clear():
#       move()
#       turn_left()
#     mover_fronteira()
#     turn_right()
#     if front_is_clear():
#       move()
#       turn_right()
