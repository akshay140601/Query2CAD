import together
import os
import requests
import openai
from openai import OpenAI

def get_answers(model, api_key, query, temp, base_url = None) -> str:
    """
    Given the prompt: Get the LLM response for that particular prompt.
    Model Used: CodeLlama 70b
    """

    if model == "codellama":
        os.environ["TOGETHER_API_KEY"] = api_key
        url = 'https://api.together.xyz/inference'
        headers = {
        'Authorization': 'Bearer ' + os.environ["TOGETHER_API_KEY"],
        'accept': 'application/json',
        'content-type': 'application/json'
        }
        data = {
        "model": "codellama/CodeLlama-70b-hf",
        "prompt": query,
        "max_tokens": 3000,
        "temperature": temp,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stop": ["<|EOT|>","<|begin▁of▁sentence|>","<|end▁of▁sentence|>", "<|\s|>", "### [User message]", "\n\n\n\n\n"]
        }
        response = requests.post(url, json=data, headers=headers)
        #print(response.json())
        #print('===================')
        text = response.json()['output']['choices'][0]['text']
        print(text)

        return text
    
    elif model == "chatgpt":
        client = OpenAI(api_key=api_key, base_url=base_url)
        message = {
            'role' : 'user',
            'content' : query
        }
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[message],
            stop=["<END>", "### [User message]", "\n\n\n\n\n"],
            temperature=temp,
            max_tokens=3000
        )
        output = response.choices[0].message.content
        print(output)

        return output
    
    elif model == 'gpt4-turbo':
        client = OpenAI(api_key=api_key, base_url=base_url)
        message = {
            'role' : 'user',
            'content' : query
        }
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[message],
            stop=["<END>", "### [User message]", "\n\n\n\n\n"],
            temperature=temp,
            max_tokens=3000
        )
        output = response.choices[0].message.content
        print(output)

        return output

    
    elif model == "llama3":
        os.environ["TOGETHER_API_KEY"] = api_key
        url = 'https://api.together.xyz/inference'
        headers = {
        'Authorization': 'Bearer ' + os.environ["TOGETHER_API_KEY"],
        'accept': 'application/json',
        'content-type': 'application/json'
        }
        data = {
        "model": "meta-llama/Llama-3-70b-chat-hf",
        "prompt": query,
        "max_tokens": 3000,
        "temperature": temp,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stop": ["<|EOT|>","<|begin▁of▁sentence|>","<|end▁of▁sentence|>", "<|\s|>", "### [User message]", "\n\n\n\n\n"]
        }
        response = requests.post(url, json=data, headers=headers)
        #print(response.json())
        #print('===================')
        text = response.json()['output']['choices'][0]['text']
        print(text)

        return text
