# pptai

Python script to generate slide deck with chatgpt using prompt.
Currently only supports chatgpt as AI model.

## Installation

```sh
# optional, create python environment
pyenv virtualenv pptai

# install python dependencies
pip install -r requirements.txt
```

Obtain [OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key). Create a config.yml
file and add this key to your config.

```yaml
client:
  openai:
    api_key: <api-key>
```

## Usage
Run the main script which will then prompt you for input

```sh
python main.py

Enter your prompt for the presentation content:
```

Script will output the generated yaml structure for the slide deck
and save the pptx file to generated_presentation.pptx

