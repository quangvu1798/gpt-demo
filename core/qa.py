import streamlit as st
from .process import construct_prompt, COMPLETIONS_API_PARAMS
import openai
import re

def main():
    default_value = 'Cách khai báo loại tiền mới trên web?'
    question = st.text_input('Câu hỏi:', default_value)
    st.write('Trả lời:')
    answer = st.empty()
    answer.markdown('')
    
    prompt = construct_prompt(question)[0]
    if st.button('Lấy câu trả lời'):
        with st.spinner('Đang sinh câu trả lời...'):
            openai.api_key = "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"
            response = ''
            for resp in openai.Completion.create(prompt = prompt, **COMPLETIONS_API_PARAMS):
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

