#import streamlit as st
#import firebase_admin
#from firebase_admin import firestore, credentials

#def app():
   
    #if 'db' not in st.session_state:
      # st.session_state['db'] = " "
       
    #db = firestore.client()
   # st.session_state.db = db
    
    #ph = " "
   # if st.session_state.username == "":
      #  ph = 'Login to be able to post'
        
    #else:
       # ph = 'Post your thought'
        
    #post = st.text_area(label=' :orange[+ New Post]', placeholder=ph, height=None, maxchars=500)
    #if st.button('Post', use_container_width = 20):
       # if post != "":
            
           # info = db.collection('posts').document(st.session_state.username).get()
           # if info.exists:
             #   info = info.to_dict()
               # if 'Content' in info.keys():
               
                #    pos = db.collection('posts').document(st.session_state.username)
                 #   pos.update({'Content': firestore.ArrayUnion([u'{}'.format(post)])})

              #  else:
                   # data = {"Content":[post], "Username":st.session_state.username}
                   # db.collection('posts').document(st.session_state.username).set(data)
                    
           # else:
              #  data = {"Content":[post], "Username":st.session_state.username}
              #  db.collection('posts').document(st.session_state.username).set(data)
                
           # st.succcess('Post uploaded!!')
            
   # st.header(' :violet[Latest Posts] ')
    
    
   # docs = db.collection('posts').get()
    
   # for doc in docs:
       # d = doc.to_dict()
       # print(doc)
       # print("d: ", d)
       # try:
         #   st.text_area(label = ':green[Posted by:] '+':orange[{}]'.format(d['username']), value = d['Content'][-1],height = 20)
       # except:
        #    pass
            
#app()           
            
    