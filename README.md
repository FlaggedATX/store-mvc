# Store MVC

> *Uma história de ambição, arquitetura, vibecoding e um estagiário muito azarado.*

---

## Parte 1: O Desenvolvedor

Era uma vez um desenvolvedor chamado **Gustavo**.

Gustavo tinha acabado de terminar um curso de engenharia de software. Ele sabia tudo sobre padrões de projeto. Sabia a diferença entre composição e agregação. Sabia quando usar Strategy, quando usar Builder, quando usar Decorator. Tinha lido o livro do GoF duas vezes. Tinha assistido palestras do Uncle Bob no YouTube às três da manhã com um caderno do lado.

O único problema era que Gustavo mal sabia Python.

Não que isso fosse um detalhe importante pra ele.

"Python é só uma ferramenta," ele dizia, acenando a mão com a autoridade de quem nunca debugou um `AttributeError` às sexta-feira às 17h58. "O que importa é a arquitetura."

Então um dia, cheio de entusiasmo e com uma xícara de café na mão esquerda e o Claude aberto na direita, Gustavo decidiu construir o projeto da sua vida: um sistema de gerenciamento de loja, do zero, com MVC limpo, múltiplos domínios, padrões de projeto aplicados com cirurgia e uma CLI digna de um terminal dos anos 80.

O plano era simples:

1. Pensar no problema
2. Modelar o domínio
3. Implementar com cuidado

O que Gustavo fez na prática:

1. Abrir o Claude
2. Digitar "faz um domínio de produto pra mim"
3. Repetir para cada domínio
4. Não testar nada
5. Commitar tudo como `feat: architecture done 🚀`

Gustavo vibecodeou domínio por domínio com a confiança de um arquiteto que nunca vai ver a construção cair. Cada conversa com o Claude era uma obra de arte. Cada classe gerada parecia perfeita isolada. O problema era que nenhuma delas conversava com a outra.

`from model.product import Product` funcionava no modelo.

`from product import Product` funcionava no controller.

`from .product import Product` funcionava em algum lugar misterioso que Gustavo nunca achou.

Mas Gustavo não se preocupou. "Vou resolver isso depois," ele disse, abrindo uma nova aba e pedindo pro Claude fazer o domínio de pagamento.

O processo de versionamento do Gustavo também merecia atenção especial. Ele sabia tudo sobre arquitetura de software, mas o conceito de controle de versão nunca tinha encaixado direito na cabeça dele. Git era "aquela coisa que os outros usavam". Na pasta do projeto, a história real estava nos nomes dos arquivos:

```
store-mvc-v1.zip
store-mvc-v1-FINAL.zip
store-mvc-v1-FINAL-revisado.zip
store-mvc-v2-ESSE.zip
store-mvc-v2-ESSE-corrigido.zip
store-mvc-v2-ESSE-corrigido-FUNCIONA.zip
store-mvc-v3-FINAL.zip
store-mvc-v3-FINAL-FINAL.zip
store-mvc-v3-FINAL-FINAL-agora-vai.zip
store-mvc-ENTREGA.zip
store-mvc-ENTREGA-real.zip
store-mvc-ENTREGA-real-DEFINITIVO.zip
store-mvc-ENTREGA-real-DEFINITIVO-v2.zip
```

A versão que você recebeu foi a `store-mvc-ENTREGA-real-DEFINITIVO-v2.zip`.

Ninguém sabe o que tinha na `v1`.

Três semanas depois de começar o projeto, a empresa passou por uma reestruturação.

Gustavo foi o primeiro a sair.

---

## Parte 2: O Estagiário

Na segunda-feira seguinte, **você** chegou no escritório achando que ia fazer café e organizar planilhas.

Em vez disso, seu gerente, **Rodrigo**, apareceu com um laptop embaixo do braço e uma expressão que misturava culpa com esperança.

---

**Rodrigo:** "Então... bom dia! Tudo bem? Você dormiu bem?"

**Você:** "Dormi, por que?"

**Rodrigo:** "Ótimo, ótimo. Porque você vai precisar de energia. Olha, sem rodeios: o Gustavo... foi redirecionado para outras oportunidades."

**Você:** "Foi demitido?"

**Rodrigo:** "Redirecionado. Anyway, ele deixou um projeto. Quase pronto, na verdade. Praticamente funcionando."

**Você:** "Praticamente?"

**Rodrigo:** "Sim. No sentido de que... os arquivos existem. Todos eles. Muito bem organizados, inclusive. Pastas com nomes bonitos, `__init__.py` em quase todo lugar..."

**Você:** "Em quase todo lugar?"

**Rodrigo:** "Bom. Em alguns lugares. Em lugares estratégicos. Você vai entender quando ver."

**Você:** "Rodrigo, o que exatamente eu preciso fazer?"

**Rodrigo:** "É simples! O sistema tem cinco domínios: identidade, produto, inventário, checkout e pagamento. Cada um tem model, view e controller. A arquitetura está linda, sério, o Gustavo tinha um talento real pra nomenclatura..."

**Você:** "Mas?"

**Rodrigo:** "Mas nada funciona."

**Você:** "..."

**Rodrigo:** "No sentido técnico de 'funciona'. Conceitualmente funciona muito bem."

**Você:** "Rodrigo."

**Rodrigo:** "Tá, tá. Tem alguns imports quebrados. E alguns métodos que estão declarados mas não implementados. E a CLI chama coisas que não existem ainda. E o Cart tem um bug que duplica produto em vez de somar quantidade. E o Payment não avança o status do Order. E..."

**Você:** "Para."

**Rodrigo:** "Mas o README vai ser incrível, eu garanto."

**Você:** "Não tem README."

**Rodrigo:** "Exatamente! Oportunidade de crescimento. Olha, você consegue, eu acredito em você. O Gustavo deixou comentários em tudo."

**Você:** "Que tipo de comentários?"

**Rodrigo:** *(abre o laptop e aponta pra tela)*

```python
# TODO: fazer isso funcionar
```

**Você:** "..."

**Rodrigo:** "Em doze arquivos diferentes."

**Você:** "Vou precisar de mais café."

**Rodrigo:** "Já pedi dois. Chega em dez minutos. Ah, e o prazo é sexta-feira."

**Você:** "Essa sexta-feira?"

**Rodrigo:** "A mais próxima possível, digamos assim."

---

## Parte 3: O Projeto

Você abriu o repositório.

A estrutura era, de fato, bonita. Cinco domínios bem separados. Models, views, controllers, cada um no seu lugar. Até os nomes das classes faziam sentido.

O problema era o resto.

Imports usando caminho absoluto em uns arquivos, relativo em outros, e nenhum nos `__init__.py` que precisavam. Métodos que o controller chamava mas o model não tinha. Validações que simplesmente não existiam, porque o Gustavo confiava que "o usuário vai colocar coisa certa."

E no meio de tudo isso, uma arquitetura genuinamente boa.

Strategy pra precificação. Builder pra plano de reserva. Value objects imutáveis. Separação de responsabilidade razoavelmente honesta entre camadas.

O Gustavo não era burro. Ele só tinha pulado a parte de *fazer funcionar*.

Sua missão agora é essa: pegar o que ele deixou, entender cada decisão de design, e completar o que está faltando.

---

## O que está quebrado (e por que)

### Imports

O Gustavo misturou três estilos de import no mesmo projeto. Sua tarefa é padronizar tudo usando o caminho completo a partir da raiz:

```python
# errado (caminho relativo sem contexto)
from product import Product

# errado (relativo dentro de pacote errado)
from .product import Product

# certo (absoluto a partir da raiz do projeto)
from model.product import Product
```

### Validações ausentes

O sistema não valida nada. Um `Price` negativo passa sem erro. Um `SKU` vazio é aceito. Um `Cart` aceita quantidade zero. Você precisa adicionar essas guardas nos lugares certos.

### Métodos não implementados

Alguns métodos estão declarados mas só têm `pass` ou retornam `None` sem fazer nada. Procure pelos comentários `# TODO` e complete cada um.

### `__init__.py` faltando

Alguns subpacotes de `controller/` e `view/` não têm `__init__.py`. Python não consegue importar de um diretório que não é reconhecido como pacote.

---

## Como rodar

```bash
# limpar cache antes de testar
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete

# rodar
python app.py
```

---

## Estrutura do projeto

```
store-mvc/
├── app.py                          # ponto de entrada
├── model/
│   ├── identity/                   # Person, Customer, Address, Contact
│   ├── product/                    # Product, SKU, Price, PricingPolicy
│   ├── inventory/                  # Aisle, Shelf, StockItem
│   ├── checkout/                   # Cart, LineItem, Order, OrderStatus
│   └── payment/                    # Payment, Cash, Card, Pix, Receipt
├── view/
│   ├── identity/                   # CustomerView
│   ├── product/                    # ProductView (tabela!)
│   ├── inventory/                  # InventoryView
│   ├── checkout/                   # CheckoutView (tabela de orders!)
│   └── payment/                    # PaymentView
├── controller/
│   ├── identity/                   # CustomerController
│   ├── product/                    # ProductController
│   ├── inventory/                  # InventoryController
│   ├── checkout/                   # CheckoutController
│   └── payment/                    # PaymentController
└
```

---

## Padrões usados

| Padrão | Onde | Por que |
|--------|------|---------|
| Strategy | `Quarto`, `PricingPolicy` | algoritmo de preço intercambiável |
| Value Object | `SKU`, `Price`, `Address`, `Contact`, `Receipt` | imutabilidade, sem identidade própria |
| MVC | toda a aplicação | separação entre dado, exibição e controle |

---

## Fluxos

Além de adicionar validações ao código, Rodrigo te deu uma meta mais concreta. Desenvolva os seguintes fluxos!

```
customer_flow -> login/cadastro, browsing, carrinho, checkout, pagamento
manager_flow -> cadastrar produto, estocar, política de preço, relatório
fulfillment_flow -> listar orders, avançar status
```

---

## Boa sorte

O Gustavo acreditava em você.

Bom, ele não sabia que você existia. Mas se soubesse, acreditaria.

Provavelmente.