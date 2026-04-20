from PIL import Image
import os
import json
from dotenv import load_dotenv
load_dotenv()

from src.image_validation import ImageValidation 
from src.doc_validation import DocValidation


def main_images():
    image_paths = [
        "/Users/igorlucena/Documents/igor - repositorios/register_validation/resources/WhatsApp Image 2026-04-09 at 10.48.20 (1).jpeg",
        "/Users/igorlucena/Documents/igor - repositorios/register_validation/resources/WhatsApp Image 2026-04-09 at 10.48.20 (2).jpeg",
        "/Users/igorlucena/Documents/igor - repositorios/register_validation/resources/WhatsApp Image 2026-04-09 at 10.48.21 (1).jpeg",
        "/Users/igorlucena/Documents/igor - repositorios/register_validation/resources/WhatsApp Image 2026-04-09 at 10.48.21 (2).jpeg",
        "/Users/igorlucena/Documents/igor - repositorios/register_validation/resources/WhatsApp Image 2026-04-09 at 10.48.21 (3).jpeg",
        "/Users/igorlucena/Documents/igor - repositorios/register_validation/resources/WhatsApp Image 2026-04-09 at 10.48.22 (1).jpeg",
        "/Users/igorlucena/Documents/igor - repositorios/register_validation/resources/WhatsApp Image 2026-04-09 at 10.48.22.jpeg"
    ]
    
    image_validation = ImageValidation()
    
    for image_path in image_paths:
        print(image_path)

        image = Image.open(image_path)
        print(image.size)
        
        result = image_validation.check_image(image)
        print(result)
        print("=" * 50, "\n")

        image.show()
        input("Press Enter to continue...")



def main_docs():
    docs_dir = "/Users/igorlucena/Documents/igor - repositorios/register_validation/resources/docs/"
    doc_paths = list_files_from_dir(docs_dir)
 
    doc_validation = DocValidation()
    
    for doc_path in doc_paths:
        print(doc_path)
        
        result = doc_validation.check_doc(doc_path)
        print(result)
        print("=" * 50, "\n")

        input("Press Enter to continue...")


        

def list_files_from_dir(directory: str) -> list[str]:
    """Returns a list of file paths in a given directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]





if __name__ == "__main__":
    # main_images()
    main_docs()
