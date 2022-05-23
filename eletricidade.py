type = str(input('O que você quer saber? corrente? tensao? ou resistencia? '))

if type == 'resistencia':

    corrente = float(input('Qual é a corrente? digite o número: '))

    tensao = float(input('Qual é a tensao? digite o número: '))

    formula = tensao / corrente

    print('a resistencia é de ', formula, ' ohms')

elif type == 'tensao':

    resistencia = int(input('Qual é a resistencia? digite o número: '))

    corrente = float(input('Qual é a corrente? digite o número: '))

    formula = resistencia * corrente
    
    print('a tensão é de', formula)
    

elif type == 'corrente':

    tensao = float(input('Qual é a tensao? digite o número: '))

    resistencia = int(input('Qual é a resistencia? digite o número: '))

    formula = tensao / resistencia

    print('a corrente é de', formula)
