import re

def validar_senha(senha):
    erros = []

    # Verifica se a senha tem no mínimo 8 caracteres
    if len(senha) < 8:
        erros.append("Ter no mínimo 8 caracteres")

    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not any(char.isupper() for char in senha):
        erros.append("Conter pelo menos uma letra maiúscula")

    # Verifica se a senha contém pelo menos uma letra minúscula
    if not any(char.islower() for char in senha):
        erros.append("Conter pelo menos uma letra minúscula")

    # Verifica se a senha contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        erros.append("Conter pelo menos um número")

    # Verifica se a senha contém pelo menos um caractere especial
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        erros.append("Conter pelo menos um caractere especial (ex: !@#$%^&*())")

    if not erros:
        return "Senha forte"
    else:
        return f"Senha fraca. Faltam os seguintes critérios: {', '.join(erros)}"

# Entrada do usuário
senha_usuario = input("Digite uma senha para validar: ")
resultado = validar_senha(senha_usuario)
while True:
    print(resultado)
    continuar = input("Deseja validar outra senha? (s/n): ").strip().lower()
    if continuar == 's':
        senha_usuario = input("Digite uma senha para validar: ")
        resultado = validar_senha(senha_usuario)
    elif continuar == 'n':
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")