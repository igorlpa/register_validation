
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum


class DocType(Enum):
    IDENTITY = "RG"
    DRIVER_LICENSE = "CNH"
    PASSPORT = "Passaporte"

class DocSchema(BaseModel):
    type: DocType = Field(description="Tipo do documento")
    approved: bool = Field(description="Indica se o documento foi aprovado. Esta com boa qualidade e todos os campos legiveis")
    reason: str | None = Field(description="Motivo pelo qual o documento nao foi aprovado, se aplicavel")
    name: str | None = Field(description="Nome completo informado no documento")
    cpf: str | None = Field(description="CPF informado no documento")
    birth_date: datetime | None = Field(description="Data de nascimento informada no documento")
    
    