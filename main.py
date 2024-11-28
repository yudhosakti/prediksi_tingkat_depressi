"""
# My first app
Here's our first attempt at using data to create a table:
"""

import joblib
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

model = joblib.load(open('depression_model.sav', 'rb'))

st.title('Prediksi Tingkat Depresi Siswa')

#open file csv
df1 = pd.read_csv('student.csv')
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Pilih Menu",
    ("Deskripsi", "DataSet", "Grafik",'Prediksi')
)

# Fungsi untuk halaman Deskripsi
def show_deskripsi():
    st.write("Selamat datang di aplikasi prediksi tingkat depresi siswa.")
    st.write("<div style='text-align: justify;'>Aplikasi ini menggunakan teknologi <i>Machine Learning</i> dengan metode Random Forest Classification untuk memprediksi apakah siswa tersebut depresi atau tidak, dengan memasukkan parameter seperti umur,tekanan akademik, tekanan kerja,CGPA, kepuasan belajar, kepuasan pekerjaan,durasi tidur,kesehatan, keinginan bunuh diri, jam belajar, ekonomi,riwayat keluarga </div>", unsafe_allow_html=True)
    st.write("Sumber data: https://www.kaggle.com/datasets/hopesb/student-depression-dataset")
    st.write("Dibuat oleh Yudho Sakti Rama Sultan Alfaridzi NIM 223307028")

# Fungsi untuk halaman Dataset
def show_dataset():
    st.header("Dataset Student")
    dataNew = df1[['Gender', 'Age','Academic Pressure','Work Pressure','CGPA','Study Satisfaction','Job Satisfaction','Sleep Duration','Dietary Habits','Have you ever had suicidal thoughts ?','Work/Study Hours','Financial Stress','Family History of Mental Illness','Depression']]
    st.dataframe(dataNew)
    st.markdown("""
( 1 ) **Gender**
   - Terdiri dari Female dan Male yang akan menunjukkan jenis kelamin dari siswa.
  \n(
2 ) **Age**
   - Umur dari Sisw
  \n(
3 ) **Academic Pressure**
   - Tekanan akademik yang dialami siswa
  \n(
4 ) **Work Pressure**
   - Tekanan pekerjaan yang dialami siswa
  \n(
5 ) **CGPA**
   - Grade Point Average or other academic scores.
  \n(
6 ) **Dietary Habits**
   - Tingkat kesehatan dikelompokkan kedalam 4 kelompok ('Healty,Unhealthy,Moderate,Other)
   \n
7 ) **Have you ever had suicidal thoughts ?**
   - Apakah siswa pernah terpikir untuk bunuh diri
   \n
8 ) **Work/Study Hours**
   - jam belajar siswa
   \n
9 ) **Financial Stress**
   - Masalah ekonomi
   \n
10 ) **Family History of Mental Illness**
   - Riwayat Keluarga terkait kesehatan mental
   \n
""")

# Fungsi untuk halaman Grafik
def show_grafik():
    st.header("Grafik")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Umur", "CGPA", "Study Satisfaction", "Work/Study Hours", "Academic Pressure"])

    with tab1:
        # Input untuk jumlah bins pada histogram
        bins = st.slider("Pilih jumlah bins untuk histogram:", min_value=5, max_value=50, value=10,key='5')
        fig, ax = plt.subplots()
        ax.hist(df1['Age'], bins=bins, color='skyblue', edgecolor='black')
        ax.set_title("Histogram Distribusi Umur")
        ax.set_xlabel("Umur")
        ax.set_ylabel("Frekuensi")
        # Menampilkan plot di Streamlit
        st.pyplot(fig)

    with tab2:
        bins1 = st.slider("Pilih jumlah bins untuk histogram:", min_value=5, max_value=50, value=10,key='4')
        fig, ax = plt.subplots()
        ax.hist(df1['CGPA'], bins=bins1, color='skyblue', edgecolor='black')
        ax.set_title("Histogram Distribusi CGPA")
        ax.set_xlabel("CGPA")
        ax.set_ylabel("Frekuensi")
        # Menampilkan plot di Streamlit
        st.pyplot(fig)

    with tab3:
        bins2 = st.slider("Pilih jumlah bins untuk histogram:", min_value=5, max_value=50, value=10,key='3')
        fig, ax = plt.subplots()
        ax.hist(df1['Study Satisfaction'], bins=bins2, color='skyblue', edgecolor='black')
        ax.set_title("Histogram Distribusi Study Satisfaction")
        ax.set_xlabel("Study Satisfaction")
        ax.set_ylabel("Frekuensi")
        # Menampilkan plot di Streamlit
        st.pyplot(fig)

    with tab4:
        bins3 = st.slider("Pilih jumlah bins untuk histogram:", min_value=5, max_value=50, value=10,key='2')
        fig, ax = plt.subplots()
        ax.hist(df1['Work/Study Hours'], bins=bins3, color='skyblue', edgecolor='black')
        ax.set_title("Histogram Distribusi Work/Study Hours")
        ax.set_xlabel("Work/Study Hours")
        ax.set_ylabel("Frekuensi")
        # Menampilkan plot di Streamlit
        st.pyplot(fig)
    with tab5:
       bins4 = st.slider("Pilih jumlah bins untuk histogram:", min_value=5, max_value=50, value=10,key='1')
       fig, ax = plt.subplots()
       ax.hist(df1['Academic Pressure'], bins=bins4, color='skyblue', edgecolor='black')
       ax.set_title("Histogram Distribusi Academic Pressure")
       ax.set_xlabel("Academic Pressure")
       ax.set_ylabel("Frekuensi")
        # Menampilkan plot di Streamlit
       st.pyplot(fig)

def show_prediksi():
    st.header("Prediksi")
    st.write("Tentukan nilai-nilai pada variabel berikut untuk menentukan apakah siswa tersebut depresi atau tidak:")
    valueGender = 0
    valueHealty = 0
    valueSuicide = 0
    valueRiwayat= 0
    add_selectbox = st.selectbox(
    "Pilih Gender",
    ("Perempuan", "Laki-Laki"),key='200'
    )
    if add_selectbox == 'Perempuan':
       valueGender = 0
    else:
        valueGender = 1
    age = st.slider('Age', 1, 30, 100)
    academicPressure = st.slider('Academic Pressure:', 1, 3, 5)
    workPressure = st.slider('Work Pressure:', 0, 1)
    cgpa = st.slider('CGPA :', 1.0, 2.25, 10.0)
    studySatisfactionn = st.slider('Study Satisfaction:', 1, 2, 5)
    jobsatisfaction = st.slider('Job Satisfaction:', 0, 1)
    sleepduration = st.slider('Sleep Duration:', 1,2, 9)
    workstudy = st.slider('Work Study Duration:', 0.0,2.0, 10.0)
    financialStrees = st.slider('Financial Stress:', 0, 3, 5)
    healty = st.selectbox(
    "Pilih Kondisi Kesehatan",
    ("Healty", "Unhealthy",'Moderate','Other'),
    key='2001'
    )
    if healty == 'Healty':
       valueHealty = 3
    elif healty == 'Unhealthy':
        valueHealty = 2
    elif healty == 'Moderate':
        valueHealty = 1
    else:
        valueHealty = 0

    suicide = st.selectbox(
    "Apakah Anda Terpikir Untuk Bunuh Diri",
    ("Yes", "No"),
    key='3000'
    )
    if suicide == 'Yes':
       valueSuicide = 1
    else:
        valueSuicide = 0
        
    riwayat = st.selectbox(
    "Apakah Keluarga Anda Memiliki Riwayat Penyakit Mental",
    ("Yes", "No"),
    key='3022'
    )
    if riwayat == 'Yes':
       valueRiwayat = 1
    else:
        valueRiwayat = 0

    if st.button('Prediksi'):
        car_prediction = model.predict([[valueGender, age, academicPressure, workPressure, cgpa, studySatisfactionn,jobsatisfaction,sleepduration,valueHealty,valueSuicide,workstudy,financialStrees,valueRiwayat]])
        if car_prediction == 1:
            hasil = "Siswa Terindikasi Depresi"
        else:
            hasil = "Siswa Tidak Depresi"
        st.write('Hasil prediksi :', hasil)


print(add_selectbox)
if add_selectbox == "Deskripsi":
    show_deskripsi()
elif add_selectbox == "DataSet":
    show_dataset()
elif add_selectbox == "Grafik":
    show_grafik()
elif add_selectbox == "Prediksi":
    show_prediksi()

