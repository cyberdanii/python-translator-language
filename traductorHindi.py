from translate import Translator

traductor =  Translator(from_lang = "Spanish",to_lang="Hindi")
traduccion = traductor.translate(
	'''hola mundo.\n ''''''
	Mi nombre es Daniel y yo soy programador''')
print(traduccion)
file = open("traduccion.txt","w", encoding="utf-8")

file.write(traduccion)
file.close()


