#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import openai
import eliza

# Configuração da chave da API OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

therapist = eliza.eliza()

def get_gpt3_response(prompt):
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()

def combined_chatbot_response(user_input):
    eliza_response = therapist.respond(user_input)
    
    # Se a resposta do ELIZA for muito genérica, consulte o GPT-3.
    if len(eliza_response.split()) <= 3:  # Este é um critério simplificado; você pode ajustar conforme necessário.
        return get_gpt3_response(user_input)
    else:
        return eliza_response

st.title("Chatbot Combinado ELIZA e GPT-3")

user_input = st.text_input("Digite sua mensagem:")
if st.button("Responder"):
    response = combined_chatbot_response(user_input)
    st.write(response)
