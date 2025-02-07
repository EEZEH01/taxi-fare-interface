import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Select the parameters of the ride
'''

date = st.date_input("Pickup date", datetime.date(2023, 1, 1))
time = st.time_input("Pickup time", datetime.time(12, 0))
pickup_longitude = st.number_input("Pickup longitude", -74.00)
pickup_latitude = st.number_input("Pickup latitude", 40.75)
dropoff_longitude = st.number_input("Dropoff longitude", -73.95)
dropoff_latitude = st.number_input("Dropoff latitude", 40.78)
passenger_count = st.slider("Passenger count", 1, 6, 1)

datetime_str = f"{date} {time}"

url = 'https://taxifare.lewagon.ai/predict'

if st.button("Predict fare"):
    # 2. Construir un diccionario con los parámetros
    params = {
        "pickup_datetime": datetime_str,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # 3. Hacer la solicitud a la API usando el paquete `requests`
    response = requests.get(url, params=params)
    prediction = response.json()

    # Imprimir la respuesta para verificar su contenido
    st.write(prediction)

    # 4. Mostrar la predicción al usuario (si existe)
    if 'fare_amount' in prediction:
        st.write(f"The predicted fare is: ${prediction['fare_amount']:.2f}")
    else:
        st.write("Error: 'fare_amount' key not found in the response.")

