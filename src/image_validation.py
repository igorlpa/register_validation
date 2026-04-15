
import base64
import os
import json
from io import BytesIO

from PIL import Image
from google import genai
from src.image_schema import ImageSchema



class ImageValidation:
    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

        if not self.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set")

        # The client gets the API key from the environment variable `GEMINI_API_KEY`.
        self.client = genai.Client()
        
        self.prompt = """
Você é um assistente de IA com expertise em análise de imagens para cadastro em sistemas.

Seu objetivo é analisar a imagem e verificar se é uma imagem de boa qualidade para ser utilizada em um cadastro online. 
Verifique se é uma imagem de busto de uma pessoa, com fundo neutro e com boa qualidade. 
Verifique os seguintes requisitos:
- A imagem deve conter apenas uma pessoa.
- A pessoa deve estar de frente para a câmera.
- A pessoa deve estar centralizada. Especialmente no eixo horizontal. Aceite leves desvios no eixo vertical.
- A pessoa deve estar enquadrada do busto ao topo da cabeça (estilo 3x4 ou mais afastada mas do torax pra cima). recuse imagens que a parte inferior do abdomen e/ou pernas sejam visiveis.
- A pessoa nao deve estar recortada. A pessoa deve estar nitida e claramente sendo recortada. Se o contorno da pessoa tocar levemente a borda deve ser aceito.
- A pessoa nao deve estar obstruída por objetos, outras pessoas ou partes do proprio corpo. (*RECUSE* se houver bracos cruzados ou outras posicoes que obstruam a visao da face e/ou torax)
- O fundo deve ser neutro (aceite leves altercoes).
- A qualidade da imagem deve ser boa (nao deve estar borrada, com excesso de ruidos, mau iluminada, contra luz, etc).
- A pessoa nao deve estar usando bones, chapeus, mascaras, toucas ou veu. (desconsiderar relogios, oculos de grau e colares)
- A imagem nao deve estar manipulada e nem ter sido editada com filtros ou efeitos.

Caso nao consiga identificar alguma das condições acima, retorne False e explique o motivo.
"""
    
    def check_image(self, pil_image: Image):
        # Convert PIL Image to bytes
        buffer = BytesIO()
        pil_image.save(buffer, format='JPEG')
        image_bytes = buffer.getvalue()
        
        # Create the content with proper MIME type
        image_part = {
            "inline_data": {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(image_bytes).decode('utf-8')
            }
        }
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[self.prompt, image_part],
            config=genai.types.GenerateContentConfig(
                #   thinking_config=genai.types.ThinkingConfig(thinking_budget=512),
                  temperature=0.0,
                  response_mime_type="application/json",
                  response_schema=ImageSchema
                )
        )
        return ImageSchema(**json.loads(response.text))