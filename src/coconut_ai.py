from typing import TypedDict


class GenerateImageOptions(TypedDict):
    prompt: str
    output_path: str


class CoconutAI:
    def __init__(self) -> None:
        pass

    def generate_image(self, options: GenerateImageOptions) -> None:
        print("Generating image...")
        print(f"Prompt: {options['prompt']}")
        print(f"Output path: {options['output_path']}")
