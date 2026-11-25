from datetime import datetime
from abc import ABC, abstractmethod

# Exceções Personalizadas:
class IngressoError(Exception):
    """No método da classe a exceção será personalizada e aplicada."""

class SetorLotadoError(Exception):
    """No método da classe a exceção será personalizada e aplicada."""

class LimiteMeiaEntradaError(Exception):
    """No método da classe a exceção será personalizada e aplicada."""

class LimitePorCompraError(Exception):
    """No método da classe a exceção será personalizada e aplicada."""

class EventoEncerradoError(Exception):
    """No método da classe a exceção será personalizada e aplicada."""

class CancelamentoNaoPermitidoError(Exception):
    """No método da classe a exceção será personalizada e aplicada."""

# Classes Principais:
class Ingresso(ABC):
    def __init__(self, nome: str, local: str, data_hora: datetime) -> None:
        self.nome = nome
        self.local = local
        self.data_hora = data_hora

    @abstractmethod
    def calcular_preco(preco_base: float) -> float:
        """As subclasses irão implementar o método."""

class IngressoInteira(Ingresso):
    def __init__(self, nome, local, data_hora) -> None:
        super().__init__(nome, local, data_hora)

    def calcular_preco(preco_base) -> float:
        return preco_base

class IngressoMeia(Ingresso):
    def __init__(self, nome, local, data_hora) -> None:
        super().__init__(nome, local, data_hora)
    
    def calcular_preco(preco_base) -> float:
        return preco_base * 0.5

class IngressoVIP(Ingresso):
    def __init__(self, nome, local, data_hora):
        super().__init__(nome, local, data_hora)
    
    def calcular_preco(preco_base):
        return preco_base * 1.5

class Evento:
    pass

class Setor:
    pass

class Compra:
    pass

class Comprador:
    pass

class Bilheteria:
    pass

