palabra=str(input('Ingrese una palabra '))

palabra=palabra.lower()

palabra = palabra.casefold()

# reverse the string
palabrareves = reversed(palabra)

# check if the string is equal to its reverse
if list(palabra) == list(palabrareves):
   print("La palabra es palindromo")
else:
   print("La palabra no es palindromo")