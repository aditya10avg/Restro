# Restaurant Name Generator

This project generates a fancy restaurant name and menu items based on a given cuisine using OpenAI's GPT model via the LangChain library.

## Requirements

Before running the project, ensure you have the following dependencies installed:

1. **Python 3.10 or above**
2. **OpenAI API Key** – You must have an OpenAI API key. [Get your key here](https://beta.openai.com/signup/).
3. **Libraries** – You need to install the required libraries.

### Install Dependencies

```bash
pip install openai langchain python-dotenv langchain-community
```

### Setup Instructions
Create a .env File

In the root directory of the project, create a .env file and add your OpenAI API key in this format:
``` bash
OPENAI_API_KEY=your_openai_api_key
```
Load Environment Variables

The script loads environment variables from the .env file using python-dotenv, so ensure the .env file is correctly configured.

Run the Script

You can run the Python script directly from the terminal. For example, to generate a restaurant name and menu items for "Indian" cuisine:

```bash
python generate_restaurant.py
```
The function generate_name_menu(cuisine) generates a fancy restaurant name and menu based on the provided cuisine argument. The result is displayed in the console.


### Code Explanation

LangChain Setup: This project uses LangChain, a powerful framework for working with language models. The script defines two chains:
Name Generation Chain: Takes the cuisine as input and generates a fancy restaurant name.
Menu Generation Chain: Based on the restaurant name, it generates a list of menu items.
SequentialChain: The output of the name chain is passed into the menu chain, creating a sequential flow.
OpenAI: This code interacts with OpenAI's GPT model using the langchain_openai package to generate text based on the templates.

Example Output
For a cuisine input like "Indian", the output might look like this:
``` bash
Restaurant Name: The Royal Curry House
Menu Items:
- Butter Chicken, Biryani, Samosa, Naan, Tandoori Chicken
```

### Customization

Temperature: You can adjust the creativity of the model by modifying the temperature setting in the OpenAI instance (0.0 is deterministic, 1.0 is more creative).
Cuisines: You can input different cuisines like "Italian", "Chinese", or any other cuisine to generate unique restaurant names and menus.

### Troubleshooting

Missing API Key: Ensure that you have a valid OPENAI_API_KEY in the .env file.
Dependencies: If any libraries are missing, use pip install -r requirements.txt to install all dependencies.
