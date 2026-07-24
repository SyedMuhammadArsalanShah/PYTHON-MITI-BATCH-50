import streamlit as st
import requests

# Title
st.title("📖 Quran Mushaf")

# API se Surah List
response = requests.get("https://api.alquran.cloud/v1/surah")
surahs = response.json()["data"]

# Sirf names ki list
options = []
for surah in surahs:
    options.append(f'{surah["number"]}. {surah["englishName"]}')

# Dropdown
selected = st.selectbox("Select Surah", options)

# Surah Number
surah_number = selected.split(".")[0]

# Ayahs Fetch
url = f"https://api.alquran.cloud/v1/surah/{surah_number}/ar.abdurrahmaansudais"
ayahs = requests.get(url).json()["data"]["ayahs"]

# Display Ayahs
for ayah in ayahs:
    st.write("Ayah:", ayah["numberInSurah"])
    st.write(ayah["text"])
    st.audio(ayah["audio"])
    st.divider()