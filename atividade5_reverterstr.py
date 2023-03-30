def reverter_ordem_texto():
    """
    reverte uma entrada de string de traz para frente.
    """
    texto = input('insira uma palavra: ')
    
    texto_reverso = texto[::-1] 
    print(texto_reverso)

reverter_ordem_texto()
