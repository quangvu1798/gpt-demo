import streamlit as st

from core import intro, finetune, qa, gpt3_finetune

def init():
    st.session_state.pages = {
        '🕴️ Introduce': intro.main,
        # '🔥 Fine-tuned model': finetune.main,
        '🌟 Fine-tuned GPT-3 with meInvoice Data': gpt3_finetune.main,
        '✨ Question-Answering with Embedding': qa.main
    }

def draw_style():
    st.set_page_config(page_title = 'GPT Demo',
                       page_icon = '🔥',
                       layout = 'wide',
                       menu_items = {
                          'Get help': 'https://www.facebook.com/chienlady/',
                          'Report a Bug': 'https://www.facebook.com/chienlady/',
                          'About': 'Trang web có mục đích riêng rư.'
                       })

    style = '''
        <style>
            header {visibility: visible;}
            footer {visibility: hidden;}
        </style>
    '''
    st.markdown(style, unsafe_allow_html = True)
 
def load_page(page_name):
    st.session_state.pages[page_name]()
    
def main():
    init()
    draw_style()
    with st.sidebar:
        st.markdown('# Menu GPT Demo')
        st.image('https://media.giphy.com/media/udbIBMfgpypAqeQDHs/giphy.gif')
        page = st.selectbox('Chọn mục thử nghiệm',
                            ('🕴️ Introduce',
                            #  '🔥 Fine-tuned model',
                             '🌟 Fine-tuned GPT-3 with meInvoice Data',
                            '✨ Question-Answering with Embedding'),
                            key = 'choose_page')
    load_page(page) 
 
if __name__ == '__main__':
    main()


