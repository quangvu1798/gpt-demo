import streamlit as st

def main():
    st.markdown(
        '''
        <h1 align="center">
            Chào mừng tới trang chủ 👋
        </h1>
        ---
        ''',
        unsafe_allow_html = True,
    )
    with st.expander('Về trang web', True):
        st.markdown(
            '''
            Team AI đã xây dựng một demo về ChatGPT
            '''
        )

    
if __name__ == '__main__':
    main()

