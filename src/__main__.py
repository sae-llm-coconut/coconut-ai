import os
from src.coconut_ai import CoconutAI

if __name__ == "__main__":
    coconut_ai = CoconutAI()
    coconut_ai.text_to_image({
        "text": "Prompt...",
        "output_path": os.path.abspath(os.path.join(os.getcwd(), "dist", "output.png"))
    })
