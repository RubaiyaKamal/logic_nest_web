import streamlit as st
import firebase_admin

from firebase_admin import credentials, auth

cred = credentials.Certificate("logic-nest-firebase-adminsdk-fbsvc-2ff6f4b534.json")
firebase_admin.initialize_app(cred)


def app():
    st.title('Welcome To :violet[Logic Nest]')
    
    
    #choice = st.selectbox('Login/Signup', ['Login', 'SignUp'])
    
    if 'username' not in st.session_state:
        st.session_state.username = ''
        
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    
    def f():
        try:
            user = auth.get_user_by_email(email)
            #print(user.uid)
            
            st.success('Login Successful')
            
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            st.session_state.signedout = True
            
            
        except:
            st.warning('Login failed')
            
    def t():
        st.session_state.signedout = False
        st.session_state.signout = False
        st.session_state.username = ''
    
            
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False
        
    if not st.session_state.signedout:
        choice = st.selectbox('Login/Signup', ['Login', 'SignUp'])
    
        if choice == 'Login':
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
       
            st.button('Login', on_click=f)

    
        else:
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
       
            username = st.text_input('Enter your unique username')
       
            if st.button('Create my account'):
                user = auth.create_user(
                    email=email,
                    password=password,
                    display_name=username,
               )
           
                st.success('Your created successfully')  
                st.markdown('Please Login using your email and password')
                st.balloons()
                
                
    if st.session_state.signedout:
        st.text('Name' +st.session_state.username)
        st.text('Email' +st.session_state.useremail)
        st.button('Sign out', on_click=t)
        
    def signout():
        st.session_state.signout = True
        st.session_state.signedout = False
        st.experimental_rerun()
        
    if st.session_state.signout:
        st.session_state.signout = False
        st.experimental_rerun()
        
