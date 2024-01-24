import os

from .coconut_ai import coconut_ai

if __name__ == '__main__':
    print("Coconut AI")
    # output_path = os.path.abspath("data/output.png")
    # os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # coconut_ai.text_to_image({
    #     "input_text": "Coconut",
    #     "output_path": output_path,
    #     "steps": 5
    # })

    model_path = os.path.abspath("data/llama-2-7b.Q5_K_M.gguf")
    print(coconut_ai.text_to_text({
        'input_text': "Generate a list of 5 funny dog names.",
        'max_tokens': 1000,
        'model_path': model_path
    }))
