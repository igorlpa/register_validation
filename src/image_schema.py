



from pydantic import BaseModel, Field

class ImageSchema(BaseModel):
    approved: bool = Field(description="Se a imagem é aprovada de acordo com as regras")
    centered: bool = Field(description="Se a pessoa está centralizada na imagem")
    framed: bool = Field(description="Se a pessoa está dentro do enquadramento desejado, sem cortes e sem obstruções (incluindo proprios bracos)")
    background: bool = Field(description="Se a pessoa está com fundo simples e neutro")
    quality: bool = Field(description="Se a pessoa está com qualidade de imagem adequada (não borrada, não superexposta, não subexposta, com boa iluminação)")
    accessories: bool = Field(description="Se a pessoa está sem acessorios (bone, chapeu, mascaras, etc)")
    filters: bool = Field(description="Se a pessoa está sem filtros ou efeitos aplicados")
    reason: str = Field(description="Motivo da aprovação ou reprovação da imagem")
    
    def __str__(self):
        return f"ImageSchema(approved={self.approved}, \ncentered={self.centered}, \nframed={self.framed}, \nbackground={self.background}, \nquality={self.quality}, \naccessories={self.accessories}, \nfilters={self.filters}, \nreason={self.reason})"
