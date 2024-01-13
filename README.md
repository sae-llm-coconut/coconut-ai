# coconut-ai

## About

Coconut AI

<https://pypi.org/project/coconut-ai/>

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) v3.10
- [Pipenv](https://pipenv.pypa.io/)
- [Pip](https://pypi.org/project/pip/)
- [AUTOMATIC1111/Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) v1.6.0

### Installation

```sh
pipenv install coconut-ai
```

### Usage

```sh
# Go to AUTOMATIC1111/Stable Diffusion web UI source code
cd stable-diffusion-webui

# Run the AUTOMATIC1111/Stable Diffusion Web API
./webui.sh --api --nowebui

# Go to coconut-ai source code
cd ../coconut-ai

# Run the coconut-ai example script
cd example
pipenv install
pipenv run start --type="text_to_image" --input="Coconut" --output="./data/output.png"
```

## 💡 Contributing

Anyone can help to improve the project, submit a Feature Request, a bug report or even correct a simple spelling mistake.

The steps to contribute can be found in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## 📄 License

[MIT](./LICENSE)
