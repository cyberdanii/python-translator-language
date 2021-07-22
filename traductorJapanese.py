from translate import Translator

# param 1: define el lenguage del texto a traducir
# param 2: define el lenguage al cual se traducira
traductor = Translator(from_lang="Spanish", to_lang="Japanese")

# se inserta el texto a traducir
traduccion = traductor.translate('''
		Hola Mundo, esto es una prueba de traduccion.
	''')
print(traduccion)

# se guarda el resultado en un archivo (opcional)
file = open("traduccion.txt","w", encoding="utf-8")
file.write(traduccion)
file.close()
