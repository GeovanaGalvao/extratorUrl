url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
# Separa a base dos parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

# Busca o valor de um parâmetro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
valor = (url_parametros[indice_valor:] if indice_e_comercial == -1 else url_parametros[indice_valor:indice_e_comercial])
''' Se a informação a ser buscada ser depois do ultimo &, o valor a ser atribuido irá até o final da string, 
caso contrário será considerado o indice do parâmetro a ser buscado até o próximo & na string.'''
print(valor)
