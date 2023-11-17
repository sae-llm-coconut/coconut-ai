import os

from coconut_ai import CoconutAI

if __name__ == "__main__":
    coconut_ai_instance = CoconutAI()
    os.makedirs(os.path.abspath(os.path.join(os.getcwd(), "dist")), exist_ok=True)
    coconut_ai_instance.text_to_image({
        "text": "Coconut",
        "output_path": os.path.abspath(os.path.join(os.getcwd(), "dist", "output.png"))
    })
    print('Hello World!')
