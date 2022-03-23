
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque(temperatura)
        self._add_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque(self, temperatura):
        print(f'Llenando tanque con agua {temperatura}')

    def _add_jabon(self):
        print(f'Agregando jabón')
    
    def _lavar(self):
        print(f'Lavando')
    
    def _centrifugar(self):
        print('centrifugando')
    
if __name__=='__main__':
    lavadora = Lavadora()
    lavadora.lavar()