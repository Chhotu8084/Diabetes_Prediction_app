import pandas as pd
import streamlit as st
import pickle
import sklearn
# Load the model
with open('model_for_diabetes.pkl', 'rb') as pkl:
    classifier = pickle.load(pkl)


def main():
    style = """<div style='background-color: #12345F; padding:10px'>
                <h1 style ='color:white'><Center>Diabetes Prediction</h1>
                </div> """
    st.markdown(style, unsafe_allow_html=True)
    left, right = st.columns((2, 2))
    Pregnancies = left.text_input('Enter Preganancies as whole numbers(0 - 20)', " ")
    Glucose = right.text_input('Enter Glucose as whole numbers(0 - 240)', " ")
    BloodPressure = left.text_input('Enter Blood Pressure as whole numbers(0 - 150)', "")
    SkinThickness = right.text_input('Enter Skin Thickness as whole numbers(0 - 100)', " ")
    Insulin = left.text_input('Enter Insulin as whole numbers(0 - 1000)', " ")
    BMI = right.text_input('Enter BMI as decimal numbers(0 - 100)', " ")
    DiabetesPedigreeFunction = left.text_input('Enter  DiabetesPedigreeFunction as decimal numbers(0 - 5)'," ")
    Age = right.text_input('Enter Age as whole numbers(0 - 100)', " ")
    predict_button = st.button('Am I Diabetic ?')

    # When predict button is clicked
    if predict_button:

        res = classifier.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if res[0] == 0:
            st.success("You are not Diabetic")
        else:
            st.success("You are Diabetic")


if __name__ == '__main__':
    main()
