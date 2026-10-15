# 📦 Cálculo de Frete com o Padrão Strategy

Refatoração de um *code smell* em Python: a cadeia de `if/elif` do cálculo de frete deu lugar ao **padrão Strategy**, seguindo o **Princípio Aberto/Fechado (OCP)**.

> Atividade de sala de aula invertida de **Engenharia de Software**
> Bacharelado em Sistemas de Informação, CEFET-MG (4º período)
> Feito por **Antônio** ([@Titanio112](https://github.com/Titanio112))

---

## 🐛 O problema

Na versão original, a classe `Pedido` conhecia **todos** os tipos de frete:

- Cada novo serviço (ex.: `DRONE`) obrigava a **abrir e modificar** o `Pedido`
- Risco de quebrar fretes que já funcionavam
- Classe "pronta" que nunca ficava realmente pronta

## ✅ A solução

O `Pedido` agora só **delega** o cálculo para uma estratégia. Cada frete vive na sua própria classe.

```
        ┌──────────────────┐
        │  EstrategiaFrete │  ← interface (ABC)
        └────────▲─────────┘
                 │ implementam
   ┌─────────┬───┴─────┬──────────────┬──────────┬─────────┐
FreteSedex FretePac FreteTransportadora FreteMotoboy FreteDrone
                                                       (novo!)

Pedido ──usa──▶ EstrategiaFrete
```

## 🗂️ Estrutura

| Arquivo | O que faz |
|---|---|
| `estrategia_frete.py` | Interface `EstrategiaFrete` com o método `calcular(pedido)` |
| `fretes.py` | Estratégias: `FreteSedex`, `FretePac`, `FreteTransportadora`, `FreteMotoboy` |
| `frete_drone.py` | `FreteDrone`, criado **sem tocar** no `Pedido` |
| `pedido.py` | Contexto: guarda a estratégia e delega o cálculo |
| `teste-frete.py` | Cliente que injeta a estratégia e imprime os valores |

## 💸 Regras de frete

| Serviço | Fórmula |
|---|---|
| SEDEX | R$ 10,00 + R$ 1,50 por kg |
| PAC | R$ 5,00 + R$ 1,00 por kg |
| Transportadora | R$ 20,00 + R$ 3,00 por kg |
| Motoboy | R$ 15,00 fixo |
| Drone | R$ 25,00 fixo |

## ▶️ Como rodar

Precisa de Python 3.10 ou superior.

```bash
python teste-frete.py
```

## 💡 Como usar no seu código

```python
from pedido import Pedido
from fretes import FreteSedex

pedido = Pedido(peso_kg=2.5)
pedido.set_estrategia(FreteSedex())
print(pedido.calcular_frete())  # 13.75
```

## ➕ Como adicionar um novo frete

Só é preciso **criar uma classe nova**. Nada mais muda:

```python
from estrategia_frete import EstrategiaFrete

class FreteRetiradaLocal(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 0.0
```

É isso que o Aberto/Fechado quer dizer: **aberto para extensão, fechado para modificação**.

---

📚 Referência: [Strategy no Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/strategy)
🍴 Fork de [brunoacre/es-code-smell](https://github.com/brunoacre/es-code-smell)
