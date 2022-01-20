from classes.recipiente import Recipiente

class Copo(Recipiente):
    
    def __init__(self, tamanho: float, bebida: str = "água") -> None:
        super().__init__(tamanho)
        self.bebida = bebida

    def encher(self, bebida: str = "água"):
        
        if self.limpo:
            self.sujar()
            self.conteudo = self.tamanho
            self.bebida = bebida

        else:
            return "Não se pode encher um copo sujo"    
    
    def beber(self, quantidade: float):
        
        if quantidade < 0:
            return "Quantidade deve ser positiva"

        elif quantidade > self.tamanho:
            return "Não há bebida suficiente no copo"

        else:        
            self.conteudo = self.tamanho - quantidade

    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True       

    def __repr__(self):

        return f"Um copo vazio de {self.tamanho}ml" if self.conteudo == 0 else f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"

    def __str__(self):

        return f"Um copo vazio de {self.tamanho}ml" if self.conteudo == 0 else f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"   