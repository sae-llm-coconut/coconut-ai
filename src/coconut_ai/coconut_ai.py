import json
import requests
import io
import base64
import urllib.request
import os
from typing import TypedDict
from PIL import Image


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

url = "http://127.0.0.1:7860"

def encode_file_to_base64(path: str)->str:
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

class CoconutAI:
    def __init__(self) -> None:
        pass

    def text_to_image(self, options: TextToImageOptions) -> None:
        print("---Text To Image---")
        print(f"Text: {options['text']}")
        payload = {
            "prompt": options['text'],
            "steps": 5
        }

        response = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/txt2img', json=payload)
        r = response.json()
        print(f"Output Image Path: {options['output_path']}")

        image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))
        image.save(options['output_path'])

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
        payload = {
            "init_images": [encode_file_to_base64(options['image_path'])],
            "steps": 5
        }
        response = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/img2img', json=payload)
        r = response.json()
        print(f"Output Image Path: {options['output_path']}")
        image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))
        image.save(options['output_path'])



