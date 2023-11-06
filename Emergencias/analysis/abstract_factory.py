from abc import ABC, abstractmethod

class AbstractFactoryAnalisis(ABC):
    @abstractmethod
    def create_analisis_estadistico(self, data):
        pass

    @abstractmethod
    def create_visualizacion(self, data):
        pass
