from abc import ABC, abstractmethod
from typing import List
from src.doman.models.cliente import Cliente


class ClienteRepositoryInterface(ABC):

    """ Interface to Pet Repository """

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Cliente:
        """ Abstractmethod """

        raise Exception("Method not implementend")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[Cliente]:
        """ Abstractmethod """

        raise Exception("Method not implementend")
