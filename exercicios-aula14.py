# EXERCÍCIOS: 

# 1: Verificando se o número é par ou ímpar

num = int(input('>> '))

match num:
    case x if x % 2 == 0:
        print('Par')
    case x if x % 2 == 1:
        print('impar')
    case _:
        print('Desconhecido')

# 2: Verificando se um número é positivo, negativo ou zero


numero = int(input('>>'))

match numero:
    case x if x > 0:
        print('Positivo')
    case x if x < 0:
        print('negativo')
    case _:
        print('zero')

# 3: Verificando se uma string é vazia ou não
        
exisitir = input('digite algo> ')

match exisitir:
    case a if a:
        print('Existe')
    case _:
        print('Não existe')

# 4: Verificando se um número é maior, menor ou igual a 10,
        
number = int(input('Digite um numero>> '))

match number:
    case n if n > 10:
        print('maior q 10')
    case n if n < 10:
        print('menor q 10')
    case n if n == 10:
        print('é 10')

# 5: Classificando uma idade em faixas etárias -  criança, jovem, adulto, 
        
def etaria():
        
    idade = int(input('Digite sua idade: '))

    match idade:
        case i if i <= 2:
            print('bb')
        case i if i <= 12:
            print('Criança')
        case i if i < 18:
            print('jovem')
        case i if i >= 18:
            print('Adulto')
        case i if i >= 63:
            print('Idoso')


etaria()
