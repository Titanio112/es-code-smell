# ---------------------------------------------------------------------------
# TESTES AUTOMATIZADOS
# ---------------------------------------------------------------------------
# Garantem que a refatoração para o padrão Strategy manteve exatamente os
# mesmos valores de frete da versão original e que os casos de erro funcionam.
#
# Como rodar:  python -m unittest -v

import unittest

from estrategia_frete import EstrategiaFrete
from frete_drone import FreteDrone
from fretes import FreteMotoboy, FretePac, FreteSedex, FreteTransportadora
from pedido import Pedido


class TestFretesConcretos(unittest.TestCase):
    """Cada estratégia deve reproduzir a fórmula original do if/elif."""

    def setUp(self):
        # Pedido de 2,5 kg usado na maioria dos testes.
        self.pedido = Pedido(peso_kg=2.5)

    def _frete(self, estrategia: EstrategiaFrete) -> float:
        # Mesmo fluxo do cliente: injeta a estratégia e calcula.
        self.pedido.set_estrategia(estrategia)
        return self.pedido.calcular_frete()

    def test_sedex(self):
        # 10,00 + 2,5 * 1,50 = 13,75
        self.assertAlmostEqual(self._frete(FreteSedex()), 13.75)

    def test_pac(self):
        # 5,00 + 2,5 * 1,00 = 7,50
        self.assertAlmostEqual(self._frete(FretePac()), 7.50)

    def test_transportadora(self):
        # 20,00 + 2,5 * 3,00 = 27,50
        self.assertAlmostEqual(self._frete(FreteTransportadora()), 27.50)

    def test_motoboy_taxa_fixa(self):
        self.assertAlmostEqual(self._frete(FreteMotoboy()), 15.0)

    def test_drone_taxa_fixa(self):
        # Novo requisito: criado sem alterar a classe Pedido.
        self.assertAlmostEqual(self._frete(FreteDrone()), 25.0)

    def test_taxa_fixa_ignora_o_peso(self):
        pesado = Pedido(peso_kg=100.0)
        pesado.set_estrategia(FreteDrone())
        self.assertAlmostEqual(pesado.calcular_frete(), 25.0)

    def test_frete_proporcional_ao_peso(self):
        pedido = Pedido(peso_kg=10.0)
        pedido.set_estrategia(FretePac())
        # 5,00 + 10 * 1,00 = 15,00
        self.assertAlmostEqual(pedido.calcular_frete(), 15.0)


class TestContextoPedido(unittest.TestCase):
    """Comportamento da classe Pedido (o Contexto do Strategy)."""

    def test_troca_de_estrategia_em_tempo_de_execucao(self):
        pedido = Pedido(peso_kg=2.5)
        pedido.set_estrategia(FreteSedex())
        self.assertAlmostEqual(pedido.calcular_frete(), 13.75)
        pedido.set_estrategia(FreteDrone())
        self.assertAlmostEqual(pedido.calcular_frete(), 25.0)

    def test_sem_estrategia_levanta_erro_claro(self):
        with self.assertRaises(ValueError):
            Pedido(peso_kg=1.0).calcular_frete()

    def test_interface_nao_pode_ser_instanciada(self):
        with self.assertRaises(TypeError):
            EstrategiaFrete()

    def test_estrategia_sem_calcular_nao_pode_ser_instanciada(self):
        class FreteIncompleto(EstrategiaFrete):
            pass

        with self.assertRaises(TypeError):
            FreteIncompleto()

    def test_estrategia_customizada_funciona_sem_alterar_pedido(self):
        # Prova do Aberto/Fechado: uma estratégia nova, definida só aqui,
        # funciona com o Pedido exatamente como está.
        class FreteRetiradaLocal(EstrategiaFrete):
            def calcular(self, pedido: Pedido) -> float:
                return 0.0

        pedido = Pedido(peso_kg=5.0)
        pedido.set_estrategia(FreteRetiradaLocal())
        self.assertEqual(pedido.calcular_frete(), 0.0)


if __name__ == "__main__":
    unittest.main()
