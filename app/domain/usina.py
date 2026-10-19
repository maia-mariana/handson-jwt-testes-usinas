"""
Camada de Dominio, entidade Usina (usinas solares da Bulbe Energia).
"""

from enum import Enum

from pydantic import BaseModel, Field


class StatusUsina(str, Enum):
    ativa = "ativa"
    inativa = "inativa"
    em_manutencao = "em_manutencao"


class UsinaCreate(BaseModel):
    """Dados enviados para cadastrar uma usina."""
    nome: str = Field(..., min_length=3, max_length=100)
    localizacao: str = Field(..., min_length=3, max_length=150)
    capacidade_geracao_kwh: float = Field(..., gt=0, description="Capacidade em kWh, maior que zero")
    status: StatusUsina = StatusUsina.ativa


class UsinaUpdate(BaseModel):
    """Dados para atualizar uma usina. Todos os campos sao opcionais."""
    nome: str | None = Field(None, min_length=3, max_length=100)
    localizacao: str | None = Field(None, min_length=3, max_length=150)
    capacidade_geracao_kwh: float | None = Field(None, gt=0)
    status: StatusUsina | None = None


class Usina(UsinaCreate):
    """Usina cadastrada, com id."""
    id: int
