from datetime import datetime
from abc import ABC, abstractmethod

# Exceções Personalizadas:
class IngressoError(Exception):
    """No método da classe a exceção será personalizada e aplicada."""

class SetorLotadoError(IngressoError):
    """No método da classe a exceção será personalizada e aplicada."""

class LimiteMeiaEntradaError(IngressoError):
    """No método da classe a exceção será personalizada e aplicada."""

class LimitePorCompraError(IngressoError):
    """No método da classe a exceção será personalizada e aplicada."""

class EventoEncerradoError(IngressoError):
    """No método da classe a exceção será personalizada e aplicada."""

class CancelamentoNaoPermitidoError(IngressoError):
    """No método da classe a exceção será personalizada e aplicada."""

# Classes Principais:
class Ingresso(ABC):
    @abstractmethod
    def calcular_preco(self, preco_base: float) -> float:
        """As subclasses irão implementar o método."""

class IngressoInteira(Ingresso):
    def calcular_preco(self, preco_base) -> float:
        return preco_base

class IngressoMeia(Ingresso):
    def calcular_preco(self, preco_base) -> float:
        return preco_base * 0.5

class IngressoVIP(Ingresso):
    def calcular_preco(self, preco_base) -> float:
        return preco_base * 1.5

class Evento:
    def __init__(self, nome: str, local: str, data_hora: datetime) -> None:
        self.nome = nome
        self.local = local
        self.data_hora = data_hora
        self.setores = []

class Setor:
    def __init__(self, nome: str, capacidade: int, preco_base: float) -> None:
        self.nome = nome
        self.capacidade = capacidade
        self.preco_base = preco_base
        self.ingressos_vendidos = 0

class Comprador:
    def __init__(self, nome: str, cpf: str, email: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Compra:
    def __init__(self, comprador: Comprador) -> None:
        self.comprador = comprador
        self.ingressos = 0
        self.compra_cancelada = False

class Bilheteria:
    pass