 
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
model = load_model('bank')






def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('photo-1518183214770-9cffbec72538.jpg')
    image_office = Image.open('HOME-LOAN-HIKE.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict if customer is eligible for personal loan or not')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predict that whether the individual could get a loan from bank or not ")
    if add_selectbox == 'Online':
        Age=st.number_input('age',min_value=1.0, max_value=100.0, value=1.0)
        Job=st.selectbox('job',['student','unemployed','self-employed','admin.','blue-collar','entreprenuer','housemaid','management','others','retired','services','technician'])
        Marital=st.selectbox('marital',['single','married','divorced'])
        Education=st.selectbox('education',['primary','secondary','tertiary'])
        Default=st.selectbox('default',['yes','no'])
        Balance=st.number_input('balance',min_value=1.0, max_value=400000.0, value=1.0)
        Housing=st.selectbox('housing',['Yes','No'])
        Day=st.number_input('day',min_value=1.0, max_value=31.0, value=1.0)
        Month=st.selectbox('month',['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
        Duration=st.number_input('duration',min_value=0.0, max_value=50.0, value=1.0)
        Campaign=st.number_input('campaign',min_value=0.0, max_value=60.0, value=1.0)
        Pdays=st.number_input('pdays',min_value=-1.0, max_value=1000.0, value=1.0)
        Previous=st.number_input('previous',min_value=0.0, max_value=60.0, value=1.0)
        Poutcome=st.selectbox('poutcome'['unknown','failure','success'])
        Response=st.selectbox('response',['yes','no'])


        output=""
        input_dict={'age':age,'job':job,'marital':marital,'education':education,'default':default,'balance':balance,'housing':housing,'day':day,'month':month,'duration':duration,'campaign':campaign,'pdays':pdays,'previous':previous,'poutcome':poutcome,'response':response}
        input_df = pd.DataFrame([input_dict])
        if st.button(" predict eligible or not"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
            if output == '0' :
              output="SORRY! YOU ARE NOT ELIGIBLE FOR PERSONAL LOAN"
            else:
              output="CONGRATS! YOU ARE ELIGIBLE FOR PERSONAL LOAN"
        st.success('The Prediction   --  {}'.format(output))
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
