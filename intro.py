import streamlit as st

def main():
    st.markdown(
        '''
<h1 align="center">
    Chào mừng tới trang web thử nghiệm mô hình GPT 👋
</h1>
        ''',
        unsafe_allow_html = True,
    )
    with st.expander('Giới thiệu', True):
        st.markdown(
            '''
Team AI đã xây dựng một demo về OpenAI GPT, có một số lưu ý sau:
1. Hiện tại OpenAI chưa mở API cho phép sử dụng ChatGPT, hiện chỉ hỗ trợ cho một số bộ mô hình sau:
- **OpenAI GPT-3**: mô hình sinh ngôn ngữ lớn (large language model) của OpenAI
- **OpenAI InstructGPT**: được fine-tune dựa trên OpenAI GPT-3 với phương pháp RLHF (Reinforcement Learning from Human Feedback)
2. Tuy nhiên OpenAI mới chỉ cho phép fine-tune mô hình GPT-3 của họ, tuy nhiên phương pháp fine-tune này không được áp dụng RLHF mà chỉ là SFT (Supervised Fine-Tuning) nên sẽ tạo ra một mô hình GPT-3 mới có khả năng few-shot tốt hơn với dữ liệu của cá nhân
> ![RLHF](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffbdf39e9-c592-44dd-b760-50557806614a_867x477.png)
            '''
        )
    with st.expander('Giải thích', True):
        st.markdown(
            '''
*Hiện tạo Team AI đang thử nghiệm 2 phương pháp*
## 1. 🔥 Fine-tuned model
Fine-tune GPT-3 với tác vụ Tư vấn hỗ trợ

## 2. ✨ Question-Answering with Embedding
Sử dụng phương pháp Question Answering with Embedding
            '''
        )

    
if __name__ == '__main__':
    main()

