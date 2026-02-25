from datetime import date
from Turismo.app import services
from Turismo.infra.repo_protocols import PacoteRepository

def _ler_int(msg: str) -> int:
    return int(input(msg).strip())

def _ler_float(msg: str) -> float:
    return float(input(msg).strip().replace(",", "."))

def _ler_data(msg: str) -> date:
    s = input(f"{msg} (YYYY-MM-DD): ").strip()
    return date.fromisoformat(s)

def run_cli(repo: PacoteRepository) -> None:
    while True:
        print("\n=== Agencia de Turismo ===")
        print("1) Cadastrar pacote")
        print("2) Buscar pacote por ID")
        print("3) Listar pacotes")
        print("4) Atualizar pacote")
        print("5) Remover pacote")
        print("0) Sair")

        op = input("Escolha: ").strip()

        try:
            if op == "1":
                id_ = _ler_int("ID: ")
                destino = input("Destino: ")
                preco = _ler_float("Preço: ")
                ida = _ler_data("Data ida")
                volta = _ler_data("Data volta")
                services.cadastrar_pacote(repo, id=id_, destino=destino, preco=preco, ida=ida, volta=volta)
                print("✅ OK: pacote cadastrado.")

            elif op == "2":
                id_ = _ler_int("ID: ")
                p = services.buscar_pacote(repo, id_)
                print("✅ Encontrado:", p)

            elif op == "3":
                pacotes = services.listar_pacotes(repo)
                if not pacotes:
                    print("ℹ️ Nenhum pacote cadastrado.")
                for p in pacotes:
                    print("-", p)

            elif op == "4":
                id_ = _ler_int("ID: ")
                destino = input("Novo destino: ")
                preco = _ler_float("Novo preço: ")
                ida = _ler_data("Nova data ida")
                volta = _ler_data("Nova data volta")
                services.atualizar_pacote(repo, id=id_, destino=destino, preco=preco, ida=ida, volta=volta)
                print("✅ OK: pacote atualizado.")

            elif op == "5":
                id_ = _ler_int("ID: ")
                services.remover_pacote(repo, id_)
                print("✅ OK: pacote removido.")

            elif op == "0":
                print("Saindo...")
                break

            else:
                print("❌ Opção inválida.")

        except Exception as e:
            print(f"❌ Erro: {e}")