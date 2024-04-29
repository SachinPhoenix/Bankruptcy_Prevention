import streamlit as st
import pickle

# Load the model
load = open('model.pkl', 'rb')
model = pickle.load(load)
load.close()

def main():
    st.title('Bankruptcy Prevention App')

   

    def add_bg_from_url():
        st.markdown(
            f"""
             <style>
             .stApp {{
                 background-image: url('https://wallpaperbat.com/img/439560-e-clipart-banking-e-banking-transparent-free-for-download.png');
                 background-attachment: fixed;
                 background-size: cover
             }}
             </style>
             """,
            unsafe_allow_html=True
        )

    add_bg_from_url()
    st.markdown("<span style='font-size: 18px;'>Enter data for prediction:</span>", unsafe_allow_html=True)
    industrial_risk = st.slider('*Select Industrial Risk*', min_value=0.0, max_value=1.0, step=0.1, value=0.0,
                                format="%.2f")
    management_risk = st.slider('*Select Management Risk*', min_value=0.0, max_value=1.0, step=0.1, value=0.0)
    financial_flexibility = st.slider('*Select Financial Flexibility*', min_value=0.0, max_value=1.0, step=0.1,
                                      value=0.0)
    credibility = st.slider('*Select Credibility*', min_value=0.0, max_value=1.0, step=0.1, value=0.0)
    competitiveness = st.slider('*Select Competitiveness*', min_value=0.0, max_value=1.0, step=0.1, value=0.0)
    operating_risk = st.slider('*Select Operating Risk*', min_value=0.0, max_value=1.0, step=0.1, value=0.0)

    # Button to trigger prediction
    if st.button('Predict'):
        # Prepare the input data as a list
        data = [industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]

        prediction = model.predict([data])[0]

        if prediction == 0:
            st.success("### Prediction: Not Bankruptcy")
        else:
            st.error("### Prediction: Bankruptcy")

if _name_ == '_main_':
    main()
