# ---------------------------------------------------------------------------
# PASSO 2: AS ESTRATÉGIAS CONCRETAS
# ---------------------------------------------------------------------------
# Cada classe abaixo implementa UM algoritmo de frete. A lógica que antes ficava
# nos blocos if/elif da classe Pedido foi movida, sem alteração nas fórmulas,
# para o método `calcular` de cada classe.
#
# Vantagens:
#   - Cada classe tem uma única responsabilidade (um único cálculo).
#   - Mudar a regra do SEDEX não afeta PAC, Transportadora nem Motoboy.
#   - Todas respeitam o mesmo contrato (EstrategiaFrete), então o Pedido
#     trata todas do mesmo jeito (polimorfismo).

from estrategia_frete import EstrategiaFrete
from pedido import Pedido


class FreteSedex(EstrategiaFrete):
    """SEDEX: taxa base de R$ 10,00 + R$ 1,50 por kg."""

    def calcular(self, pedido: Pedido) -> float:
        return 10.0 + (pedido.peso_kg * 1.5)


class FretePac(EstrategiaFrete):
    """PAC: taxa base de R$ 5,00 + R$ 1,00 por kg."""

    def calcular(self, pedido: Pedido) -> float:
        return 5.0 + (pedido.peso_kg * 1.0)


class FreteTransportadora(EstrategiaFrete):
    """Transportadora: taxa base de R$ 20,00 + R$ 3,00 por kg."""

    def calcular(self, pedido: Pedido) -> float:
        return 20.0 + (pedido.peso_kg * 3.0)


class FreteMotoboy(EstrategiaFrete):
    """Motoboy: taxa fixa de R$ 15,00, independente do peso."""

    def calcular(self, pedido: Pedido) -> float:
        return 15.0
