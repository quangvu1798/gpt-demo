import streamlit as st
from .process import construct_prompt
import openai
import re

finetune_model = {
    'temperature': 0.5,
    'max_tokens': 1000,
    'model': "davinci:ft-personal-2023-02-10-04-28-17",
    'stream': True
}

def main():
    default_value = 'Cách khai báo loại tiền mới trên web?'
    question = st.text_input('Câu hỏi:', default_value)
    st.write('Trả lời:')
    answer = st.empty()
    answer.markdown('')
    
    prompt = construct_prompt(question)[0]
    if st.button('Lấy câu trả lời'):
        with st.spinner('Đang sinh câu trả lời...'):
            response = ''
            openai.api_key = "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"
            for resp in openai.Completion.create(prompt = prompt, **finetune_model):
                response += resp.choices[0].text
                response = response.replace(r'\n', '\n\n')
                links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response)
                if len(links) > 0:
                    for link in links:
                        link = link.replace('[', '').replace(']', '')
                        if link[-4:] in ['.jpg', '.png', '.jpeg', '.gif']:
                            response = response.replace('[' + link + ']', f'![image]({link})')
                try:
                    answer.markdown(response)
                except:
                    pass
        st.success('Đã tạo xong câu trả lời!')

    
if __name__ == '__main__':
    main()

