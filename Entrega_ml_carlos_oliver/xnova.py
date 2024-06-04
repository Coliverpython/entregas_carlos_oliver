import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import joblib
import base64
from PIL import Image

import base64
import io

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()


# Cargar la imagen de fondo
background_image = Image.open('Marinas_Evening_Ships_Container_ship_553210_1280x884.jpg')

# Establecer la imagen de fondo con CSS
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/jpeg;base64,{image_to_base64(background_image)});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Cargar el modelo
best_model = joblib.load('best_model.pkl')

# Cargar el scaler ajustado y los label encoders
scaler = joblib.load('scaler.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# Título de la aplicación
st.title("Port Delay Prediction")

# Predefinir los valores posibles para las variables categóricas
countries = ['IT', 'CN', 'VN', 'IN']
shipper_names = ['GRANITIFIANDRE','JENNY', 'YOUTOOZ', 'CNE EXPRESS']
shipper_addresss = ['VIA RADICI NORD 112','1501 BLOCK A SHENZHOU BAIRUIDA BUILDING BANTIAN STREET LONGGANG DISTRICT', 'LEVEL 1 SHENZHEN INTL AIRPORT CARG SHENZHEN GUANGDONG', 'YANWEN EXPRESS 397 1 PINGLU ROAD ZHGUANGDONG SHANGHAI']
consignee_addresss = ['314 W SUPERIOR ST SUITE 201', 'PORT OF SAN DIEGO 10TH AV MARINE TERMINAL 850 WATER SSAN DIEGO CA UNITED STA92101', 'ONE BOWERMAN DRIVE BEAVERTON OR 97005', ' 4104 INDUSTRIAL PARKWAY DRIVE LEBEC CA 93243 UNITED STATES']
consignee_names = ['STONEPEAK CERAMICS', 'IKEA SUPPLY', 'DOLE FRESH FRUIT', 'GLOBAL ETRADE SERVICES']
product_descrip = ['CERAMIC TILES', 'COLLECTIBLE TOY', 'AUTOMOTIVE PARTS']
carrier_sasc_codes = ['GNSI, GOUGH & SONS INC', 'MAEU, MAERSK LINES, INC.', 'MEDU, BCSL US-MED LINE LTD.', 'CMDU, COMPAGNIE MARITIME DAFFRETEMEN']
vessel_names = ['MSC AZOV', 'KAIMANA HILA', 'COSCO NETHERLANDS', 'MANUKAI']
loading_ports = ['47537, LIVORNO', '57078, YANTIAN', '57035, SHANGHAI', '57020, NINGPO']
unloading_ports = ['1703, SAVANNAH, GA', '2704, LOS ANGELES, CA', '2709, LONG BEACH, CA', '4601, NEW YORK/NEWARK AREA, NEWARK, NJ']
container_types = ['2210', '45G1', '4510', '45G0']
place_of_receipt_v = ['CASTELLARANO', 'SHANGHAI', 'YANTIAN', 'NINGBO']

# Crear entradas para cada característica
country = st.selectbox("Country", countries)
weight = st.number_input("Weight", min_value=0.0)
quantity = st.number_input("Quantity", min_value=0)
shipper_name = st.selectbox("Shipper Name", shipper_names)
shipper_address = st.selectbox("Shipper Address", shipper_addresss)
consignee_name = st.selectbox("Consignee Name", consignee_names)
consignee_address = st.selectbox("Consignee Address", consignee_addresss)
product_desc = st.selectbox("Product Description", product_descrip)
estimate_arrival_date_year = st.number_input("Estimated Arrival Date Year", min_value=2024, max_value=2100)
estimate_arrival_date_month = st.number_input("Estimated Arrival Date Month", min_value=1, max_value=12)
estimate_arrival_date_day = st.number_input("Estimated Arrival Date Day", min_value=1, max_value=31)
carrier_sasc_code = st.selectbox("Carrier SASC Code", carrier_sasc_codes)
vessel_name = st.selectbox("Vessel Name", vessel_names)
inbond_type = st.number_input("Inbond Type", min_value=0.0)
loading_port = st.selectbox("Loading Port", loading_ports)
unloading_port = st.selectbox("Unloading Port", unloading_ports)
place_of_receipt = st.selectbox("Place of Receipt", place_of_receipt_v)
container_type = st.selectbox("Container Type", container_types)

data = pd.DataFrame({
    'country': [country],
    'weight': [weight],
    'shipper_name': [shipper_name],
    'shipper_address': [shipper_address],
    'consignee_name': [consignee_name],
    'consignee_address': [consignee_address],
    'product_desc': [product_desc],
    'carrier_sasc_code': [carrier_sasc_code],
    'vessel_name': [vessel_name],
    'inbond_type': [inbond_type],
    'loading_port': [loading_port],
    'unloading_port': [unloading_port],
    'place_of_receipt': [place_of_receipt],
    'quantity': [quantity],
    'container_type': [container_type],
    'estimate_arrival_date_year': [estimate_arrival_date_year],
    'estimate_arrival_date_month': [estimate_arrival_date_month],
    'estimate_arrival_date_day': [estimate_arrival_date_day]
})

# Asegurarse de que los nombres de las características coinciden con los usados durante el entrenamiento
expected_columns = [
    'country', 'weight', 'shipper_name', 'shipper_address', 'consignee_name',
    'consignee_address', 'product_desc', 'carrier_sasc_code', 'vessel_name', 'inbond_type',
    'loading_port', 'unloading_port', 'place_of_receipt', 'quantity', 'container_type',
    'estimate_arrival_date_year', 'estimate_arrival_date_month', 'estimate_arrival_date_day'

    ['country', 'weight', 'shipper_name', 'shipper_address',
       'consignee_name', 'consignee_address', 'product_desc',
       'carrier_sasc_code', 'vessel_name', 'inbond_type', 'loading_port',
       'unloading_port', 'place_of_receipt', 'quantity', 'container_type',
       'estimate_arrival_date_year', 'estimate_arrival_date_month',
       'estimate_arrival_date_day'
]
data = data[expected_columns]

# Codificar variables categóricas usando los encoders cargados
categorical_columns = data.select_dtypes(include=['object']).columns

le = LabelEncoder()
le.fit_transform(categorical_columns)



# Normalizar los datos usando el scaler cargado
data_scaled = scaler.transform(data)

if st.button("Predict"):
    # Convertir a DataFrame para mantener los nombres de las características
    data_scaled_df = pd.DataFrame(data_scaled, columns=expected_columns)
    prediction = best_model.predict(data_scaled_df)
    st.write("Prediction:", prediction[0])

