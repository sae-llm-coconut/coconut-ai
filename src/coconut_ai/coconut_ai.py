import requests
import io
import base64
from typing import Iterator, TypedDict
from llama_cpp import Llama

from PIL import Image


BASE_URL = "http://127.0.0.1:7861"


def encode_file_to_base64(path: str) -> str:
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')


class TextToImageOptions(TypedDict):
    input_text: str
    output_path: str
    steps: int


class TextToTextOptions(TypedDict):
    input_text: str
    model_path: str
    max_tokens: int


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


def text_to_text(options: TextToTextOptions) -> str:
    """
    Given a model path, input text, and max tokens, return the generated text.

    Returns an empty string if the model path is invalid or the model fails to generate text.
    """
    model = Llama(model_path=options['model_path'])
    system_message = "You are a helpful assistant"
    user_message = options["input_text"]
    prompt = f"""<s>[INST] <<SYS>>
    {system_message}
    <</SYS>>
    {user_message} [/INST]"""
    output = model(prompt, max_tokens=options['max_tokens'], echo=False)
    if not isinstance(output, Iterator) and len(output['choices']) > 0:
        return output['choices'][0]['text']
    return ""


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
