from classes import Recipiente, Copo

if __name__ == "__main__":

    r = Recipiente(100)
    print(r)
    print(r.esta_limpo())
    print(r.estado())

    r.sujar()
    print(r.esta_limpo())

    r.lavar()
    print(r.esta_limpo(), "\n")


    copo = Copo(300)
    print(copo)

    copo.encher('café')
    print(copo.bebida)
    print(copo.__str__())

    copo.beber(30)
    print(copo.__str__())

    copo.lavar()
    print(copo.esta_limpo())
    print(copo.__repr__())