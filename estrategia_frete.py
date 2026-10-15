# ---------------------------------------------------------------------------
# PASSO 1: A INTERFACE (STRATEGY)
# ---------------------------------------------------------------------------
# Este arquivo define o "contrato" que todo algoritmo de frete deve cumprir.
#
# No padrão Strategy, a Strategy é a abstração comum a todas as variações de um
# algoritmo. O contexto (a classe Pedido) só conhece ESTA abstração, nunca as
# classes concretas (FreteSedex, FretePac, etc.). É isso que permite adicionar
# novos fretes sem mexer no Pedido (Princípio Aberto/Fechado).

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# O import abaixo só serve para as "dicas de tipo" (type hints).
# TYPE_CHECKING é False em tempo de execução, então o import não acontece de
# verdade e evitamos um import circular (pedido.py também importa este arquivo).
if TYPE_CHECKING:
    from pedido import Pedido


class EstrategiaFrete(ABC):
    """Interface (classe abstrata) para qualquer cálculo de frete.

    Por herdar de ABC e usar @abstractmethod, não é possível instanciar
    EstrategiaFrete diretamente, nem uma subclasse que esqueça de implementar
    o método `calcular`. O Python avisa o erro na hora de criar o objeto.
    """

    @abstractmethod
    def calcular(self, pedido: Pedido) -> float:
        """Calcula e devolve o valor do frete (em reais) para o pedido dado.

        Recebe o próprio pedido para que cada estratégia possa ler os dados de
        que precisa (por exemplo, `pedido.peso_kg`) por meio das propriedades
        públicas, sem acessar atributos privados.
        """
        raise NotImplementedError
