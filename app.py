import streamlit as st

from chatbot import predict_class, get_response, intents

#### DEPLOY ########################################
# Descargar recursos si no están disponibles
import nltk
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
    
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4')
#### /DEPLOY #######################################
    
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.title("Asistente virtual de EAD para Moodle")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "first_message" not in st.session_state:
    st.session_state.first_message = True
    
for message in st.session_state.messages:
    
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
if st.session_state.first_message:
    
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿cómo puedo ayudarte?")
        
    st.session_state.messages.append({"role": "assistant", "content": "Hola, ¿cómo puedo ayudarte?"})
    st.session_state.first_message = False
    
if prompt := st.chat_input("¿cómo puedo ayudarte?"):
    
    with st.chat_message("user"):
        st.markdown(prompt)
        
    st.session_state.messages.append({"role": "user", "content": prompt})
      
    # Implementación del algoritmo de IA
    insts = predict_class(prompt)
    res = get_response(insts, intents)
    
    with st.chat_message("assistant"):
        st.markdown(res)
        
    st.session_state.messages.append({"role": "assistant", "content": res})