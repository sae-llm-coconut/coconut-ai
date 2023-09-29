from typing import TypedDict


class GenerateImageOptions(TypedDict):
    text: str
    output_path: str


class CoconutAI:
    def __init__(self) -> None:
        pass

    def text_to_image(self, options: GenerateImageOptions) -> None:
        print("Generating Image from Text...")
        print(f"Image: {options['text']}")
        print(f"Output Image Path: {options['output_path']}")
