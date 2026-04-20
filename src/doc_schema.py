
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum


class DocType(Enum):
    IDENTITY = "RG"
    DRIVER_LICENSE = "CNH"
    PASSPORT = "Passaporte"
    UNKNOWN = "Unknown"

class DocSchema(BaseModel):
    type: DocType = Field(description="Tipo do documento")
    approved: bool = Field(description="Indica se o documento foi aprovado. Esta com boa qualidade e todos os campos legiveis")
    reason: str | None = Field(description="Motivo pelo qual o documento nao foi aprovado, se aplicavel")
    name: str | None = Field(description="Nome completo informado no documento")
    doc_id: str | None = Field(description="ID do documento (CPF ou numero do Passaporte)")
    birth_date: datetime | None = Field(description="Data de nascimento informada no documento")
    
    def __str__(self):
        return f"DocSchema(type={self.type}, approved={self.approved}, reason={self.reason}, name={self.name}, doc_id={self.doc_id}, birth_date={self.birth_date})"