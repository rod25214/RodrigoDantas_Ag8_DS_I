# Pesquisa de Opinião - Tudoweb

## Sobre o projeto

Este projeto foi desenvolvido em Python para realizar uma pesquisa de opinião com clientes da empresa de marketing **TudoWeb**, com o objetivo de verificar o grau de satisfação em relação ao atendimento prestado.

O programa permite cadastrar até **50 entrevistados**, coletando o nome, a idade e a opinião de cada participante.

## Opções de atendimento

O entrevistado pode escolher uma das seguintes opções:

* **1 - EXCELENTE**
* **2 - BOM**
* **3 - RUIM**

Ao final da pesquisa, o programa apresenta:

* Quantidade total de entrevistados;
* Quantidade de respostas **EXCELENTE**;
* Quantidade de respostas **RUIM**.

## Funcionalidades

* Cadastro de até 50 entrevistados;
* Contagem dos entrevistados cadastrados;
* Cadastro de nome e idade;
* Registro da opinião sobre o atendimento;
* Contagem das respostas EXCELENTE e RUIM;
* Estruturas de decisão com `if`, `elif` e `else`;
* Estrutura de repetição com `while`;
* Possibilidade de encerrar a pesquisa antes de completar 50 entrevistados;
* Exibição dos resultados ao finalizar a pesquisa.

## Como funciona

Antes de cadastrar cada entrevistado, o programa informa quantas pessoas já foram cadastradas.

O usuário pode escolher:

```text
S - Continuar cadastrando entrevistados
N - Encerrar a pesquisa
```

Caso seja escolhida a opção **N**, a pesquisa é encerrada imediatamente e os resultados são apresentados.

Caso sejam cadastrados 50 entrevistados, o programa também encerra automaticamente a pesquisa.

## Exemplo de execução

```text
===================================
ENTREVISTADOS CADASTRADOS: 0/50
===================================
Deseja cadastrar um novo entrevistado? (S/N): S

--- Entrevistado 1 ---
Digite o nome do entrevistado: João
Digite a idade: 25

Opinião sobre o atendimento:
1 - EXCELENTE
2 - BOM
3 - RUIM

Digite sua opinião: 1
```

Depois de alguns cadastros, o usuário pode encerrar:

```text
===================================
ENTREVISTADOS CADASTRADOS: 10/50
===================================
Deseja cadastrar um novo entrevistado? (S/N): N

Pesquisa encerrada pelo usuário.

===================================
       RESULTADO DA PESQUISA
===================================
Total de entrevistados: 10
Quantidade de respostas EXCELENTE: 4
Quantidade de respostas RUIM: 3
Pesquisa encerrada.
```

## Tecnologias utilizadas

* **Python 3**
* Estrutura de repetição `while`
* Estruturas condicionais `if`, `elif` e `else`
* Entrada e saída de dados com `input()` e `print()`

## Testes

Foi realizado um teste com **10 entrevistados** para verificar o funcionamento do programa e a contagem das respostas.

O programa também foi testado com a opção de encerramento antecipado, permitindo finalizar a pesquisa antes de atingir o limite de 50 entrevistados.

## Arquivo do projeto

O código principal está disponível no arquivo:

```text
pesquisa_opiniao.py
```

## Atividade

Projeto desenvolvido como atividade da **Agenda 8 de Desenvolvimento de Sistemas**, utilizando estruturas de repetição e decisão em Python.
- Rodrigo D.
