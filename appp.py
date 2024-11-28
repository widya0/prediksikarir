import pickle

import numpy as np
import streamlit as st
import pandas as pd
import os


# Load model dari file .pkl
try:
    with open('karir.pkl', 'rb') as file:
        model = pickle.load(file)
        label_mapping = {
            1: 'Applications Developer',
            2: 'CRM Technical Developer',
            3: 'Database Developer',
            4: 'Mobile Applications Developer',
            5: 'Network Security Engineer',
            6: 'Software Developer',
            7: 'Software Engineer',
            8: 'Software Quality Assurance (QA) / Testing',
            9: 'Systems Security Administrator',
            10: 'Technical Support',
            11: 'UX Designer',
            12: 'Web Developer',
        }
    print("Model loaded successfully!")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")

print(type(model))

# Load label encoders
try:
    with open('label_encoders.pkl', 'rb') as file:
        label_encoders = pickle.load(file)
    with open('y_encoder.pkl', 'rb') as file:
        y_encoder = pickle.load(file)
    print("Encoders loaded successfully!")
except Exception as e:
    print(f"An error occurred while loading the encoders: {e}")

# Data contoh untuk visualisasi (sesuaikan dengan dataset asli)

# Membaca DataFrame dari file Excel lokal
try:
    # Ganti "mldata.xls" dengan path file Excel Anda
    df = pd.read_csv('mldata.csv')

    # Kolom yang diambil dari file Excel
    selected_columns = [
        'Logical quotient rating',
        'hackathons',
        'coding skills rating',
        'public speaking points',
        'self-learning capability?',
        'Extra-courses did',
        'certifications',
        'workshops',
        'reading and writing skills',
        'memory capability score',
        'Interested subjects',
        'interested career area ',
        'Type of company want to settle in?',
        'Taken inputs from seniors or elders',
        'Interested Type of Books',
        'Management or Technical',
        'hard/smart worker',
        'worked in teams ever?',
        'Introvert',
        'Suggested Job Role'
    ]

    # Memfilter kolom yang diperlukan
    if all(col in df.columns for col in selected_columns):
        df1 = df[selected_columns]
    else:
        missing_columns = [col for col in selected_columns if col not in df.columns]
        st.error(f"Kolom berikut tidak ditemukan dalam file Excel: {missing_columns}")
        df1 = None
except FileNotFoundError:
    st.error("File 'mldata.xls' tidak ditemukan. Pastikan file tersedia di direktori yang benar.")
    df1 = None
except Exception as e:
    st.error(f"Terjadi kesalahan saat membaca file Excel: {e}")
    df1 = None

st.title('Aplikasi Prediksi Peran Pekerjaan')

# Fungsi untuk halaman Deskripsi
def show_deskripsi():
    st.write("""
    <div style='text-align: justify;'>Aplikasi ini menggunakan <i>Machine Learning</i> untuk memprediksi peran pekerjaan berdasarkan kemampuan, pengalaman, dan preferensi individu. 
    Dengan memasukkan data seperti penilaian logis, pengalaman hackathon, kemampuan berbicara di depan umum, dan sertifikasi, 
    aplikasi ini memberikan rekomendasi pekerjaan yang sesuai. Gunakan fitur ini untuk menemukan jalur karir yang cocok!</div>
    """, unsafe_allow_html=True)
    st.write("")

# Fungsi untuk halaman Dataset
def show_dataset():
    st.header("Dataset")
    st.dataframe(df1)

# Fungsi untuk halaman Grafik
def show_grafik():
    st.header("Grafik")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["certifications", "workshops", "reading and writing skills", "memory capability score", "Interested subjects", "interested career area ", "Type of company want to settle in?", "Interested Type of Books", "Management or Technical", "Suggested Job Role"])

    with tab1:
        st.bar_chart(df1['certifications'])
    with tab2:
        st.line_chart(df1['workshops'])
    with tab3:
        st.area_chart(df1['reading and writing skills'])
    with tab4:
        st.bar_chart(df1['memory capability score'])
    with tab5:
        st.line_chart(df1['Interested subjects'])
    with tab6:
        st.area_chart(df1['interested career area '])
    with tab7:
        st.bar_chart(df1['Type of company want to settle in?'])
    with tab8:
        st.line_chart(df1['Interested Type of Books'])
    with tab9:
        st.area_chart(df1['Management or Technical'])
    with tab10:
        st.bar_chart(df1['Suggested Job Role'])

# Fungsi untuk halaman Prediksi
def show_prediksi():
    st.header("Prediksi Peran Pekerjaan")
    st.write("Tentukan nilai-nilai berikut untuk memprediksi peran pekerjaan yang cocok:")

    # Input data pengguna
    logical_quotient = st.slider('Logical quotient rating:', 1, 10, 5)
    hackathons = st.slider('Hackathons:', 1, 10, 2)
    coding_skills = st.slider('Coding skills rating:', 1, 10, 6)
    public_speaking = st.slider('Public speaking points:', 1, 10, 5)

    self_learning_capability = st.radio('Self-learning capability?', ['Yes', 'No'])
    extra_courses = st.radio('Extra-courses did?', ['Yes', 'No'])
    taken_inputs = st.radio('Taken inputs from seniors or elders?', ['Yes', 'No'])
    worked_in_teams = st.radio('Worked in teams ever?', ['Yes', 'No'])
    introvert = st.radio('Introvert?', ['Yes', 'No'])

    # Input kategori lainnya
    interested_career_area = st.selectbox('Interested Career Area:', ['system developer', 'security', 'Business process analyst', 'developer', 'testing', 'cloud computing'])
    interested_subjects = st.selectbox('Interested Subjects:', ['Software Engineering', 'IOT', 'cloud computing', 'programming', 'networks', 'Computer Architecture', 'data engineering', 'hacking', 'Management', 'parallel computing'])
    workshops = st.selectbox('Workshops:', ['database security', 'system designing', 'web technologies', 'hacking', 'testing', 'data science', 'game development', 'cloud computing'])
    certifications = st.selectbox('Certifications:', ['r programming', 'information security', 'shell programming', 'machine learning', 'full stack', 'hadoop', 'python', 'distro making', 'app development'])
    reading_writing_skills = st.selectbox('Reading and writing skills:', ['excellent', 'medium', 'poor'])
    memory_capability = st.selectbox('Memory capability score:', ['excellent', 'medium', 'poor'])
    management_or_technical = st.selectbox('Management or Technical:', ['Management', 'Technical'])
    hard_smart_worker = st.selectbox('Hard/Smart worker:', ['hard worker', 'smart worker'])
    type_of_company = st.selectbox('Type of Company:', ['Service Based', 'Web Services', 'BPA', 'Testing and Maintenance Services', 'Product based', 'Finance', 'Cloud Services', 'product development', 'Sales and Marketing', 'SAaS services'])
    interested_books = st.selectbox('Interested Books:', ['Guide', 'Health', 'Horror', 'Self help', 'Biographies', 'Science fiction', 'Satire', 'Childrens', 'Autobiographies', 'Prayer books', 'Fantasy', 'Journals', 'Trilogy', 'Anthology', 'Encyclopedias', 'Drama', 'Mystery', 'History', 'Science', 'Dictionaries', 'Religion-Spirituality', 'Diaries', 'Action and Adventure', 'Poetry', 'Comics', 'Travel', 'Art', 'Cookbooks', 'Series', 'Math', 'Romance'])

    # Mapping input menjadi numerik
    self_learning_capability = 1 if self_learning_capability == 'Yes' else 0
    extra_courses = 1 if extra_courses == 'Yes' else 0
    taken_inputs = 1 if taken_inputs == 'Yes' else 0
    worked_in_teams = 1 if worked_in_teams == 'Yes' else 0
    introvert = 1 if introvert == 'Yes' else 0

    reading_writing_skills = {'excellent': 3, 'medium': 2, 'poor': 1}[reading_writing_skills]
    memory_capability = {'excellent': 3, 'medium': 2, 'poor': 1}[memory_capability]
    management_or_technical = 1 if management_or_technical == 'Management' else 0
    hard_smart_worker = 1 if hard_smart_worker == 'smart worker' else 0

    # Mapping pilihan ke kategori numerik
    career_area_mapping = {'system developer': 0, 'security': 1, 'Business process analyst': 2, 'developer': 3, 'testing': 4, 'cloud computing': 5}
    interested_books_mapping = {'Guide': 0, 'Health': 1, 'Horror': 2, 'Self help': 3, 'Biographies': 4, 'Science fiction': 5, 'Satire': 6, 'Childrens': 7, 'Autobiographies': 8, 'Prayer books': 9, 'Fantasy': 10, 'Journals': 11, 'Trilogy': 12, 'Anthology': 13, 'Encyclopedias': 14, 'Drama': 15, 'Mystery': 16, 'History': 17, 'Science': 18, 'Dictionaries': 19, 'Religion-Spirituality': 20, 'Diaries': 21, 'Action and Adventure': 22, 'Poetry': 23, 'Comics': 24, 'Travel': 25, 'Art': 26, 'Cookbooks': 27, 'Series': 28, 'Math': 29, 'Romance': 30}
    subject_mapping = {'Software Engineering': 0, 'IOT': 1, 'cloud computing': 2, 'programming': 3, 'networks': 4, 'Computer Architecture': 5, 'data engineering': 6, 'hacking': 7, 'Management': 8, 'parallel computing': 9}
    workshops_mapping = {'database security': 0, 'system designing': 1, 'web technologies': 2, 'hacking': 3, 'testing': 4, 'data science': 5, 'game development': 6, 'cloud computing': 7}
    certifications_mapping = {'r programming': 0, 'information security': 1, 'shell programming': 2, 'machine learning': 3, 'full stack': 4, 'hadoop': 5, 'python': 6, 'distro making': 7, 'app development': 8}
    type_of_company_mapping = {'Service Based': 0, 'Web Services': 1, 'BPA': 2, 'Testing and Maintenance Services': 3, 'Product based': 4, 'Finance': 5, 'Cloud Services': 6, 'product development': 7, 'Sales and Marketing': 8, 'SAaS services': 9}

    # Mapping data ke angka
    interested_career_area = career_area_mapping[interested_career_area]
    interested_books = interested_books_mapping[interested_books]
    interested_subjects = subject_mapping[interested_subjects]
    workshops = workshops_mapping[workshops]
    certifications = certifications_mapping[certifications]
    type_of_company = type_of_company_mapping[type_of_company]

    input_array = np.array([[logical_quotient, hackathons, coding_skills, public_speaking, self_learning_capability,
                              extra_courses, certifications, workshops, reading_writing_skills, memory_capability,
                              interested_subjects, interested_career_area, type_of_company, taken_inputs,
                              interested_books, management_or_technical, hard_smart_worker, worked_in_teams, introvert]])

    if st.button("Prediksi"):
        try:
            # Prediksi
            prediction = model.predict(input_array)
            label = label_mapping.get(prediction[0], "Label tidak ditemukan")
            st.success(f"Hasil prediksi: {label}")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

# Menu sidebar
menu = st.sidebar.selectbox("Pilih Menu", ["Deskripsi", "Dataset", "Grafik", "Prediksi"])

if menu == "Deskripsi":
    show_deskripsi()
elif menu == "Dataset":
    show_dataset()
elif menu == "Grafik":
    show_grafik()
elif menu == "Prediksi":
    show_prediksi()
