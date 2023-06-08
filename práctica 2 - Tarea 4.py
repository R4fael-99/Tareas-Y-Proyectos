while True:
 try: 
  num1 = float(input("Ingrese el primer número: "))
  num2 = float(input("Ingrese el segundo número:"))
 except:
  print("Error: ingrese un número válido")
 operacion = input("Ingrese la operación a realizar (+,-,*,/):") 
 if operacion == "+":
  resultado = num1 + num2
  print("El resultado es: ", resultado)
 elif operacion == "-":
  resultado = num1 - num2
  print("El resultado es: ", resultado)
 elif operacion == "*":
  resultado = num1 * num2
  print("El resultado es: ", resultado)
 elif operacion == "/":
  if num2 == 0:
   print("Error: no se puede dividir entre cero")
  else:
   resultado = num1/num2 
   print("El resultado es: ", resultado)
 else:
  print("Error: ingrese una operación válida (+,-,*,/)")
 continuar = input("¿Desea realizar otra operación? (S/N):") 
 if continuar!= "S": 
  break
print("Hasta luego!")