import openai
import os
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


# Load environment variables from .env file
_ = load_dotenv(find_dotenv(r"C:\Users\hassa\OneDrive\Desktop\Internship Files\LiteLLM Test\openai_key.env"))

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    # Create a chat completion
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response['choices'][0]['message']['content']

# Example usage
#print(get_completion("What is 1+1?"))

customer_email = """
Arrr, I be fuming that me blender lid flew off and splattered me kitchen walls with smoothie! And to make matters worse,\
the warranty don't cover the cost of cleaning up me kitchen. I need yer help right now, matey!"""

style = """American English in a calm and respectful tone"""

prompt = f"""Translate the text that is delimited by triple backticks into a style that is {style}.
text: ```{customer_email}```"""
print(prompt)
'''
chat = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")
template_string = """Translate the text that is delimited by triple backticks into a style that is {style}. \
text: ```{text}```"""
prompt_template = ChatPromptTemplate.from_template(template_string)
prompt_template.messages[0].prompt.input_variables

customer_style = """American English in a calm and respectful tone
"""
customer_email = """
Arrr, I be fuming that me blender lid flew off and splattered me kitchen walls with smoothie! And to make matters worse, \
the warranty don't cover the cost of cleaning up me kitchen. I need yer help right now, matey!"""

prompt = f"""Translate the text that is delimited by triple backticks into a style that is {style}.
text: ```{customer_email}```"""

#this formats the prompt by inputting the style and text
customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)

# Call the LLM to translate to the style of the customer message
customer_response = chat(customer_messages)
'''
print(prompt)
response = get_completion(prompt)
print(response)

