# coconut-ai

## About

**Coconut AI** is a **Python library** that allows you to use [AUTOMATIC1111/Stable Diffusion Web API](https://github.com/AUTOMATIC1111/stable-diffusion-webui), to **generate images from text** or **images to images**.

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

### Usage

For a complete example, see the [coconut-ai-example](https://github.com/sae-llm-coconut/coconut-ai-example) repository.

```sh
# Go to AUTOMATIC1111/Stable Diffusion web UI source code
cd stable-diffusion-webui

# Run the AUTOMATIC1111/Stable Diffusion Web API
./webui.sh --api --nowebui

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

## 💡 Contributing

Anyone can help to improve the project, submit a Feature Request, a bug report or even correct a simple spelling mistake.

The steps to contribute can be found in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## 📄 License

[MIT](./LICENSE)
