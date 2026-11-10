import random
import string

def gerar_senha(tamanho=12):
    caracteres = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas Seguras ===")

    try:
        tamanho = int(input("Digite o tamanho da senha: "))

        if tamanho < 4:
            print("A senha deve ter pelo menos 4 caracteres.")
            return

        senha = gerar_senha(tamanho)

        print("\nSenha gerada:")
        print(senha)

    except ValueError:
        print("Digite um número válido.")

if __name__ == "__main__":
    main()