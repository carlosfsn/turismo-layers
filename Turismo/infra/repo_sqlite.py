import sqlite3
from datetime import date
from typing import Optional, Iterable
from Turismo.domain.models import Pacote

class PacoteRepoSQLite:
    def __init__(self, db_path: str = "cvc.db") -> None:
        self.db_path = db_path
        self._init_db()

    def _conn(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init_db(self) -> None:
        with self._conn() as con:
            con.execute("""
            CREATE TABLE IF NOT EXISTS pacotes (
                id INTEGER PRIMARY KEY,
                destino TEXT NOT NULL,
                preco REAL NOT NULL,
                ida TEXT NOT NULL,
                volta TEXT NOT NULL
            )
            """)
            con.commit()

    def add(self, pacote: Pacote) -> None:
        with self._conn() as con:
            con.execute(
                "INSERT INTO pacotes (id, destino, preco, ida, volta) VALUES (?, ?, ?, ?, ?)",
                (pacote.id, pacote.destino, pacote.preco, pacote.ida.isoformat(), pacote.volta.isoformat()),
            )
            con.commit()

    def get_by_id(self, id_: int) -> Optional[Pacote]:
        with self._conn() as con:
            row = con.execute(
                "SELECT id, destino, preco, ida, volta FROM pacotes WHERE id=?",
                (id_,),
            ).fetchone()

        if not row:
            return None

        return Pacote(
            id=int(row[0]),
            destino=str(row[1]),
            preco=float(row[2]),
            ida=date.fromisoformat(row[3]),
            volta=date.fromisoformat(row[4]),
        )

    def list_all(self) -> Iterable[Pacote]:
        with self._conn() as con:
            rows = con.execute(
                "SELECT id, destino, preco, ida, volta FROM pacotes ORDER BY id"
            ).fetchall()

        for r in rows:
            yield Pacote(
                id=int(r[0]),
                destino=str(r[1]),
                preco=float(r[2]),
                ida=date.fromisoformat(r[3]),
                volta=date.fromisoformat(r[4]),
            )

    def update(self, pacote: Pacote) -> None:
        with self._conn() as con:
            cur = con.execute(
                "UPDATE pacotes SET destino=?, preco=?, ida=?, volta=? WHERE id=?",
                (pacote.destino, pacote.preco, pacote.ida.isoformat(), pacote.volta.isoformat(), pacote.id),
            )
            con.commit()

        if cur.rowcount == 0:
            raise ValueError("Pacote não encontrado para atualizar.")

    def delete(self, id_: int) -> None:
        with self._conn() as con:
            cur = con.execute("DELETE FROM pacotes WHERE id=?", (id_,))
            con.commit()

        if cur.rowcount == 0:
            raise ValueError("Pacote não encontrado para remover.")