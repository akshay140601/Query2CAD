# Query2CAD

## How to run the system
1. Download and setup the [FreeCAD](https://github.com/FreeCAD/FreeCAD) software. The system has been tested on Windows and Linux OS with a screen size of 1920x1080.
2. Clone the repository.
```
git clone https://github.com/akshay140601/Query2CAD.git
```

3. Set up Together AI API to use Llama models or get the API key of OpenAI to use GPT models. Take a look at args in src/run.py for arguments that you can specify. Assuming the keys are already set, run the below command to run the system.
```
python src/run.py --code_gen_model codellama/chatgpt/llama3/gpt4-turbo --reasoning_model codellama/chatgpt/llama3/gpt4-turbo --human_feedback True
```

4. The results will be stored in the results/ folder and new queries can be added in data/queries.txt
