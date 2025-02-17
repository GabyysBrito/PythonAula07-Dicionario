# 🐍 Anotações de Python - Dicionário

## O que é dicionário?
- Um **dicionário** em Python é uma coleção de pares chave-valor. Ele é um tipo de dado mutável e desordenado, onde cada valor é armazenado com uma chave única que é usada para acessar o valor associado.

Diferente de listas e tuplas, os dicionários não mantêm uma ordem dos elementos. Cada chave é única e é usada para mapear a um valor correspondente.

### Sintaxe do dicionário:
```python
nome_dicionario = {
    'chave': 'valor'
}
```

## Características dos Dicionários

- `Mutabilidade:` Dicionários podem ser alterados depois de criados, ou seja, é possível adicionar, modificar ou remover elementos.

- `Desordenado:` Os elementos não possuem uma ordem definida.
Chaves únicas: As chaves devem ser únicas, mas os valores podem ser repetidos.

- `Acessibilidade:` Os valores são acessados pelas chaves.

- `Tipos de dados:` As chaves devem ser de tipos imutáveis (como strings, números, tuplas), e os valores podem ser de qualquer tipo de dado (strings, listas, inteiros, etc).

## Exemplo de um dicionário de clientes

``` python
    nomes_clientes = {
    'cliente_mg': 'Douglas',
    'clientes_rj': ["Yuri", "Jakeline", "Leonardo", "Bernardo"],
    'cliente_rs': 'Argel',
    'cliente_pe': 'Hugo',
    'cliente_pi': 'Davi',
    'cliente_sp': 'Vinicius',
    'cliente_pa': 'Marlon',
    'cliente_ce': 'Waldecy'
}
```

## Operações comuns em Dicionários

1. Adicionar uma nova chave

- O método update() permite adicionar uma nova chave ao dicionário:

    ```python
    nomes_clientes.update({'cliente_df':'Leonardo'})
    ```

2. Alterar o valor de uma chave existente

- Pode modificar o valor de uma chave já existente:

    ```python
    nomes_clientes["cliente_sp"] = "Danilo"
    print(nomes_clientes)
    ```

3. Remover uma chave

- Para remover uma chave do dicionário, você pode usar a função del:

    ```python
    del nomes_clientes['cliente_mg']
    print(nomes_clientes)
    ```

4. Adicionar um valor à chave existente (quando o valor é uma lista)

- Se o valor associado a uma chave for uma lista, você pode usar o método append() para adicionar um novo valor a essa lista:

    ```python
    nomes_clientes['clientes_rj'].append("Fernanda")
    print(nomes_clientes)
    ```

## Tipos de Estruturas Utilizadas

- `()`: Usado para armazenar valores imutáveis, como tuplas, que não podem ser modificados.

- `[]`: Usado quando há a necessidade de armazenar uma quantidade grande de informações que podem ser modificadas, mas não necessariamente organizadas.

- `{}`: Usado para armazenar uma grande quantidade de informações que podem ser modificadas e precisam estar organizadas.

## Iteração sobre o Dicionário

- Pode iterar sobre as chaves de um dicionário utilizando um laço for. O exemplo a seguir mostra como percorrer as chaves e exibir os estados dos clientes:

```python
    for clientes in nomes_clientes:
    print(f"Os estados dos clientes são: {clientes}")
```

# Conclusão

- Dicionários em Python são extremamente úteis para armazenar dados de forma organizada, permitindo o acesso rápido aos valores através das chaves. Eles oferecem uma grande flexibilidade para trabalhar com coleções de dados de diferentes tipos.

