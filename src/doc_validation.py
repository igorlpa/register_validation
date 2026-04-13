

from src.doc_schema import DocSchema
import os
from google import genai


class DocValidation:
    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

        if not self.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set")

        # The client gets the API key from the environment variable `GEMINI_API_KEY`.
        self.client = genai.Client()
        
        self.prompt = """ 
Você é um assistente de IA com expertise em análise de documentos para cadastro em sistemas.

Seu objetivo é analisar o documento e verificar se ele está de boa qualidade para ser utilizada em um cadastro online e extrair as informações necessárias. 
Verifique se é uma imagem de um documento valido e que o mesmo esta com todos os campos legiveis e sem obstruções.

Verifique os seguintes requisitos:
- A imagem deve conter apenas um documento.
- O documento deve estar bem iluminado e sem borrões ou manchas.
- O documento deve estar completo e sem cortes.
- O documento nao deve estar recortado ou com partes importantes fora da imagem.
- O documento deve ser: CNH, RG ou Passaporte.

Extraia as seguintes informações do documento:
- Nome
- Data de nascimento
- Numero do cpf
- Tipo do documento (CNH, RG ou Passaporte)

Se a informacao nao estiver presente no documento ou estiver ilegivel, retorne None para o campo correspondente.
"""
    
    def check_doc(self, doc_path: str) -> DocSchema:
        # TODO: Implement document validation logic
        pass