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

class IngressoNaoEncontradoError(IngressoError):
    """No método da classe a exceção será personalizada e aplicada."""

# Classes Principais:
class Ingresso(ABC):
    def __init__(self, setor: Setor) -> None:
        self.codigo = str(uuid4()) # a funcao uuid4 gera um codigo aleatorio de uns 30 digitos
        self.setor = setor
        self.eh_meia_entrada = False
    
    @abstractmethod
    def calcular_preco(self, preco_base: float) -> float:
        """As subclasses irão implementar o método."""

class IngressoInteira(Ingresso):
    def __init__(self, setor: Setor) -> None:
        super().__init__(setor)
        self.eh_meia_entrada = False

    def calcular_preco(self, preco_base: float) -> float:
        return preco_base

class IngressoMeia(Ingresso):
    def __init__(self, setor: Setor) -> None:
        super().__init__(setor)
        self.eh_meia_entrada = True

    def calcular_preco(self, preco_base: float) -> float:
        return preco_base * 0.5

class IngressoVIP(Ingresso):
    def __init__(self, setor: Setor) -> None:
        super().__init__(setor)
        self.eh_meia_entrada = False
    
    def calcular_preco(self, preco_base: float) -> float:
        return preco_base * 1.5

class Setor:
    def __init__(self, nome: str, capacidade: int, preco_base: float) -> None:
        self.nome = nome
        self._ingressos_vendidos: list[Ingresso] = [] # joguei pra cima pq nos testes dava attribute error
        self.capacidade = capacidade
        self.preco_base = preco_base

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if nome.strip() == "":
            raise ValueError("O nome não deve estar vazio.")
        else:
            self._nome = nome

    @property
    def capacidade(self) -> int:
        return self._capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int) -> None:
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser um número maior que 0.")
        if capacidade < len(self._ingressos_vendidos):
            raise ValueError("A capacidade deve ser um número maior que a quantidade de ingressos vendidos.")
        else:
            self._capacidade = capacidade

    @property
    def preco_base(self) -> float:
        return self._preco_base

    @preco_base.setter
    def preco_base(self, preco_base: float) -> None:
        if preco_base <= 0:
            raise ValueError("O preço base deve ser um número maior que 0.")
        else:
            self._preco_base = preco_base

    @property
    def ingressos_vendidos(self) -> tuple:
        return tuple(self._ingressos_vendidos) # tupla é imutavel, se for lista, podem mudar os itens dela

    @property
    def vagas_disponiveis(self) -> int:
        return self._capacidade - len(self._ingressos_vendidos)

    @property
    def ta_lotado(self) -> bool:
        return self.vagas_disponiveis == 0

    @property
    def limite_meia_entrada(self) -> int:
        return int(self._capacidade * 0.4) # limite de 40% p meia entrada, se der float, retorna int por meio de int()

    @property
    def quantidades_meia_entrada_vendidas(self) -> int:
        quantidade = 0

        for ingresso in self._ingressos_vendidos:
            if ingresso.eh_meia_entrada:
                quantidade += 1

        return quantidade

    def adicionar_ingresso(self, ingresso: Ingresso) -> None:
        if self.ta_lotado:
            raise SetorLotadoError("O setor está lotado.")
        
        if ingresso.eh_meia_entrada:
            if self.quantidades_meia_entrada_vendidas >= self.limite_meia_entrada:
                raise LimiteMeiaEntradaError("O setor está com limite de meia entrada.")
        
        if ingresso in self._ingressos_vendidos:
            raise ValueError("Esse ingresso já foi adicionado antes.")
        
        self._ingressos_vendidos.append(ingresso)

    def remover_ingresso(self, ingresso: Ingresso) -> None:
        if ingresso in self._ingressos_vendidos:
            self._ingressos_vendidos.remove(ingresso)
        else:
            raise IngressoNaoEncontradoError("O ingresso não foi encontrado.")

class Evento:
    def __init__(self, nome: str, local: str, data_hora: datetime) -> None:
        self.nome = nome
        self.local = local
        self.data_hora = data_hora
        self.setores: list[Setor] = []

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