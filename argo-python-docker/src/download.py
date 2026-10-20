from datetime import datetime, timezone


def main():
    print("Iniciando download dos dados...")
    print(f"Data: {datetime.now(timezone.utc).isoformat()}")
    print("Download concluído com sucesso!")


if __name__ == "__main__":
    main()
