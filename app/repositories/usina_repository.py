"""
Camada de Persistencia, UsinaRepository (em memoria).
"""

from app.domain.usina import Usina, UsinaCreate


class UsinaRepository:
    def __init__(self) -> None:
        self._usinas: dict[int, Usina] = {}
        self._proximo_id: int = 1

    def listar(self) -> list[Usina]:
        return list(self._usinas.values())

    def buscar_por_id(self, usina_id: int) -> Usina | None:
        return self._usinas.get(usina_id)

    def criar(self, dados: UsinaCreate) -> Usina:
        usina = Usina(id=self._proximo_id, **dados.model_dump())
        self._usinas[usina.id] = usina
        self._proximo_id += 1
        return usina

    def atualizar(self, usina: Usina) -> Usina:
        self._usinas[usina.id] = usina
        return usina

    def remover(self, usina_id: int) -> None:
        del self._usinas[usina_id]


usina_repository = UsinaRepository()
