from typing import TypedDict


class TextToImageOptions(TypedDict):
    text: str
    output_path: str


class ImageToTextOptions(TypedDict):
    image_path: str


class TextToTextOptions(TypedDict):
    text: str


class ImageToImageOptions(TypedDict):
    image_path: str
    output_path: str


class CoconutAI:
    def __init__(self) -> None:
        pass

    def text_to_image(self, options: TextToImageOptions) -> None:
        print("---Text To Image---")
        print(f"Text: {options['text']}")
        print(f"Output Image Path: {options['output_path']}")

    def image_to_text(self, options: ImageToTextOptions) -> str:
        print("---Image To Text---")
        print(f"Image Path: {options['image_path']}")
        return "Text"

    def text_to_text(self, options: TextToTextOptions) -> str:
        print("---Text To Text---")
        print(f"Text: {options['text']}")
        return options["text"]

    def image_to_image(self, options: ImageToImageOptions) -> None:
        print("---Image To Image---")
        print(f"Image Path: {options['image_path']}")
        print(f"Output Image Path: {options['output_path']}")
