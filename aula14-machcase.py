# match case

n = 3

match n:
    case 0:
        print('é zero')
    case 1:
        print('é um')
    case 2:
        print('é dois')
    case _:
        print('Desconhecido')



n1 = int(input('Digite um numero >>'))



match n1:
    case x if x > 0:
        print('é positivo')
    case x if x < 0:
        print('é negativo')
    case _:
        print('é zero')
