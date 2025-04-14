import streamlit as st
from firebase_admin import firestore

def app():
    db = firestore.client()
    
    try:
        st.title("Posted by: "+st.session_state['username'])
        
        result = db.collection('posts').document(st.session_state['username']).get()
        r = result.to_dict()
        content = r['content']
        
        def delete_post(k):
            c = int(k)
            h = content[c]
            
            try:
                db.collection('posts').document(st.session_state['username']).update({'content': firestore.ArrayRemove([h])})
                st.warnining("Post deleted")
            except:
                st.write("Something went wrong")
                
        for c in range(len(content)-1,-1,-1):
            st.text_area(label='', value=content[c])
            st.button("Delete",on_click=delete_post,args=([c] ), key=c)
            
    except:
        if st.session_state['username'] == '':
            st.write("Please login first")
        else:
            st.write("You have not posted anything yet")
