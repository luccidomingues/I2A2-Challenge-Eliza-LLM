import streamlit as st
import openai
import pyElizaChatbotClient
# from pyElizaChatbotClient import Eliza
from pyElizaChatbotClient.pyEliza import pyElizaChatbot

# Configuração da chave da API OpenAI
openai.api_key = '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'

# therapist = Eliza()
therapist = pyElizaChatbot(name='Eliza', log_file='pyEliza.log')
therapist.start()

def get_gpt3_response(prompt):
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()

def combined_chatbot_response(user_input):
    eliza_response = therapist.respond(user_input)
    
    # Se a resposta do ELIZA for muito genérica, consulte o GPT-3.
    if len(eliza_response.split()) <= 3:  # critério simplificado.
        return get_gpt3_response(user_input)
    else:
        return eliza_response

st.title("Chatbot Combinado ELIZA e GPT-3")

user_input = st.text_input("Digite sua mensagem:")
if st.button("Responder"):
    response = combined_chatbot_response(user_input)
    st.write(response)
