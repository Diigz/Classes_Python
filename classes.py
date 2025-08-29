class CaixaDeSom():
    def __init__(self):
        self.volumeMaximo = 100

    def Comparador(self, comparador):
        if comparador == self.volumeMaximo:
            print(f'Você chegou no volume máximo de {self.volumeMaximo}%\n')
        elif comparador < self.volumeMaximo:
            print(f'Você está no volume {comparador}% e falta apenas {self.volumeMaximo - comparador}% para estar no volume máximo.\n')
        else:
            print(f'Algo de errado, não está certo.\n')