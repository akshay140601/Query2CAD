import together
import os
import requests

def get_answers(model, api_key, query, temp) -> str:
    """
    Given the prompt: Get the LLM response for that particular prompt.
    Model Used: CodeLlama 70b
    """

    os.environ["TOGETHER_API_KEY"] = api_key

    if model == "codellama":
        url = 'https://api.together.xyz/inference'
        headers = {
        'Authorization': 'Bearer ' + os.environ["TOGETHER_API_KEY"],
        'accept': 'application/json',
        'content-type': 'application/json'
        }
        data = {
        "model": "codellama/CodeLlama-70b-hf",
        "prompt": query,
        "max_tokens": 1500,
        "temperature": temp,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stop": ["<|EOT|>","<|begin▁of▁sentence|>","<|end▁of▁sentence|>", "<|\s|>", "### [User message]"]
        }
        response = requests.post(url, json=data, headers=headers)
        #print(response.json())
        #print('===================')
        text = response.json()['output']['choices'][0]['text']
        #print(text)
        return text
    
    else:
        # TODO: Write code for GPT models using OpenAI keys
        pass