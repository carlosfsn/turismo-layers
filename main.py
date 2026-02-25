from Turismo.infra.repo_sqlite import PacoteRepoSQLite
from Turismo.ui.cli import run_cli

def main() -> None:
    repo = PacoteRepoSQLite(db_path="cvc.db")
    run_cli(repo)

if __name__ == "__main__":
    main()