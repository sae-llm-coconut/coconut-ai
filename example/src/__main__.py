import os

import importlib
from coconut_ai import CoconutAI

if __name__ == "__main__":
    coconut_ai = CoconutAI()
    os.makedirs(os.path.abspath(os.path.join(os.getcwd(), "dist")), exist_ok=True)
    coconut_ai.text_to_image({
        "text": "Coconut",
        "output_path": os.path.abspath(os.path.join(os.getcwd(), "dist", "output.png"))
    })
    print('Hello World!')
