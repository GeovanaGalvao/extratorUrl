import re


class ExtratorURL:
    def __init__(self, url):
        self.valida_url(url)
        self.url = url.strip()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.get_url_base() + "\nMoeda Origem: " + self.get_moeda_origem() + "\nMoeda Destino: "\
               + self.get_moeda_destino() + "\nQuantidade: " + self.get_quantidade()

    def __eq__(self, other):
        return self.url.__eq__(other.url)

    @staticmethod
    def valida_url(url):
        if type(url) != str or not url:
            raise ValueError("A URL é inválida")
        elif not re.compile('(http(s)?://)?(www.)?bytebank.com.br/cambio').match(url):  # valida a URL
            raise ValueError("A URL é inválida")

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

    def get_moeda_origem(self):
        return self.get_valor_parametro("moedaorigem")

    def get_moeda_destino(self):
        return self.get_valor_parametro("moedadestino")

    def get_quantidade(self):
        return self.get_valor_parametro("quantidade")
