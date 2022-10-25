import pickle
import streamlit as st
model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))
def main():
    st.title("Email spam classifier")
    st.subheader("It is used to classify whether tany test is")
    msg=st.txt_input("enter the test: ")
    if st.button("predict"):
        data=[msg]
        vect=cv.transform(data).toarray()
        predict=model.predict(vect)
        result=predict[0]
        if result==1:
            st.error("this text is spam")
        else:
            st.success("this text is not spam")
    
main()
