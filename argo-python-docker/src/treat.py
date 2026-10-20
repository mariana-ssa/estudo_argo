def main():
    print("Iniciando tratamento dos dados...")

    dados = [10, 20, 30, 40, 50]
    media = sum(dados) / len(dados)

    print(f"Dados processados: {dados}")
    print(f"Média calculada: {media}")
    print("Tratamento concluído!")
    # raise ValueError("Erro proposital para teste do Argo Workflow")


if __name__ == "__main__":
    main()
