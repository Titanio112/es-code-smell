# ---------------------------------------------------------------------------
# PASSO 5: TESTE DE EXTENSIBILIDADE (novo requisito: frete por DRONE)
# ---------------------------------------------------------------------------
# O gerente de produto pediu o frete por drone com taxa fixa de R$ 25,00.
#
# Para atender o pedido, foi preciso APENAS criar esta nova classe, em um
# arquivo novo. Nenhuma linha de Pedido, EstrategiaFrete ou das outras
# estratégias foi alterada. Isso é o Princípio Aberto/Fechado na prática:
# o sistema está ABERTO para extensão e FECHADO para modificação.

from estrategia_frete import EstrategiaFrete
from pedido import Pedido


class FreteDrone(EstrategiaFrete):
    """Drone: taxa fixa de R$ 25,00, independente do peso."""

    def calcular(self, pedido: Pedido) -> float:
        return 25.0
