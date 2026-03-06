bpm = int(input('Insira seu batimentos cardíacos por minuto: '))
idade = int(input('Insira sua idade: '))

if idade <=2:
    if (bpm >= 120 and bpm <=140):
        print('Dentro')
    elif (bpm < 120):
        print('Abaixo')
    else:
        print('Acima')    

elif (idade >= 8) and (idade <= 17):
    if bpm >= 80 and bpm <=100:
        print('Dentro')
    elif bpm < 80:
        print('Abaixo')
    else:
        print('Acima')

