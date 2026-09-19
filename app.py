excelente = 0
ruim = 0
entrevistados = 0

while entrevistados < 50:

    print("\n===================================")
    print(f"ENTREVISTADOS CADASTRADOS: {entrevistados}/50")
    print("===================================")

    opcao = input("Deseja cadastrar um novo entrevistado? (S/N): ").upper()

    if opcao == "N":
        print("\nPesquisa encerrada pelo usuário.")
        break

    if opcao != "S":
        print("Opção inválida! Digite S ou N.")
        continue

    entrevistados += 1

    print(f"\n--- Entrevistado {entrevistados} ---")

    nome = input("Digite o nome do entrevistado: ")
    idade = int(input("Digite a idade: "))

    print("\nOpinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        pass
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção de opinião inválida!")

print("\n===================================")
print("       RESULTADO DA PESQUISA")
print("===================================")
print(f"Total de entrevistados: {entrevistados}")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
print("Pesquisa encerrada.")
