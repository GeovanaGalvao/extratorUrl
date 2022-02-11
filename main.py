import extratorUrl


url = extratorUrl.ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
print(url.get_valor_parametro("quantidade"))
