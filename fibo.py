def fibonacci():
    proximo = 1
    anterior = 0
    limite = 50
    found = 0
    resposta = "0,"
    while (found < limite):
        tmp = proximo
        proximo = proximo + anterior
        anterior = tmp
        found = found + 1
        resposta+= str(proximo)+ ","
    
    return resposta
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
