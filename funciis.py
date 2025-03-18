numeros_alma=[]
palind=[]
def mostrar_menu():
    print("1. Pares de nùmeros primos gemelos\n2. Primos palindròmicos\n3. Salir")
    print("____________________________________________________________________")

def deter_primo(num):
    
    count=0
    for j in range(2,num+1):
        if num%j==0:
            count=count+1
    if count==1:
        numeros_alma.append(num)
    
def palindro(numeros_alma):
    
    for j in numeros_alma:
        invert=str(j)
        invert=invert[::-1]
        if invert==str(j):
            palind.append(j)
    print("Los siguientes numeros primos son palindròmicos")
    print(palind)
    palind.clear()






    


    



