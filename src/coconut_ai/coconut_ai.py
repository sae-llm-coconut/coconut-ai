import requests
import io
import base64
from typing import TypedDict

from PIL import Image


BASE_URL = "http://127.0.0.1:7861"


def encode_file_to_base64(path: str) -> str:
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')


class TextToImageOptions(TypedDict):
    input_text: str
    output_path: str
    steps: int


class ImageToTextOptions(TypedDict):
    input_path: str


class TextToTextOptions(TypedDict):
    text: str


class ImageToImageOptions(TypedDict):
    input_path: str
    output_path: str
    steps: int


def text_to_image(options: TextToImageOptions) -> None:
    payload = {
        "prompt": options['input_text'],
        "steps": options['steps']
    }
    response = requests.post(url=f'{BASE_URL}/sdapi/v1/txt2img', json=payload)
    data = response.json()
    image = Image.open(io.BytesIO(base64.b64decode(data['images'][0])))
    image.save(options['output_path'])
    image.close()


def image_to_text(options: ImageToTextOptions) -> str:
    print("---Image To Text---")
    print(f"Image Path: {options['input_path']}")
    return "Text"


def text_to_text(options: TextToTextOptions) -> str:
    print("---Text To Text---")
    print(f"Text: {options['text']}")
    return options["text"]


def image_to_image(options: ImageToImageOptions) -> None:
    payload = {
        "init_images": [encode_file_to_base64(options['input_path'])],
        "steps": options['steps']
    }
    response = requests.post(url=f'{BASE_URL}/sdapi/v1/img2img', json=payload)
    data = response.json()
    image = Image.open(io.BytesIO(base64.b64decode(data['images'][0])))
    image.save(options['output_path'])
    image.close()
