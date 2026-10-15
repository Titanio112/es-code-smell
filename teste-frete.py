# ---------------------------------------------------------------------------
# PASSO 4: O CLIENTE (main)
# ---------------------------------------------------------------------------
# O cliente agora é o responsável por ESCOLHER e "injetar" a estratégia no
# pedido antes de calcular o frete (injeção de dependência via setter).
# Quem decide qual algoritmo usar é o cliente. O Pedido só executa.

from pedido import Pedido
from fretes import FreteSedex, FretePac, FreteTransportadora, FreteMotoboy
from frete_drone import FreteDrone  # PASSO 5: nova estratégia, arquivo novo


def main():
    print("*" * 30)
    print("Executando Versão Refatorada (Strategy)")
    print("*" * 30)

    pedido = Pedido(peso_kg=2.5)

    # Para cada serviço: 1) injeta a estratégia  2) chama calcular_frete()
    pedido.set_estrategia(FreteSedex())
    print(f"Valor do frete SEDEX: R$ {pedido.calcular_frete():.2f}")

    pedido.set_estrategia(FretePac())
    print(f"Valor do frete PAC: R$ {pedido.calcular_frete():.2f}")

    pedido.set_estrategia(FreteTransportadora())
    print(f"Valor do frete TRANSPORTADORA: R$ {pedido.calcular_frete():.2f}")

    pedido.set_estrategia(FreteMotoboy())
    print(f"Valor do frete MOTOBOY: R$ {pedido.calcular_frete():.2f}")

    # PASSO 5: o novo frete funciona sem nenhuma alteração na classe Pedido.
    pedido.set_estrategia(FreteDrone())
    print(f"Valor do frete DRONE: R$ {pedido.calcular_frete():.2f}")

    # Segundo pedido, com outro peso. (Na versão original o código criava
    # "pedido2" mas calculava em "pedido", o que era um bug de digitação.)
    pedido2 = Pedido(peso_kg=10.0)
    pedido2.set_estrategia(FretePac())
    print(f"Valor do frete PAC (pedido de 10 kg): R$ {pedido2.calcular_frete():.2f}")

    # Troca de estratégia em tempo de execução no mesmo pedido.
    pedido2.set_estrategia(FreteDrone())
    print(f"Valor do frete DRONE (pedido de 10 kg): R$ {pedido2.calcular_frete():.2f}")


# Ponto de entrada para execução
if __name__ == "__main__":
    main()
