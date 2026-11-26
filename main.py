from __future__ import annotations # a classe setor é declarada depois, e causa erro em ingresso, esse import "evita" esse erro
from datetime import datetime
from abc import ABC, abstractmethod
from uuid import uuid4

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
    def __init__(self, setor: Setor) -> None:
        self.codigo = str(uuid4()) # a funcao uuid4 gera um codigo aleatorio de uns 20 digitos
        self.setor = setor
    
    @abstractmethod
    def calcular_preco(self, preco_base: float) -> float:
        """As subclasses irão implementar o método."""

class IngressoInteira(Ingresso):
    def __init__(self, setor: Setor) -> None:
        super().__init__(setor)

    def calcular_preco(self, preco_base) -> float:
        return preco_base

class IngressoMeia(Ingresso):
    def __init__(self, setor: Setor) -> None:
        super().__init__(setor)

    def calcular_preco(self, preco_base) -> float:
        return preco_base * 0.5

class IngressoVIP(Ingresso):
    def __init__(self, setor: Setor) -> None:
        super().__init__(setor)
    
    def calcular_preco(self, preco_base) -> float:
        return preco_base * 1.5

class Evento:
    def __init__(self, nome: str, local: str, data_hora: datetime) -> None:
        self.nome = nome
        self.local = local
        self.data_hora = data_hora
        self.setores: list[Setor] = []

class Setor:
    def __init__(self, nome: str, capacidade: int, preco_base: float) -> None:
        self.nome = nome
        self.capacidade = capacidade
        self.preco_base = preco_base
        self.ingressos_vendidos: list[Ingresso] = []

class Comprador:
    def __init__(self, nome: str, cpf: str, email: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Compra:
    def __init__(self, comprador: Comprador) -> None:
        self.comprador = comprador
        self.ingressos: list[Ingresso] = []
        self.compra_cancelada = False

class Bilheteria:
    def __init__(self) -> None:
        self.eventos: list[Evento] = []
        self.compradores: list[Comprador] = []