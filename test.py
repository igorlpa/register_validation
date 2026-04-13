from PIL import Image
from src.image_validation import ImageValidation 
from dotenv import load_dotenv
load_dotenv()


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




        





if __name__ == "__main__":
    main_images()