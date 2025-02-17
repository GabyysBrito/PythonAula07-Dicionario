# =========================================================================================

# Funções 
# -> Elas são as responsáveis por executar ações de forma programática (em determinados momentos de interação do usuário).

# =========================================================================================

print('Bom dia, usuário seja bem vindo ao Vai no Coffee!!!')

login = input('Digite seu e-mail: ')
senha = int(input('Digite sua senha: '))

# Sintaxe da função em python
# def nome_da_funcao():
#     acao_a_ser_executada

def boas_vindas():
    print(f'Bom dia, {login} usuário seja bem vindo ao Vai no Coffee!!!')

def login_invalido():
    print('Tente novamente, suas credenciais são inválidas')

if login == "gaby@gmail.com" and senha == 12345:
    boas_vindas()
else:
    login_invalido()

# =========================================================================================

# Dicionario -> Que permite guardar uma quantidade quase infinita de valores, de forma desordenada, porém organizada em chave: valor

# =========================================================================================

# AS CHAVES DEVEM SER ÚNICAS, NÃO PODEM TER CHAVES REPETIDAS

# () -> Vamos utilizar somente se tive a necessidade de valores imutáveis (que não podem ser modificados)

# [] -> Vamos utilizar somente se tivermos a necessidade de guardamos uma quantidade muito grande de informação que podem ser modificada, porém não organizada (quarto da bagunça) 

# {} -> Vamos utilizar somente se tivermos a necessidade de guardamos uma quantidade muito grande de informação, que pode ser modificada, porém precisa obrigatóriamente estar organizada

# Sintaxe do dicionário

#nome_dicionario = {
#   'chave': 'valor'
#}

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

# Método update adiciona uma nova chave
nomes_clientes.update({'cliente_df':'Leonardo'})

# Trocando um valor em uma chave que já existe
nomes_clientes["cliente_sp"] = "Danilo" 
print(nomes_clientes)

# Remover uma chave do dicionário

del nomes_clientes['cliente_mg']
print(nomes_clientes)

# Adiciona um valor na chave
# OBS: Precisa colocar uma lista []
nomes_clientes['clientes_rj'].append("Fernanda")
print(nomes_clientes)


#--------------------- Iteração no Dicionário ----------------------------
# Iteração sobre as chaves do dicionário para exibir os estadoos dos clientes
# Usando for in

for clientes in nomes_clientes:
    print(f"Os estados dos clientes são: {clientes}")
