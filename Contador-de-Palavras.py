def contar_palavras_e_caracteres(texto):
    palavras = texto.split() #Divide o texto por espaços em branco
    numero_palavras = len(palavras)
    numero_caracteres = len(texto.replace(" ", " ")) # Remove os espaços para contar apenas os caracteres

    return numero_palavras, numero_caracteres

def contador_de_palavras():
    print ("===== Contador de Palavras e Caracteres =====")
    texto = input("Digite o texto para contagem: ")

    palavras, caracteres = contar_palavras_e_caracteres(texto)

    print(f"\nO texto possui {palavras} palavras e {caracteres} caracteres (sem contar os espaços).")

def continuar_contagem ():
    while True:
        contador_de_palavras()
        resposta = input("\nDeseja contar palavras em outro texto? (sim/não): ").strip().lower()
        if resposta != 'sim':
            print("Obrigado por usar o contador de palavras! Até logo.")
            break

#Começando a contagem
continuar_contagem()