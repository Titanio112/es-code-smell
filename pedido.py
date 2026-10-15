# Representa um pedido em um sistema de comércio eletrônico.
#
# PASSO 3: A CLASSE PEDIDO COMO "CONTEXTO" DO PADRÃO STRATEGY
# ---------------------------------------------------------------------------
# Antes: o Pedido sabia COMO calcular cada tipo de frete (cadeia de if/elif).
#        Todo novo frete obrigava a reabrir e modificar esta classe.
# Agora: o Pedido apenas guarda uma estratégia de frete e DELEGA o cálculo a
#        ela. Ele não sabe qual frete está usando nem como ele funciona.
#        Novos fretes viram novas classes e esta classe nunca mais muda.

from estrategia_frete import EstrategiaFrete


class Pedido:

    def __init__(self, peso_kg: float):
        self._peso_kg = peso_kg

        # Atributo PRIVADO (convenção do Python: prefixo "_") que guarda a
        # estratégia de frete atual. Começa vazio (None) porque o cliente
        # ainda não escolheu o serviço. A escolha é feita depois, por meio
        # do método set_estrategia().
        self._estrategia: EstrategiaFrete | None = None

    # SETTER público: é por aqui que o cliente "injeta" a estratégia desejada.
    # O tipo esperado é a abstração EstrategiaFrete, então qualquer frete
    # (existente ou futuro) é aceito sem alterar este método.
    # Como a troca é feita em tempo de execução, o mesmo pedido pode ter o
    # frete recalculado com outro serviço simplesmente chamando o setter de novo.
    def set_estrategia(self, estrategia: EstrategiaFrete) -> None:
        self._estrategia = estrategia

    # Método que substitui o antigo calcular_frete(tipo_servico: str).
    # Repare que não recebe mais parâmetros nem tem if/elif: apenas delega o
    # cálculo à estratégia, passando a si mesmo (self) para que ela possa ler
    # os dados do pedido (como o peso) pelas propriedades públicas.
    def calcular_frete(self) -> float:
        # Proteção: se ninguém definiu a estratégia, falhamos com uma mensagem
        # clara em vez de um erro confuso de "NoneType has no attribute...".
        if self._estrategia is None:
            raise ValueError(
                "Nenhuma estratégia de frete definida. "
                "Use set_estrategia() antes de calcular_frete()."
            )
        return self._estrategia.calcular(self)

    # Propriedades (get's) para acesso seguro aos atributos.
    # As estratégias usam esta propriedade para ler o peso sem mexer no
    # atributo privado _peso_kg diretamente (encapsulamento).
    @property
    def peso_kg(self) -> float:
        return self._peso_kg
