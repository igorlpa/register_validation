



from pydantic import BaseModel, Field

class ImageSchema(BaseModel):
    approved: bool = Field(description="Se a imagem é aprovada de acordo com as regras")
    centered: bool = Field(description="Se a pessoa está centralizada na imagem ")
    profile: bool = Field(description="Informa se a pessoa está de perfil ou de frente para a camera. Deve ser True se estiver olhando para frente")
    framed: bool = Field(description="Se a pessoa está dentro do enquadramento desejado (3x4 ou mais afastada mas do torax pra cima), sem cortes e sem obstruções (nao aceites bracos obstruindo cabeca e ou torax)")
    background: bool = Field(description="Se a pessoa está com fundo simples e neutro - aceite alteracoes *minimas*")
    quality: bool = Field(description="Se a pessoa está com qualidade de imagem adequada (não borrada, não superexposta, não subexposta, com boa iluminação)")
    accessories: bool = Field(description="Se a pessoa está sem acessorios (bone, chapeu, mascaras, veu, bolsas)")
    filters: bool = Field(description="Se a pessoa está sem filtros ou efeitos aplicados")
    reason: str = Field(description="Motivo da aprovação ou reprovação da imagem")
    
    def __str__(self):
        return f"ImageSchema(approved={self.approved}, \ncentered={self.centered}, \nframed={self.framed}, \nbackground={self.background}, \nquality={self.quality}, \naccessories={self.accessories}, \nfilters={self.filters}, \nreason={self.reason})"
