meme_dict = {"LOL" : "respuesta a algo gracioso","CRINGE": "algo raro o embarazoso","ROFL" : "una respuesta a una broma","SHEESH" : "ligera desaprobación","CREEPY" : "aterrador, siniestro","AGGRO" : "ponerse agresivo/enojado"}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(f"Significado de {word}: {meme_dict[word]}")
else:
    print(f"Lo siento, no tengo información sobre la palabra '{word}'.")
