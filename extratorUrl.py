class ExtratorURL:
    def __init__(self, url):
        self.url = url.strip()
        self.valida_url()

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL está vazia")

    def get_url_base(self):
        return self.url[:self.url.find('?')]

    def get_url_parametros(self):
        return self.url[self.url.find('?') + 1:]

    def get_valor_parametro(self, parametro):
        indice_valor = self.get_url_parametros().find(parametro) + len(parametro) + 1
        # Retorna a posição inicial do valor de interesse
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        return self.get_url_parametros()[indice_valor:] if indice_e_comercial == -1 \
            else self.get_url_parametros()[indice_valor:indice_e_comercial]
        '''Retorna a posição final do valor de interesse. Se o indice_e_comercial = -1, signfica que não existe mais
        separador & depois do valor, então será atribuido o valor até o final da string. Caso o resultado seja maior
        que -1, significa que o indice do valor a ser atribuido termina no próximo &.'''
