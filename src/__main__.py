import os
from .coconut_ai import coconut_ai
# from . import utils


if __name__ == "__main__":
    # Download model
    # utils.download_model(url="", folder_name="example_model", file_name="example_model.pt")

    # Create CoconutAI instance
    coconut_ai_instance = coconut_ai.CoconutAI()
    os.makedirs(os.path.abspath(os.path.join(os.getcwd(), "dist")), exist_ok=True)
    coconut_ai_instance.image_to_image({
        "image_path": "C:/Users/jules/Documents/BUT/A3/SAE la mort/coconut-ai/dist/potooJesus.png",
        "output_path": os.path.abspath(os.path.join(os.getcwd(), "dist", "output_img_to_img.png"))
    })
    coconut_ai_instance.text_to_image({
        "text": "Coconut",
        "output_path": os.path.abspath(os.path.join(os.getcwd(), "dist", "output.png"))
    })

