

from src.doc_schema import DocSchema
import os
import json
from google import genai
from PIL import Image
import base64
from io import BytesIO
import pathlib
from google.genai import types



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
- Tipo do documento (CNH, RG ou Passaporte)
- Numero do cpf (Se for um passaporte, retorne o numero do passaporte)

Se a informacao nao estiver presente no documento ou estiver ilegivel, retorne None para o campo correspondente.
"""
    
    def check_doc(self, doc_path: str) -> DocSchema:
 
        if doc_path.lower().endswith('.pdf'):
            filepath = pathlib.Path(doc_path)
            file_part = types.Part.from_bytes(data=filepath.read_bytes(), mime_type='application/pdf')
        else:
            image = Image.open(doc_path)
            # Convert PIL Image to bytes
            buffer = BytesIO()
            image.save(buffer, format='JPEG')
            image_bytes = buffer.getvalue()
            
            # Create the content with proper MIME type
            file_part = {
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(image_bytes).decode('utf-8')
                }
            }

        
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[self.prompt, file_part],
            config=genai.types.GenerateContentConfig(
                #   thinking_config=genai.types.ThinkingConfig(thinking_budget=512),
                  temperature=0.0,
                  response_mime_type="application/json",
                  response_schema=DocSchema
                )
        )
        return DocSchema(**json.loads(response.text))
               
       