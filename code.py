        # Meu Primeiro App com Kivy

#   * Para melhor funcionamento do Kivy, acesse kivy.org
#   e em documentações segue o passo a passo recomendado para seu sistema operacional
#   * Instalar o kivy no terminal: pip install kivy

        # 1. Para iniciar um app com kivy você precisa:

# importar do kivy a função App e Builder (GUI)
# criar uma classe para o nosso aplicativo
# criar a função build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

        #  2. Criando a classe para o App
        #  função def do GUI

class MeuAplicativo(App):
    def build(self):
        return GUI
        
        # 3. Selecionando a cotação
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dolar R${self.cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.cotacao('ETH')}"

        #  4. Cconsumindo API de conversão de moedas:
        #  preparando a requisição usando o requests.get
        #  recebendo o arquivo em formato .json e retornando a cotação em tempo real
    def cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

# Executa abaixo a janela
MeuAplicativo().run()


