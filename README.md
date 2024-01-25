# coconut-ai

## About

**Coconut AI** is a **Python library** that allows you to use [AUTOMATIC1111/Stable Diffusion Web API](https://github.com/AUTOMATIC1111/stable-diffusion-webui) and [LLama 2](https://ai.meta.com/llama/), to **generate images from text**, **images to images** or **text to text**.

The library is available on **PyPy**: <https://pypi.org/project/coconut-ai/>.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) v3.10
- [Pipenv](https://pipenv.pypa.io/)
- [AUTOMATIC1111/Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) v1.6.0

### Installation

```sh
pipenv install coconut-ai
```

### Stable Diffusion Guide

For a complete example, see the [coconut-ai-example](https://github.com/sae-llm-coconut/coconut-ai-example) repository.

#### Install Stable Diffusion Web UI

[AUTOMATIC1111/Stable Diffusion Web UI installation guide](https://github.com/AUTOMATIC1111/stable-diffusion-webui?tab=readme-ov-file#installation-and-running)

```sh
# Clone the AUTOMATIC1111/Stable Diffusion Web UI repository
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

# Go to AUTOMATIC1111/Stable Diffusion Web UI source code
cd stable-diffusion-webui

# For Windows users, run the following command for starting the server
./webui-user.bat --api --nowebui

# For Linux/MacOS users, run the following command for starting the server
./webui.sh --api --nowebui
```

#### Stable Diffusion Usage

**Note:** Before using the library, you must start the Stable Diffusion Web UI server.

```sh
# Go to your Python project/source code
cd ../python-project
pipenv install coconut-ai
```

Create a file named `main.py` with the following content (minimal example):

```py
import os

import coconut_ai

if __name__ == '__main__':
    print("Coconut AI")
    output_path = os.path.abspath("output.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    coconut_ai.text_to_image({
        "input_text": "Coconut",
        "output_path": output_path,
        "steps": 5
    })
```

Run the script:

```sh
pipenv run python main.py
```

### LLama 2 Guide

For a complete example, see the [coconut-ai-example](https://github.com/sae-llm-coconut/coconut-ai-example) repository.

Download the model [`llama-2-7b.Q5_K_M.gguf`](https://huggingface.co/TheBloke/Llama-2-7B-GGUF/blob/main/llama-2-7b.Q5_K_M.gguf) manually.

All available models can be found on the [Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-GGUF#provided-files) website.

```sh
# Go to your Python project/source code
cd ../python-project
pipenv install coconut-ai
```

Create a file named `main.py` with the following content (minimal example):

```py
import os

import coconut_ai

if __name__ == '__main__':
    print("Coconut AI")
    # Replace with the model path for the llama-2-7b.Q5_K_M.gguf model downloaded manually
    model_path = os.path.abspath("data/llama-2-7b.Q5_K_M.gguf")
    print(coconut_ai.text_to_text({
        'input_text': "Generate a list of 5 funny dog names.",
        'max_tokens': 1000,
        'model_path': model_path
    }))
```

Run the script:

```sh
pipenv run python main.py
```

## 💡 Contributing

Anyone can help to improve the project, submit a Feature Request, a bug report or even correct a simple spelling mistake.

The steps to contribute can be found in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## 📄 License

[MIT](./LICENSE)
