#for hora in range(24):
    #for minuto in range (60):
        #for segundo in range (60):
            #print (f"{hora:02d}:{minuto:02d}:{segundo:02d}")
            

nombre= "ana"
edad = 25
print (f"Hola {nombre}, tienes {edad} años.")


a= 10
b = 5
print (f"La suma es {a + b}")


#Aliner texto 
print (f"{'Hola': <10}-")
print (f"{'Hola': >10}-")
print (f"{'Hola': ^10}-")


#Floats con decimales fijos
pi = 3.14159265
print(f"{pi:.2f}")
#despues del punto 2 cifras flotantes (Reales)


#Separador de miles
num = 1234567
print (f"{num:,}")


#Para usar punto como separador 
print (f"{num:,}".replace(',', '.'))


#Formato en porcentaje
x = 0.1234
print (f"{x:.2%}")


#saltos
for i in range(5,0,-1):
    print (i)