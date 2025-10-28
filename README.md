# Entrevistas Técnicas de Processos seletivos

Resumo de conhecimento essencial e obrigatório para arrasar em entrevistas técnicas


## Motivação

Praticamente todo processo seletivo de desenvolvedores tem uma fase de entrevista técnica. Nela, o candidato precisa programar ao vivo para demonstrar seu conhecimento. Por isso, é necessário afiar o machado para causar uma boa impressão na entrevista.

A grande motivação deste repositório é apresentar um resumo geral desse conhecimento.

Os exemplos aqui são códigos Python válidos. Mas os conceitos se aplicam a qualquer linguagem de programação.

Seguem os conhecimentos essenciais.

## Estruturas de dados lineares

As entrevistas técnicas costumam durar apenas uma hora. Por isso, é raro cairem questões envolvendo estruturas complexas, como árvores e grafos. Devemos focar no conhecimento profundo de estruturas de dados lineares. São elas:

1. Lista (List) ou Vetor (Vector)
2. Lista Duplamente Ligada (Double Linked List - Deque)
3. Conjunto (Set)
4. Dicionário (Dict) ou Mapa (Map)

A primeira camada é saber quais problemas podemos resolver com essas estruturas de forma simples e eficiente. Mais importante ainda é saber quando não utilizar essas estruturas. Segue resumo de cada uma:

### Lista (List) ou Vetor (Vector)

São estruturas de dados contíguas extremamente eficientes para leitura de dados por índice. Também são extremamente eficientes para adição e remoção de elementos em seu final. São excelentes implementações de pilhas.

Costumam ser muito utilizadas em problemas que envolvem ordenação de dados, de forma direta ou indireta. São eficientes para obter o tamanho de uma lista e também para trocar um elemento por outro. Seguem as operações eficientes:

```python

>>> lista = list(range(1, 10))  # Criação da lista
>>> lista # Lista com 9 elementos contíguos
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista[0] # Acesso eficiente a primeiro elemento
1
>>> lista[1] # Acesso eficiente a segundo elemento
2
>>> lista[-1] # Acesso eficiente ao último elemento
9
>>> lista.append(10) # Adicionando elemento 10 ao final de forma eficiente
>>> lista # Confira elemento adicionado ao final
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> lista.pop() # Removendo último elemento de forma eficiente, inclusive tem nome pop, igual ao definido para uma pilha
10
>>> lista # Confira elemento removido do final
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(lista) # Obtendo tamanho da lista
9
>>> lista[1] = -1 # Alterando segundo elemento de forma eficiente
>>> lista # Confira novo segundo elemento
[1, -1, 3, 4, 5, 6, 7, 8, 9]

```

#### Quando não utilizar Lista (List) ou Vetor (Vector)

Essas estruturas são ineficientes para inserções de elementos em seu início ou meio. Por isso não devem ser usadas em problemas que precisam de filas. Exemplo de operações ineficientes:

```python
>>> lista = list(range(1, 10))  # Criação da lista
>>> lista # Lista com 9 elementos contíguos
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista.pop(0) # Removendo primeiro elemento de forma ineficiente, quanto maior a lista, mais tempo demora
1
>>> lista # Lista com primeiro elemento removido
[2, 3, 4, 5, 6, 7, 8, 9]
>>> lista.pop(3) # Removendo elemento no meio de forma ineficiente, quanto maior a lista, mais tempo demora
5
>>> lista # Lista com primeiro elemento removido
[2, 3, 4, 6, 7, 8, 9]
>>> lista.insert(0, 1) # Inserindo elemento no início de forma ineficiente, quanto maior a lista, mais tempo demora
>>> lista # Lista com primeiro elemento inserido
[1, 2, 3, 4, 6, 7, 8, 9]

```

Então, para os casos em que se precisa de uma fila, melhor usar uma lista duplamente ligada. Confira na próxima seção.

### Lista Duplamente Ligada (Double Linked List - Deque)

São estruturas parecidas com a lista. Mas permitem remoção e inserção eficiente tanto no inĩ́cio quando em fim. 
Por isso são recomendadas em problemas que exigem fila. Confira as operações iguais as das lista que são eficientes:

```python
>>> from collections import deque
>>> lista = deque(range(1, 10))  # Criação da lista
>>> lista # Lista com 9 elementos contíguos
deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> lista.popleft() # Removendo primeiro elemento de forma eficiente
1
>>> lista # Lista com primeiro elemento removido
deque([2, 3, 4, 5, 6, 7, 8, 9])
>>> lista.appendleft(1) # Inserindo elemento no início de forma eficiente
>>> lista # Lista com primeiro elemento inserido
deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> lista.pop() # Também eficiente para remoção do fim da lista
9
>>> lista # Lista com último elemento removido
deque([1, 2, 3, 4, 5, 6, 7, 8])
>>> lista.append(9) # Também eficiente para inserção no fim da lista
>>> lista # Lista com último elemento adicionado
deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

```

#### Quando não usar Lista Duplamente Ligada (Double Linked List - Deque)
A lista duplamente ligada não é eficiente para acesso a elementos próximos ao seu meio. Para esses casos, é melhor usar listas.

```python
>>> from collections import deque
>>> lista = deque(range(1, 10))  # Criação da lista
>>> lista[4] # Acesso a elemento do meio de forma ineficiente. Quando maior a lista, mais tempo demora
5

```

Por fim, existe uma operação ineficiente para listas duplamente ligadas e listas comuns, confira a seguir.

#### Quando não usar Lista comum ou Duplamente Ligada

Ambas listas, a comum e a duplamente ligada, são ineficientes para a operação de pertencimento. 
Ou seja, para chegar se um elemento está contido nela ou não. Confira a seguir:

```python
>>> from collections import deque
>>> d = deque(range(1, 10))  # Criação da lista duplamente ligada
>>> d # Lista com 9 elementos contíguos
deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> 9 in d # operação ineficiente de elemento que está contido na lista
True
>>> 10 in d # operação ineficiente de elemento que não está contido na lista
False
>>> lista = list(d)  # Criação da lista simples
>>> lista # Lista com 9 elementos contíguos
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 9 in lista # operação ineficiente de elemento que está contido na lista
True
>>> 10 in lista # operação ineficiente de elemento que não está contido na lista
False

```

É muito comum existirem problemas onde é necessário manter a memória de passos já realizados (backtrack). Para esses casos, deve se
evitar usar listas. Nesse caso, melhor usar conjuntos, confira a seguir.

### Conjunto (Set)

Conjuntos, também chamados de hash sets em algumas liguagens, são muito eficientes para remoção e adição de elementos.
São também extremamente rápidos para operação de pertencimento de elementos.
Eles são parecidos com os conjuntos estudados em matemática e por isso não permitem elementos repetidos. 
Confira as operações eficientes:

```python
>>> conjunto = set() # Criação de conjunto vazio
>>> conjunto
set()
>>> 1 in conjunto # Operação de pertencimento é eficiente
False
>>> conjunto.add(1) # Adição de elementos é eficiente
>>> conjunto
{1}
>>> 1 in conjunto
True
>>> conjunto.update(range(10)) # Adiição de múltiplos elementos é eficiente e não permite duplicatas, só possui "1" uma vez
>>> conjunto
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> conjunto.add(1)  # Mesmo com adição de elemento, não permite repetição
>>> conjunto
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> 1 in conjunto
True
>>> conjunto.remove(1) # Eficiente para remoção de elementos
>>> conjunto
{0, 2, 3, 4, 5, 6, 7, 8, 9}

```

Apesar de conjuntos serem excelentes para se manter backtracking, não permitem acesso a elementos por índices.

#### Quando não usar conjuntos

Conjuntos não são ordenados em muitas linguagens. Por isso não permite acesso por índice. 
Por isso devem ser evitados em problemas de acesso a elementos contíguos ou com ordenação. Confira:

```python
>>> conjunto =set(range(5))
>>> conjunto
{0, 1, 2, 3, 4}
>>> conjunto[0] # Não permite acesso por índice
Traceback (most recent call last):
  ...
TypeError: 'set' object is not subscriptable
>>> for elemento in conjunto: print(elemento) # Mas é possível iterar sobre os elementos
0
1
2
3
4

```

Algumas vezes precisamos conectar elementos a respectivos valores e o conjunto não resolve esse problema. 
Para esse caso devemos usar dicionários, confira a seguir.

### Dicionário (Dict) ou Mapa (Map)

Dicionários, também chamados de mapas ou hash maps, servem para conectar elementos únicos (chaves) a valores.
Em termos de eficiencia de operações, funcionam exatamente como conjuntos, confira a seguir:

```python
>>> frutas ={'banana': 12.50, 'laranja': 1.50, 'uva': 1.20} # Criação de dicionário
>>> frutas['banana'] # Acesso a elemento de forma eficiente, retornando respectivo preço
12.5
>>> frutas['laranja']
1.5
>>> frutas['uva']
1.2
>>> frutas['abacaxi'] = 2.50 # Adicionando elemento de forma eficiente
>>> frutas
{'banana': 12.5, 'laranja': 1.5, 'uva': 1.2, 'abacaxi': 2.5}
>>> frutas['abacaxi'] = 3.75 # alterando valor de forma eficiente
>>> frutas
{'banana': 12.5, 'laranja': 1.5, 'uva': 1.2, 'abacaxi': 3.75}
>>> del frutas['abacaxi'] # Removendo elemento de forma eficiente}
>>> frutas
{'banana': 12.5, 'laranja': 1.5, 'uva': 1.2}

```
Como são parecidos com conjuntos, os casos onde dicionários não devem ser usados são parecidos. Confira a seguir.

#### Quando não usar dicionários

Dicionários não são ordenados em muitas linguagens. Por isso não permite acesso por índice. 
Por isso devem ser evitados em problemas de acesso a elementos contíguos ou com ordenação. Confira:

```python
>>> frutas ={'banana': 12.50, 'laranja': 1.50, 'uva': 1.20}
>>> frutas[0] # Não é possível acessar por índice, retorna erro
Traceback (most recent call last):
  ...
KeyError: 0
>>> for nome in frutas: print(nome) # Mas é possível iterar por chaves de forma eficiente
banana
laranja
uva
>>> for preco in frutas.values(): print(preco) # Também possível iterar por valores de forma eficiente
12.5
1.5
1.2
>>> for nome,preco in frutas.items(): print(nome, preco) # Também útil iterar por chave e valor de forma eficiente
banana 12.5
laranja 1.5
uva 1.2

```

Assim se encerram as estruturas de dados lineares necessárias para resolver 99% das questões de entrevistas técnicas.

### Conclusão sobre estruturas de dados lineares

Conhecer as quatro estruturas de dados lineares elementares é fundamental para passar nas entrevistas técnicas de processos seletivos para desenvolvedores. Saber escolher a estrutura de dados mais adequada para um problema é essencial para demonstrar conhecimento dos fundamentos.

Esse conhecimento já deve fazer o profissional passar em várias entrevistas para empresas médias e pequenas.

Se pretendemos trabalhar em grandes empresas, principalmente as do exterior ou americanas, como Google e Facebook, precisamos ir além. Precisamos conhecer e analisar nossos algoritmos do ponto de vista de complexidade em tempo de execução e memória. Veja o resumo desse assunto na próxima seção.

## Análise e Complexidade de Algoritmos

Análise de complexidade de tempo de execução e uso de memória é uma matéria de faculdade. Muitas vezes só é vista na pós-graduação, no Brasil. Contudo essa matéria é dada na graduação das faculdades americanas.

Saber fazer essa análise é indispensável para quem quer fazer processos seletivos de empresas grandes, como Google e Facebook.

Não precisamos ter um conhecimento profundo. Mas precisamos conseguir fazer essa análise rapidamente e visualmente na hora do processo seletivo.

Além disso, precisamos saber usar a análise para buscar soluções eficientes. A heurística que funciona é:

1. Validamos que entendemos os requisitos dos problemas, incluindo natureza de entradas e saídas dos programas
2. Fazemos a solução mais simples possível, mesmo que ineficiente. Não resolver é pior que implementar solução ineficiente
3. Analisamos a complexidade da solução
4. Verificamos como melhorar a performance, como por exemplo, ordenar as entradas do programa
5. Implementamos a melhora de performance proposta

Para poder fazer essa análise e heurística, precisamos:

1. Saber as 7 principais funções de análise e complexidade
2. Saber comparar cada uma dessas funções em termos de performance
3. Saber a complexidade das operações das estruturas lineares
4. Conhecer e saber a complexidade dos algoritmos clássicos de soluções de problemas

Vamos detalhar cada um desses pontos.

### As 7 funções de análise e complexidade de algorítmos

Em análise e complexidade de algorítmos usando se usa a notação [Big O](https://en.wikipedia.org/wiki/Big_O_notation) para expressar a evolução do tempo de execução e uso de memória de algoritmos.
Você só precisa conhecer 7 dessas funções

#### 1. O(1) - Constante

Algorítmos de tempo de constante são aqueles em que tempo de execução e memória independem do tamanho da entrada.
Ou seja, mesmo para uma lista grande de elementos, o algorítmo vai demorar sempre o mesmo tempo para executar.
Esse tipo de algorítmo é o mais eficiente que existe, mas normalmente apenas problemas muito simples permitem solução constante.
Segue uma tabela com as principais operações de tempo constante:

| Categoria             | Operação | Descrição | Exemplo                             |
|-----------------------|----------|-----------|-------------------------------------|
| **Operações Básicas** | Atribuição de variável | Armazenar valor em variável | `x = 5`                             |
| **Operações Básicas** | Operações aritméticas | Soma, subtração, multiplicação, divisão | `a + b`, `x - y`, `m * n`, `p / q`  |
| **Operações Básicas** | Operações lógicas | AND, OR, NOT, comparações | `a and b`, `x > y`, `not flag`      |
| **Operações Básicas** | Acesso a atributo | Acessar propriedade de objeto | `obj.propriedade`                   |
| **Lista (List)**      | Acesso por índice | Ler elemento em posição específica | `lista[0]`, `lista[5]`, `lista[-1]` |
| **Lista (List)**      | Modificação por índice | Alterar elemento em posição específica | `lista[1] = -1`                     |
| **Lista (List)**      | Adicionar ao final | Inserir elemento no fim da lista | `lista.append(10)`                  |
| **Lista (List)**      | Remover do final | Retirar último elemento | `lista.pop()`                       |
| **Lista (List)**      | Obter tamanho | Quantidade de elementos | `len(lista)`                        |
| **Deque**             | Adicionar ao final | Inserir elemento no fim | `deque.append(9)`                   |
| **Deque**             | Remover do final | Retirar último elemento | `deque.pop()`                       |
| **Deque**             | Adicionar ao início | Inserir elemento no começo | `deque.appendleft(1)`               |
| **Deque**             | Remover do início | Retirar primeiro elemento | `deque.popleft()`                   |
| **Deque**             | Obter tamanho  | Quantidade de elementos | `len(deque)`                        |
| **Set**               | Adicionar elemento | Inserir novo elemento | `conjunto.add(1)`                   |
| **Set**               | Remover elemento | Retirar elemento específico | `conjunto.remove(1)`                |
| **Set**               | Verificar pertencimento | Checar se elemento existe | `1 in conjunto`                     |
| **Set**               | Obter tamanho  | Quantidade de elementos | `len(conjunto)`                     |
| **Dict**              | Acesso por chave | Obter valor associado à chave | `dict['chave']`                     |
| **Dict**              | Modificação por chave | Alterar valor de chave existente | `dict['chave'] = novo_valor`        |
| **Dict**              | Adicionar par chave-valor | Inserir nova entrada | `dict['nova_chave'] = valor`        |
| **Dict**              | Remover por chave | Excluir entrada específica | `del dict['chave']`                 |
| **Dict**              | Verificar existência de chave | Checar se chave existe | `'chave' in dict`                   |
| **Dict**              | Obter tamanho  | Quantidade de elementos | `len(dct)`                          |

Portanto devemos ser capazes de identificar as operações de tempo constante de nosso algoritmo. Devemos procurar usar as estruturas de dados lineares mais adequadas, buscando operações constantes sempre que possível.

Quando não for possível, procuramos usar a próxima solução mais eficiente, que é a logarítmica. Confira a seguir.

#### 2. O(log n) - Logarítmico

Os algorítmos logaritmicos são os mais eficientes depois dos constantes. 
Normalmente são logarítimocos os algorítmos que conseguem dividir a entrada em duas partes e, a partir de uma condição, eliminar uma das metades como possível solução.
O mais clássico algoritimo em complexidade logaritímica é a [Busca Binária](https://en.wikipedia.org/wiki/Binary_search).

Conhecer esse algorítmo é importante para poder buscar soluções com eficiencia e até validar com o entrevistador se as condições para usar o algoritmo estão presentes.
Por exemplo, se a entrada for uma lista de números, você pode perguntar se ela está ordenada para já poder efetuar uma busca binária.
Você pode ser pedido para implementar o algoritmo de busca binária. 
Ou então pode usar implementação da linguagem que estiver usando, pois a maioria vai oferecer a solução pronta.
E aí vc vai considerar a complexidade log n do algorítmo.

Exemplo em Python

```python
>>> from bisect import bisect_left, bisect_right
>>> lista= list(range(1, 20, 3))
>>> lista
[1, 4, 7, 10, 13, 16, 19]
>>> bisect_left(lista, 10) # onde inserir o 10, na posição mais a esquerda, para manter a lista ordenada, custo O(log n)
3
>>> bisect_right(lista, 10) # onde inserir o 10, na posição mais a direita, para manter a lista ordenada, custo O(log n)
4

```

Mas algumas vezes não é possĩvel chegar em algorítmicos logaritimicos.
Isso acontece quando existe a necessidade de iterar por todos elementos da lista da entrada.
Nesse caso, a solução mais eficiente é a liner, confira a seguir.

#### 3. O(n) - Linear

Algorítmos lineares normalmente exigem a iteração em todos elementos da entrada, por isso o tempo de execução fica proporcional ao tamanho da entrada.

Dentre as estruturas de dados lineares mencionadas, as seguintes operações são lineares, além de outras operaçoes básicas:

| Categoria             | Operação | Descrição | Exemplo                             |
|-----------------------|----------|-----------|-------------------------------------|
| **Operações Gerais**  | Iteração completa | Percorrer todos os elementos | `for x in lista`, `for x in conjunto` |
| **Operações Gerais**  | Conversão para lista | Transformar estrutura em lista | `list(conjunto)`, `list(dict.keys())` |
| **Operações Gerais**  | Conversão para string | Transformar estrutura em string | `str(lista)`, `' '.join(lista)` |
| **Lista (List)**      | Verificar pertencimento | Checar se elemento existe | `x in lista`, `elemento in lista` |
| **Lista (List)**      | Buscar índice | Encontrar posição de elemento | `lista.index(elemento)` |
| **Lista (List)**      | Contar ocorrências | Quantas vezes elemento aparece | `lista.count(elemento)` |
| **Lista (List)**      | Inserir no início/meio | Adicionar elemento em posição específica | `lista.insert(0, elemento)` |
| **Lista (List)**      | Remover do início/meio | Retirar elemento de posição específica | `lista.pop(0)`, `lista.remove(elemento)` |
| **Lista (List)**      | Encontrar mínimo | Menor elemento da lista | `min(lista)` |
| **Lista (List)**      | Encontrar máximo | Maior elemento da lista | `max(lista)` |
| **Lista (List)**      | Somar elementos | Soma de todos os elementos | `sum(lista)` |
| **Lista (List)**      | Reverter | Inverter ordem dos elementos | `lista.reverse()`, `lista[::-1]` |
| **Deque**             | Verificar pertencimento | Checar se elemento existe | `x in deque` |
| **Deque**             | Acesso por índice (meio) | Acessar elemento no meio | `deque[len(deque)//2]` |
| **Deque**             | Inserir no meio | Adicionar elemento em posição específica | `deque.insert(pos, elemento)` |
| **Deque**             | Remover do meio | Retirar elemento de posição específica | `deque.remove(elemento)` |
| **Deque**             | Encontrar mínimo | Menor elemento do deque | `min(deque)` |
| **Deque**             | Encontrar máximo | Maior elemento do deque | `max(deque)` |
| **Set**               | Iteração completa | Percorrer todos os elementos | `for elemento in conjunto` |
| **Set**               | Encontrar mínimo | Menor elemento do conjunto | `min(conjunto)` |
| **Set**               | Encontrar máximo | Maior elemento do conjunto | `max(conjunto)` |
| **Set**               | Operações de conjunto | União, interseção, diferença | `set1.union(set2)`, `set1.intersection(set2)` |
| **Dict**              | Iteração por chaves | Percorrer todas as chaves | `for chave in dict` |
| **Dict**              | Iteração por valores | Percorrer todos os valores | `for valor in dict.values()` |
| **Dict**              | Iteração por pares | Percorrer chaves e valores | `for chave, valor in dict.items()` |
| **Dict**              | Verificar valor | Buscar se valor existe | `valor in dict.values()` |
| **Dict**              | Encontrar chave por valor | Buscar chave que possui determinado valor | `[k for k, v in dict.items() if v == valor]` |
| **Dict**              | Encontrar mínimo/máximo | Menor/maior valor ou chave | `min(dict.values())`, `max(dict.keys())` |

Aqui fica claro o que já foi mencionado na descrição das estruturas lineares: escolher a estrutura correta ou não pode ser a diferença fundamental na performance de algorítmo.
Veja que se usar uma lista, usar a operação de pertencimento vai levar tempo proporcional ao tamanho da entrada, enquanto usar conjunto vai levar a tempo constante.

Justamente a análise de complexidade permite a comparação de algoritmos em termos de tempo de execução e uso de memória.

** Curiosidade  do mundo real ** Os índices usados em banco de dados normalmente usam estruturas de dados que justamente permitem
buscas em tempo logorítmico através de busca binária. Um exemplo é o índice [B-Tree](https://en.wikipedia.org/wiki/B-tree). 
Sem índices a busca fica linear, ou seja, toda a tabela precisa ser percorrida, o que se chama de "Full Table Scan".
Mas por outro lado a inserção e remoção de linhas na tabela piora. Sem índice essas operações podem ser feitas em O(1).
Mas com índice existe o custo de inserção e remoção de elementos no índice, que custam log n. 

Algorítmos lineares ainda são eficazes, mas nem sempre é possível atingir esse tipo de performance.
O próximo nivel em termos de função é chamado sublinear, confira a seguir:

#### 4. O(n log n) - Sublinear

Algoritmos sublineares possuem tempo de execução dado por n log n. Eles possuem esse nome por conta da complexidade ser ligeiramente pior que os lineares. Mas ainda são bem melhores que os quadráticos.

Os mais clássicos algoritmos sublineares que precisamos conhecer são os de ordenação complexos, como Merge Sort e Quick Sort.

As melhores soluções gerais de ordenação possuem essa complexidade. É raro ser solicitado para implementarmos os algoritmos na entrevista. Mas é fundamental sabermos que esse é o custo a se pagar se precisarmos ordenar uma lista de n elementos usando a biblioteca padrão da linguagem.

Algumas vezes vai compensar pagar esse custo, se for diminuir a complexidade geral do algoritmo. Mas algumas vezes não vai compensar. Exemplo disso é o cálculo do máximo elemento.

Se usarmos a função max, já vimos que o custo é linear:

```python
>>> lista = [3, 2, 5, 7, 19]
>>> max(lista)  # O(n)
19

```

Então usar ordenação vai piorar a complexidade do algorítmo, apesar de deixar a solução mais simples que implementar max manulamente:

```python
>>> lista = [3, 2, 5, 7, 19] #
>>> lista.sort() # O(n log n)
>>> lista
[2, 3, 5, 7, 19]
>>> lista[-1]  # O(1)
19

```

Contudo, se fosse uma primeira solução em vez de se implementar manualmente o algorítmo max, seria válido para demonstrar conhecimento e foco na resolução do problema, antes de pensar em performance.

Depois da complexidade sublinear temos a quadráticas em termos de ordem de complexidade. Confira na próxima seção.

#### 5. O(n^2) - Quadrática

Algorítmos quadráticos acontecem normalmente quando temos dois laços aninhados para executar uma operação.
Se encaixam aqui os algorítmos de ordenaçaõ simples, como Selection, Insertion e Buble Sort.
Costumam ocorrer também em operações em matrizes quadradas, como soma e subtração.

Quando uma solução for quadrática vale sempre a pena estudar se a ordenação das entradas dos programa diminuiria a complexidade geral do algoritmo.
Ou seja, nos casos da funçao quadráticas e das duas que vão se seguir, pagar o custo da ordenação compensa
se a complexidade geral do algorítmo mudar para sublinear.

Para expoentes da função iguais ou maiores que dois, dizemos que essa é categoria geral de complexidade polinomial.
Contudo não é comum encontrarmos problemas de complexidade polinomial maior que 3.

Por isso é suficiente conhecer a quadrática e a cúbica, explicada a seguir.


#### 6. O(n^3) - Cúbica

Algoritmos cúbicos acontecem normalmente quando temos 3 laços aninhados para executar uma operação. Se encaixam operações em matrizes com 3 dimensões. 

Ainda assim, esse tipo de problema com 3 dimensões é raro em processos seletivos. Normalmente caem mais problemas com matrizes de duas dimensões.

Por isso não precisamos nos aprofundar nessa função. Assim, só fica faltando tratar da última função, a exponencial. Confira a seguir.

#### 7. O(2^n) - Exponencial

Algoritmos exponenciais possuem a pior complexidade que existe. Normalmente com um pequeno aumento no tamanho da entrada, o tempo de execução e/ou consumo de memória são tão grandes que não é possível chegar em uma solução.

Se enquadram aqui problemas de definição recursiva implementados de forma inocente, como o cálculo da sequência de Fibonacci.

Problemas de explosão combinatorial também têm essa mesma característica, como listar as permutações possíveis de um conjunto.

Justamente por isso é tão importante para empresas grandes cobrarem esse assunto em um processo seletivo. Quando se atinge escala, performance passa a ser uma questão de viabilidade, não apenas um requisito não funcional.

É importante sabermos as ordens de grandeza ao comparar complexidades de algoritmos. Por isso apresentamos todas as funções e suas comparações na próxima seção.

### Comparação das 7 principais funções de análise de complexidade

Confira a ordem de magnitude do aumento da saída quando aumentamos a entrada n de um algoritmo, de acordo com sua complexidade:

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(n³) | O(2^n) |
|---|------|----------|------|------------|-------|-------|--------|
| 8 | 1 | 3 | 8 | 24 | 64 | 512 | 256 |
| 16 | 1 | 4 | 16 | 64 | 256 | 4.096 | 65.536 |
| 32 | 1 | 5 | 32 | 160 | 1.024 | 32.768 | 4.294.967.296 |
| 64 | 1 | 6 | 64 | 384 | 4.096 | 262.144 | 18.446.744.073.709.551.616 |
| 128 | 1 | 7 | 128 | 896 | 16.384 | 2.097.152 | ~3,4 × 10³⁸ |
| 256 | 1 | 8 | 256 | 2.048 | 65.536 | 16.777.216 | ~1,2 × 10⁷⁷ |
| 512 | 1 | 9 | 512 | 4.608 | 262.144 | 134.217.728 | ~1,3 × 10¹⁵⁴ |

**Observações importantes:**
- **O(1)**: Sempre constante, independente do tamanho de n
- **O(log n)**: Usando logaritmo base 2, cresce muito lentamente. É mais parecido com O(1) que com O(n)
- **O(n)**: Cresce linearmente com n
- **O(n log n)**: Cresce um pouco mais rápido que linear. É mais parecida com a linear do que com a quadrática
- **O(n²)**: Cresce rapidamente de forma quadrática
- **O(n³)**: Cresce muito rapidamente de forma cúbica
- **O(2^n)**: Cresce exponencialmente - torna-se impraticável muito rapidamente

**🌍 Perspectiva Astronômica da Complexidade Exponencial:**

Para entender o quão dramático é o crescimento exponencial, considere que o valor `18.446.744.073.709.551.616` (resultado de 2^64) representa:

- **Em segundos**: 584,5 bilhões de anos
- **Comparado à idade da Terra** (4,54 bilhões de anos): **129 vezes maior!**
- **Comparado à idade do Universo** (13,8 bilhões de anos): **42 vezes maior!**

Isso significa que se um computador executasse 1 operação por segundo desde a formação da Terra, ele ainda precisaria de **mais 128 "Terras" de tempo** para completar um algoritmo O(2^64)!

Para ter uma ideia visual da discrepância entre as funções, veja o gráfico abaixo gerado pelo script `plot_complexity.py`:

![Gráfico de Complexidades](./complexity_chart.png)

O gráfico usa escala logarítmica no eixo Y para poder visualizar todas as funções no mesmo gráfico, já que O(2^n) cresce tão rapidamente que tornaria as outras funções invisíveis em escala linear.

**Como interpretar o gráfico:**
- As linhas mais horizontais (O(1) e O(log n)) representam os algoritmos mais eficientes
- A linha diagonal suave (O(n)) mostra crescimento linear controlado  
- A linha um pouco mais inclinada (O(n log n)) ainda é aceitável para a maioria dos casos
- As linhas curvas (O(n²) e O(n³)) mostram crescimento polinomial preocupante
- A linha exponencial (O(2^n)) mostra crescimento explosivo e impraticável

Assim se encerra a parte conceitual obrigatória para preparação para a fase de entrevista técnica. Mas só conhecer essa base teórica não é suficiente. Por isso segue estratégia para nos prepararmos na próxima seção.

## Como nos preparar para a entrevista técnica

A recomendação é criarmos um repositório para resolver problemas. A ideia é treinar o conhecimento e aumentar nosso repertório de soluções. Fazendo isso, normalmente encontraremos questões que já fizemos ou que são muito parecidas com exercícios.

Para isso, recomendamos fazer o máximo de exercícios do [Leetcode](https://leetcode.com/problemset/). Fazendo ao menos os 30 primeiros já garantimos uma boa preparação. 

Renzo, um dos colaboradores desse repositório, passou na entrevista técnica para grandes empresas: Google, Facebook, Red Hat e Quinto Andar. [Nesse repositório](https://github.com/renzon/code_interview_training) ele concentra soluções para problemas do Leetcode e outros.

### Dicas finais

1. Escolhemos, se o processo permitir, a linguagem de programação que mais conhecemos.

2. Buscamos validar as entradas e escrever testes, mesmo que em formato de comentários de código.

3. Fazemos debug mentalmente do nosso código, acrescentando valores de variáveis e sua evolução em comentários do código.

4. Se tivermos domínio de várias linguagens, escolhemos a de mais alto nível em que se escreva pouco. Por isso Renzo sempre escolhe Python ;)

5. Escrevemos testes para validar nosso entendimento de entrada e saída. Pode ser em formato de comentário. Essa é outra razão para Renzo escolher Python. É possível executar comentários e até documentação em formato de doctest!

Por exemplo, todo código dessa página é executado e validado com o comando `python -m doctest README.md`, inclusive no [![Doctest README.md](https://github.com/codigofontetv/entrevistas-tecnicas/actions/workflows/doctest.yml/badge.svg)](https://github.com/codigofontetv/entrevistas-tecnicas/actions/workflows/doctest.yml) desse repositório.

Então é isso, desejamos bons estudos e muitas aprovações nas entrevistas técnicas!






