import streamlit as st
import pickle
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Load the model
load = open('model.pkl', 'rb')
model = pickle.load(load)
load.close()

# Prediction function
def predict(Industrial_Risk, Management_Risk, Financial_Flexibility, Credibility, Competitiveness, Operating_Risk):
    try:
        prediction = model.predict([[Industrial_Risk, Management_Risk, Financial_Flexibility, Credibility, Competitiveness, Operating_Risk]])
        return prediction[0]  # Use prediction[0] to get the actual prediction value
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


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

    if st.button('Predict'):
        Result = predict(Industrial_Risk, Management_Risk, Financial_Flexibility, Credibility, Competitiveness, Operating_Risk)
        if Result == 0:
            st.markdown('<h1 style="color: red; font-size: 36px;">Prediction: Bankruptcy</h1>', unsafe_allow_html=True)
        else:
            st.markdown('<h1 style="color: green; font-size: 36px;">Prediction: Non-Bankruptcy</h1>', unsafe_allow_html=True)

if _name_ == '_main_':
    main()
