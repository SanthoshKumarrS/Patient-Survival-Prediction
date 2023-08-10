from tensorflow import keras
from prediction import pred
import streamlit as st 
import numpy as np

model = keras.models.load_model('C:\Santhosh\Patient-Survival-Prediction-Project\Model\patient_model_at_epoch_20.h5')



def main():
    st.header('Patient Survival Prediction')

    st.write('The model was trained on the Patient Survival Dataset')

    st.subheader('Input the Data')
    st.write('Please input the data below')

    i = st.slider('age',0,100,25)
    j = st.selectbox('ventilated_apache',(0,1))
    k = st.selectbox('isin_med-surg icu',(0,1))
    l = st.slider('d1_bun_min',0,100,25)
    m = st.number_input('d1_hemaglobin_min',)
    n = st.slider('d1_spo2_min',0,200,85)


    input = np.array([[i,j,k,l,m,n]])
    print(type(i))
    print(input)
    
    
    if st.button("Find out patient's survival"):
        predi = pred(model,[i,j,k,l,m,n])
        st.success('The prediction is alive' if predi==0 else 'The prediction is dead')

     
if __name__ == '__main__':

    main()