from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"
    
class Gato(Animal):
    def comer():
        return "gato comendo"
    
def main():
    cachorro = Cachorro()
    gato = Gato()

    print(cachorro.emitir_som())

main()