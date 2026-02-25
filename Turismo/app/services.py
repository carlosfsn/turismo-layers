from datetime import date
from Turismo.domain.models import Pacote
from Turismo.domain.rules import validar_pacote
from Turismo.infra.repo_protocols import PacoteRepository

def cadastrar_pacote(repo: PacoteRepository, *, id: int, destino: str, preco: float, ida: date, volta: date) -> None:
    pacote = Pacote(id=id, destino=destino, preco=preco, ida=ida, volta=volta)
    validar_pacote(pacote)

    if repo.get_by_id(id) is not None:
        raise ValueError("Já existe pacote com este ID.")

    repo.add(pacote)

def buscar_pacote(repo: PacoteRepository, id_: int) -> Pacote:
    pacote = repo.get_by_id(id_)
    if pacote is None:
        raise ValueError("Pacote não encontrado.")
    return pacote

def listar_pacotes(repo: PacoteRepository) -> list[Pacote]:
    return list(repo.list_all())

def atualizar_pacote(repo: PacoteRepository, *, id: int, destino: str, preco: float, ida: date, volta: date) -> None:
    pacote = Pacote(id=id, destino=destino, preco=preco, ida=ida, volta=volta)
    validar_pacote(pacote)
    repo.update(pacote)

def remover_pacote(repo: PacoteRepository, id_: int) -> None:
    repo.delete(id_)