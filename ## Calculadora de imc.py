## Calculadora de imc

Altura = float(input("Qual é a sua altura?: "))
Peso = float(input("Qual é o seu peso?: "))
imc =  Peso / (Altura **2)
print (imc)

if imc < 18.5:
    print ("Seu peso está abaixo do normal!")
elif imc < 24.9:
    print ("Seu peso está normal!")
elif imc < 29.9:
    print ("Você está com sobrepeso!")
elif imc < 34.9:
    print ("Obesidade grau 1, sinal de ALERTA!")
elif imc < 39.9:
    print ("Obesidade grau 2, é hora de se cuidar!")
elif imc > 40.0: 
    print ("Obesidade grau 3, o tratamento deve ser urgente")