import pickle
import streamlit as st

# Load the pickled model
model = pickle.load(open('stunting.pkl', 'rb'))

# Define the main function
def main():
    # Set the title of the app
    st.title('Status Gizi Balita')

    # Get the input features from the user
    age = st.number_input('Umur (bulan)', min_value=0, max_value=72)
    gender = st.selectbox('Jenis Kelamin', ['Perempuan', 'Laki-laki'])
    height = st.number_input('Tinggi Badan (cm)', min_value=0.0, max_value=100.0)

    # Encode the gender
    if gender == 'Perempuan':
        gender_encoded = 0
    else:
        gender_encoded = 1

    # Create a list of input features
    input_features = [age, gender_encoded, height]

    # Make a prediction
    prediction = model.predict([input_features])

    # Display the prediction
    if st.button('Prediksi'):
        if prediction[0] == 'stunted':
            st.write('Status gizi balita: stunting')
        elif prediction[0] == 'tall':
            st.write('Status gizi balita: tinggi')
        elif prediction[0] == 'normal':
            st.write('Status gizi balita: normal')
        else:
            st.write('Status gizi balita: sangat pendek')

# Run the main function
if __name__ == '__main__':
    main()
