from email.message import Message
import imp
import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np

st.title("Bank Transaction Fraud Detetcion App")

step = st.number_input('step', 0, 1220000, 10)
type = st.selectbox('type', ['CASH_IN', 'CASH_OUT','DEBIT', 'PAYMENT','TRANSFER'])
amount = st.number_input('amount', 0, 1220000)
oldbalanceOrg = st.number_input('oldbalanceOrg', 0, 10000000,2)
newbalanceOrig = st.number_input('newbalanceOrig', 0, 10000000,2)
oldbalanceDest = st.number_input('oldbalanceDest', 0, 10000000,2)
newbalanceDest = st.number_input('newbalanceDest', 0, 10000000,2)

dict_ = {
            "step": [step],
            "type": [type],
            "amount": [amount],
            "oldbalanceOrg":[oldbalanceOrg],
            "newbalanceOrig": [newbalanceOrig],
            "oldbalanceDest": [oldbalanceDest],
            "newbalanceDest": [newbalanceDest]
        }

results = pd.DataFrame(dict_)

with open('./pickle/model.pkl', 'rb') as file:
    data = pickle.load(file)

ok = st.button("Predict")

if ok:
    if data.predict(results)[0] == 0:
        Message == "not Fraud"
    else:
         Message == "Fraud"
    st.write('Acount is',Message)
  
