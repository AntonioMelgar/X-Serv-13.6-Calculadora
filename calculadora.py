#!/usr/bin/python3
import sys

if len(sys.argv) != 4:
	sys.exit("3 argumentos de entrada necesarios");

funcion = sys.argv[1]; 
operando1 = sys.argv[2];
operando2 = sys.argv[3];

try:

	if sys.argv[1] == "sumar":
		resultado = float(operando1) + float(operando2); 

	elif  sys.argv[1] == "restar":
		resultado = float(operando1) - float(operando2);

	elif  sys.argv[1] == "multiplicar":
		resultado = float(operando1) * float(operando2);

	elif  sys.argv[1] == "dividir":
		resultado = float(operando1) / float(operando2);

	print(operando1 + funcion + operando2 + " = " + str(resultado));
except:
	print("ARGUMENTO1= sumar ó restar ó multiplicar ó dividir ; ARGUMENTO2= OPERANDO1 (float) ; ARGUMENTO3= OPERANDO2 (float)");	
