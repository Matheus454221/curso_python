   
#MENOR QUE 18,5	MAGREZA 0
#ENTRE 18,5 E 24,9	NORMAL 0
#ENTRE 25,0 E 29,9	SOBREPESO	I
#ENTRE 30,0 E 39,9	OBESIDADE	II
#MAIOR QUE 40,0	OBESIDADE GRAVE	III
def imc(): 
    weight = float(input("Digite seu peso: "))
    height = float(input("Digite sua altura: "))    
    imc_usuario = weight/(height * height)
    if  (imc_usuario <= 18.5):
            print(f'Seu Índice de Massa Corporal(IMC) é {imc_usuario}')
            print('Seu grau de obesidade é 0 porém você esta muito magro, o IMC ideal é entre 18.5 e 24.9')
           
    elif (imc_usuario >= 18.5 and imc_usuario <= 24.9):
            print(f'Seu Índice de Massa Corporal(IMC) é {imc_usuario}')
            print('Parabéns, seu clacificação de obesidade é 0 e seu IMC esta dentro do recomendado')
           
    elif (imc_usuario >= 25.0 and imc_usuario <= 29.9):
            print(f'Seu Índice de Massa Corporal(IMC) é {imc_usuario}')
            print('Sua clacificação de obesidade é 1, procure ter uma alimentação saldavel e pratique atividades físicas')
        
    elif (imc_usuario >= 30.0 and imc_usuario <= 39.9):
            print(f'Seu Índice de Massa Corporal(IMC) é {imc_usuario}')
            print('Seu grau de obesidade é 2, isso é preocupante, procure a ajuda de um médico.')
        
    else:
            print(f'Seu Indice de Massa Corporal(IMC) é {imc_usuario}')
            print('Seu grau de obesidade é 3, isso é muito sério, procure ajuda com urgencia.')
            
    return
 
    
    

    
    
    


    

        
 
                                
    
    