# COLETOR DE DADOS.V1
A idéia do programa é coletar os dados do usuário e no final montar uma frase com os dados informados

# COLETOR DE DADOS.V1
## O QUE FOI MUDADO ?

`Função get_valid_age`:

Objetivo: Garantir que o usuário insira uma idade válida (números inteiros).
Como funciona:
Usa um loop while True para continuar pedindo a entrada até que um valor válido seja fornecido.
`input("Insira sua idade: ")` solicita a idade do usuário.
`age.isdigit()` verifica se a entrada é composta apenas por dígitos.
Se a entrada for válida, a função retorna a idade como um inteiro.
Se não for válida, exibe uma mensagem de erro e continua o loop.
Coleta dos dados do usuário:

`name = input("Insira seu nome: ").strip()` coleta o nome do usuário e remove espaços em branco no início e no fim.
`city = input("Insira sua cidade: ").strip()` faz o mesmo para a cidade.
`age = get_valid_age()` chama a função para obter uma idade válida.
Saída final:

`print(f"\nOlá {name}, você tem {age} anos e mora em {city}.")` exibe uma mensagem formatada com os dados inseridos pelo usuário.
