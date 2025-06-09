saida = ""

def adicao(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a, b):
    if (b == 0.0):
        return "Não foi possível realizar a divisão por 0"
    return a/b

def calculadora(a, b, operando):
    # resultado = 0
    if (operando.lower() == "adição" or operando.lower() == "mais" or operando == '+'):
        resultado = adicao(a, b)
    elif (operando.lower() == "subtração" or operando.lower() == "menos" or operando == '-'):
        resultado = subtracao(a, b)
    elif (operando.lower() == "multiplicação" or operando.lower() == "vezes" or operando == '*'):
        resultado = multiplicacao(a, b)
    elif (operando.lower() == "divisão" or operando.lower() == "dividido" or operando == '/'):
        resultado = divisao(a, b)
    else:
        resultado = "Não foi possivel entender a operação desejada. Tente novamente."
    return resultado

#######################################################################################
# FUNÇÃO EXTRA PARA GARANTIR O RECEBIMENTO CORRETO DE NÚMEROS INSERIDOS PELO USUÁRIO
#######################################################################################
def verifica_numero(texto):
    while True:
        resposta = input(texto)
        try:
            numero = float(resposta)
            return numero
        except ValueError:
            print(f">> '{resposta}' não é válido como um número da operação! Insira corretamente a seguir.")

#######################################################################################
# FUNÇÃO EXTRA PARA GARANTIR O RECEBIMENTO CORRETO DA INFORMAÇÃO DA OPERAÇÃO DESEJADA
#######################################################################################
def verifica_operacao(texto):
    operacoes_validas = [
        "adição", "mais", "+",
        "subtração", "menos", "-",
        "multiplicação", "vezes", "*",
        "divisão", "dividido", "/"
    ]
    
    while True:
        resposta = input(texto).strip().lower()
        if resposta in operacoes_validas:
            return resposta
        else:
            print(f">> '{resposta}' não é válido como uma operação! Insira uma das opções abaixo para continuar:")
            print("<ADIÇÃO>: Adição, mais ou +")
            print("<SUBTRAÇÃO>: Subtração, menos ou -")
            print("<MULTIPLICAÇÃO>: Multiplicação, vezes ou *")
            print("<DIVISÃO>: Divisão, dividido ou /")

while (saida.lower() != "n"):
    primeiro_numero = verifica_numero("Digite o primeiro número da operação: ")
    segundo_numero = verifica_numero("Digite o segundo número da operação: ")
    operacao = verifica_operacao("Insira a operação matemática [+, -, *, /]: ")

    resultado = calculadora(primeiro_numero, segundo_numero, operacao)
    print(f"\nResultado da operação: {resultado}")

    saida = input("\nDeseja continuar fazendo operações na calculadora? [S/N]")
    print('-----------------------------------------------------------\n\n')