import streamlit as st
import openai
import os


openai.api_type = "azure"
openai.api_base = "https://yoni123.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = st.text_input('here you need the key for azure openai api',type='password')



def generate_gpt_chat(prompt,model='test',max_tokens=4000,temperature=0.5):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].text


# prompt = "suspect from pakistan that waits in the border of india \
#     and pakistan we want to guess his previos location take in \
#         concidiration he born in pakisan and he is 30 years old "
    
# prompt = "common 10 names for pets in pakistan"
# print(generate_gpt_chat(prompt,model='milan',max_tokens=4000,temperature=0.5))

list_context = []
suspect_info = st.text_input("describe the suspect")

if st.button("generate info on suspect"):
    suspect_info_out = st.write(generate_gpt_chat(suspect_info,model='milan',max_tokens=4000,temperature=1))
    list_context.append(suspect_info_out)
    


