# Importo la clase ABC (Abstract Base Class) del módulo "abc".
from abc import ABC, abstractmethod

# Defino una clase abstracta "AbstractFactoryAnalisis" que hereda de "ABC".


class AbstractFactoryAnalisis(ABC):
    # Defino dos métodos abstractos que deben ser implementados por las subclases.
    @abstractmethod
    def create_analisis_estadistico(self, data):
        pass

    @abstractmethod
    def create_visualizacion(self, data):
        pass
