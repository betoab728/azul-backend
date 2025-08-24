from abc import ABC, abstractmethod
from typing import List, Dict

class UbigeoRepository(ABC):

    @abstractmethod
    def get_departamentos(self) -> List[Dict]:
        """Lista todos los departamentos"""
        pass

    @abstractmethod
    def get_provincias(self, id_departamento: int) -> List[Dict]:
        """Lista provincias por id_departamento"""
        pass

    @abstractmethod
    def get_distritos(self, id_provincia: int) -> List[Dict]:
        """Lista distritos por id_provincia"""
        pass
