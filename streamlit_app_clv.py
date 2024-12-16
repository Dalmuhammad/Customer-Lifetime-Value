import streamlit as st
import cloudpickle
import page_1
import page_2

st.title('Customer Lifetime Value')
st.write('By Muh. Afdal Abidin')

page = st.sidebar.radio("Pilih Halaman", ("Halaman 1", "Halaman 2"))

with open('model.pkl', 'rb') as file:
    data = cloudpickle.load(file)

pipeline = data['pipeline']
metrics = data['metrics']
prediction = data['prediction']
fitur_imp = data['feature_importance']

if page == "Halaman 1":
    page_1.show_metrics(metrics)
    page_1.show_plot(prediction)

elif page == "Halaman 2":
    page_2.single_prediction(pipeline)