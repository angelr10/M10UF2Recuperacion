def fraseADiccionario(frase):
    spliteadoFrase = frase.split(" ")

    diccionarioFrase = {palabra:len(palabra) for palabra in spliteadoFrase}
    return diccionarioFrase

