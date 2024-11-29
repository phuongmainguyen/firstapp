import streamlit as st
st.title('Bé tập làm toán ')
col1, col2, col3,  = st.columns(3)
with col1:
    a = st.number_input('a')
with col2:
    op= st.radio('Phép toán', ('\+', '\-', 'x', ':'), horizontal=True)
with col3:
    b = st.number_input('b')
r=st.number_input('Nhập kết quả:')
if st.button('Kiểm tra', use_container_width=True, type = 'primary'):
    if op =='\+':
        c = a + b
    elif op =='\-':
        c = a- b
    elif op == 'x':
        c = a*b
    elif op == ':':
        c = a/b
    if c ==r:
        st.success('Chính xác')
        st.balloons()
    else: 
        st.error('Sai')
        st.snow
