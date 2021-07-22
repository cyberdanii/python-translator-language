from translate import Translator

traductor = Translator(from_lang="Spanish", to_lang="Japanese")
traduccion = traductor.translate('''
		Hola Mundo, esto es una prueba de traduccion.
	''')
print(traduccion)
file = open("traduccion.txt","w", encoding="utf-8")
file.write(traduccion)
file.close()
