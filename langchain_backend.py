import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain_openai import OpenAI

load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(openai_api_key=openai_key,temperature=0.8)


def generate_name_menu(cuisine):
    # Using Sequential Chain to get the restaurant name as well in the output. 
    from langchain.chains import LLMChain
    prompt= PromptTemplate(
        input_variables =['cuisine'],
        template="I want to open a restaurant for {cuisine} cuisine. Suggest a fancy name for this"
    )  #This actually creates a template of prompt to be given to LLM.
    name_chain = LLMChain(prompt=prompt, llm=llm,output_key="restaurant_name" )
    prompt_menu= PromptTemplate(
        input_variables =['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comman seperated value."
    )
    food_items_chain = LLMChain(prompt=prompt_menu, llm=llm, output_key="menu_items")
    from langchain.chains import SequentialChain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name','menu_items']
    )
    response=chain.invoke({"cuisine":cuisine})
    
    return response

if __name__ == "__main__":
    print(generate_name_menu("Indian"))
    
