from .models import Pacote

def validar_pacote(p: Pacote) -> None:
    if p.id <= 0:
        raise ValueError("ID deve ser positivo.")
    if not p.destino.strip():
        raise ValueError("Destino é obrigatório.")
    if p.preco < 0:
        raise ValueError("Preço não pode ser negativo.")
    if p.volta < p.ida:
        raise ValueError("Data de volta não pode ser anterior à ida.")