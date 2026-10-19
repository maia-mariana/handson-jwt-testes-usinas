"""
Camada de Servico, UsinaService: regras de negocio das usinas.
"""

from app.domain.usina import Usina, UsinaCreate, UsinaUpdate
from app.repositories.usina_repository import UsinaRepository, usina_repository


class ErroDeNegocio(Exception):
    """Erro padronizado: vira {"error": {"code", "message", "status"}} na resposta."""

    def __init__(self, code: str, message: str, status: int) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.status = status


class UsinaService:
    def __init__(self, repository: UsinaRepository) -> None:
        self._repository = repository

    def listar(self) -> list[Usina]:
        return self._repository.listar()

    def buscar_por_id(self, usina_id: int) -> Usina:
        usina = self._repository.buscar_por_id(usina_id)
        if usina is None:
            raise ErroDeNegocio(
                code="RECURSO_NAO_ENCONTRADO",
                message=f"Usina {usina_id} nao encontrada.",
                status=404,
            )
        return usina

    def criar(self, dados: UsinaCreate) -> Usina:
        return self._repository.criar(dados)

    def atualizar(self, usina_id: int, dados: UsinaUpdate) -> Usina:
        usina = self.buscar_por_id(usina_id)
        alteracoes = dados.model_dump(exclude_unset=True)
        return self._repository.atualizar(usina.model_copy(update=alteracoes))

    def remover(self, usina_id: int) -> None:
        self.buscar_por_id(usina_id)
        self._repository.remover(usina_id)


usina_service = UsinaService(usina_repository)
