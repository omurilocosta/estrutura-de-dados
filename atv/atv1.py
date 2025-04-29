# SIMULADOR DE NAVEGAÇÃO EM PÁGINAS WEB

# Simulador de navegação com uso da estrutura de dados Pilha (Stack)

# Criamos uma lista para simular a pilha de páginas visitadas
pilha_paginas = []

def acessar_pagina():
    """Solicita ao usuário o nome da nova página e a adiciona ao topo da pilha."""
    pagina = input("Digite o nome da nova página: ")
    pilha_paginas.append(pagina)  # push: adiciona a nova página no topo da pilha
    print(f"✅ Página '{pagina}' acessada com sucesso!\n")

def voltar_pagina():
    """Remove a página atual da pilha (simula voltar para a anterior)."""
    if len(pilha_paginas) > 1:
        pagina_removida = pilha_paginas.pop()  # pop: remove a página atual
        print(f"↩ Voltou da página '{pagina_removida}' para '{pilha_paginas[-1]}'\n")
    elif len(pilha_paginas) == 1:
        print("⚠ Só há uma página na pilha. Não é possível voltar.\n")
    else:
        print("⚠ Nenhuma página foi acessada ainda.\n")

def mostrar_historico():
    """Exibe o histórico de navegação em ordem (do início ao topo da pilha)."""
    if pilha_paginas:
        print("🕘 Histórico de navegação:")
        for i, pagina in enumerate(pilha_paginas):
            marcador = " <- Página atual" if i == len(pilha_paginas) - 1 else ""
            print(f"{i+1}. {pagina}{marcador}")
        print()
    else:
        print("⚠ Nenhuma página foi acessada ainda.\n")

# Menu interativo
def menu():
    while True:
        print("=== Simulador de Navegação ===")
        print("1. Acessar nova página")
        print("2. Voltar página")
        print("3. Mostrar histórico")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            acessar_pagina()
        elif opcao == "2":
            voltar_pagina()
        elif opcao == "3":
            mostrar_historico()
        elif opcao == "4":
            print("👋 Encerrando o simulador.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.\n")

# Inicializa o programa com uma página inicial
pilha_paginas.append("Página Inicial")
menu()
