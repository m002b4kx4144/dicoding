import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DATASET
@st.cache_data
def load_data():
    hour_clean = pd.read_csv('hour_clean.csv')
    day = pd.read_csv('day.csv')
    return hour_clean, day

hour_clean, day = load_data()

# Filter Sidebar
with st.sidebar:
    st.header('Pilihan Filter')

    # Musim
    opsi_musim = {
        1: 'Musim Semi',
        2: 'Musim Panas',
        3: 'Musim Gugur',
        4: 'Musim Dingin'
    }
    musim_terpilih = st.multiselect('Pilih Musim', options=list(opsi_musim.keys()),
                                    format_func=lambda x: opsi_musim[x], default=list(opsi_musim.keys()))

    # Hari dalam Minggu
    opsi_hari = {
        0: 'Minggu',
        1: 'Senin',
        2: 'Selasa',
        3: 'Rabu',
        4: 'Kamis',
        5: 'Jumat',
        6: 'Sabtu'
    }
    hari_terpilih = st.multiselect('Pilih Hari dalam Minggu', options=list(opsi_hari.keys()),
                                   format_func=lambda x: opsi_hari[x], default=list(opsi_hari.keys()))

# Filter data berdasarkan pilihan
hour_clean_terfilter = hour_clean[hour_clean['season'].isin(musim_terpilih) & 
                                  hour_clean['weekday'].isin(hari_terpilih)]
day_terfilter = day[day['season'].isin(musim_terpilih) & 
                    day['weekday'].isin(hari_terpilih)]

st.title('Dashboard Analisis Peminjaman Sepeda')

st.write("""
Dashboard ini menjawab pertanyaan-pertanyaan kunci terkait tren peminjaman sepeda berdasarkan waktu, musim, cuaca, dan faktor lainnya.
Gunakan filter di sidebar untuk menyesuaikan data yang ditampilkan.
""")

# Membuat tab
tab1, tab2 = st.tabs(["Kapan peminjaman sepeda paling tinggi?", 
                      "Pengaruh Cuaca dan Faktor Lainnya"])

with tab1:
    st.header("Kapan peminjaman sepeda paling tinggi?")
    st.write("""
    Jelajahi tren peminjaman sepeda berdasarkan waktu dalam sehari, musim, dan hari dalam seminggu.
    """)

    # Memilih analisis yang ingin dilihat
    opsi_analisis = st.selectbox(
        'Pilih Analisis:',
        ('Rata-rata Jumlah Sepeda yang Dipinjam Per Jam Berdasarkan Waktu dalam Sehari',
         'Rata-rata Jumlah Sepeda yang Dipinjam Per Jam Berdasarkan Musim (Data Hour)',
         'Rata-rata Jumlah Sepeda yang Dipinjam Per Hari Berdasarkan Musim (Data Day)',
         'Rata-rata Jumlah Sepeda yang Dipinjam Per Jam Berdasarkan Hari dalam Minggu (Data Hour)',
         'Rata-rata Jumlah Sepeda yang Dipinjam Per Hari Berdasarkan Hari dalam Minggu (Data Day)',
         'Rata-rata Peminjaman Sepeda per Jam: Hari Kerja vs Akhir Pekan')
    )

    if opsi_analisis == 'Rata-rata Jumlah Sepeda yang Dipinjam Per Jam Berdasarkan Waktu dalam Sehari':
        st.subheader(opsi_analisis)
        # Grafik garis: Rata-rata sepeda yang dipinjam per jam dalam sehari
        peminjaman_per_jam = hour_clean_terfilter.groupby('hr')['cnt'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(x='hr', y='cnt', data=peminjaman_per_jam, marker='o', ax=ax)
        ax.set_title('Rata-rata Peminjaman Sepeda per Jam (0-23)')
        ax.set_xlabel('Jam dalam Sehari')
        ax.set_ylabel('Rata-rata Jumlah Sepeda yang Dipinjam')
        ax.grid(True)
        st.pyplot(fig)
    elif opsi_analisis == 'Rata-rata Jumlah Sepeda yang Dipinjam Per Jam Berdasarkan Musim (Data Hour)':
        st.subheader(opsi_analisis)
        # Grafik batang: Rata-rata sepeda yang dipinjam per jam berdasarkan musim
        peminjaman_musim = hour_clean_terfilter.groupby('season')['cnt'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x='season', y='cnt', data=peminjaman_musim, palette='coolwarm', ax=ax)
        ax.set_title('Rata-rata Peminjaman Sepeda per Musim (Data Hour)')
        ax.set_xlabel('Musim')
        ax.set_xticklabels([opsi_musim[s] for s in peminjaman_musim['season']])
        ax.set_ylabel('Rata-rata Jumlah Sepeda yang Dipinjam')
        ax.grid(True)
        st.pyplot(fig)
    elif opsi_analisis == 'Rata-rata Jumlah Sepeda yang Dipinjam Per Hari Berdasarkan Musim (Data Day)':
        st.subheader(opsi_analisis)
        # Grafik batang: Rata-rata sepeda yang dipinjam per hari berdasarkan musim
        hari_musim = day_terfilter.groupby('season')['cnt'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x='season', y='cnt', data=hari_musim, palette='coolwarm', ax=ax)
        ax.set_title('Rata-rata Peminjaman Sepeda per Musim (Data Day)')
        ax.set_xlabel('Musim')
        ax.set_xticklabels([opsi_musim[s] for s in hari_musim['season']])
        ax.set_ylabel('Rata-rata Jumlah Sepeda yang Dipinjam')
        ax.grid(True)
        st.pyplot(fig)
    elif opsi_analisis == 'Rata-rata Jumlah Sepeda yang Dipinjam Per Jam Berdasarkan Hari dalam Minggu (Data Hour)':
        st.subheader(opsi_analisis)
        # Grafik batang: Rata-rata sepeda yang dipinjam per jam berdasarkan hari dalam minggu
        peminjaman_hari = hour_clean_terfilter.groupby('weekday')['cnt'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x='weekday', y='cnt', data=peminjaman_hari, palette='viridis', ax=ax)
        ax.set_title('Rata-rata Peminjaman Sepeda per Hari dalam Minggu (Data Hour)')
        ax.set_xlabel('Hari dalam Minggu')
        ax.set_xticklabels([opsi_hari[wd] for wd in peminjaman_hari['weekday']])
        ax.set_ylabel('Rata-rata Jumlah Sepeda yang Dipinjam')
        ax.grid(True)
        st.pyplot(fig)
    elif opsi_analisis == 'Rata-rata Jumlah Sepeda yang Dipinjam Per Hari Berdasarkan Hari dalam Minggu (Data Day)':
        st.subheader(opsi_analisis)
        # Grafik batang: Rata-rata sepeda yang dipinjam per hari berdasarkan hari dalam minggu
        hari_minggu = day_terfilter.groupby('weekday')['cnt'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x='weekday', y='cnt', data=hari_minggu, palette='viridis', ax=ax)
        ax.set_title('Rata-rata Peminjaman Sepeda per Hari dalam Minggu (Data Day)')
        ax.set_xlabel('Hari dalam Minggu')
        ax.set_xticklabels([opsi_hari[wd] for wd in hari_minggu['weekday']])
        ax.set_ylabel('Rata-rata Jumlah Sepeda yang Dipinjam')
        ax.grid(True)
        st.pyplot(fig)
    elif opsi_analisis == 'Rata-rata Peminjaman Sepeda per Jam: Hari Kerja vs Akhir Pekan':
        st.subheader(opsi_analisis)
        # Grafik garis peminjaman sepeda per jam untuk hari kerja vs akhir pekan
        hari_kerja = [0, 1, 2, 3, 4]
        akhir_pekan = [5, 6]
        data_hari_kerja = hour_clean_terfilter[hour_clean_terfilter['weekday'].isin(hari_kerja)].groupby('hr')['cnt'].mean()
        data_akhir_pekan = hour_clean_terfilter[hour_clean_terfilter['weekday'].isin(akhir_pekan)].groupby('hr')['cnt'].mean()
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(x=data_hari_kerja.index, y=data_hari_kerja.values, label='Hari Kerja', ax=ax)
        sns.lineplot(x=data_akhir_pekan.index, y=data_akhir_pekan.values, label='Akhir Pekan', ax=ax)
        ax.set_title('Rata-rata Peminjaman Sepeda per Jam: Hari Kerja vs Akhir Pekan')
        ax.set_xlabel('Jam dalam Sehari')
        ax.set_ylabel('Rata-rata Jumlah Sepeda yang Dipinjam')
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

with tab2:
    st.header("Pengaruh Cuaca, Suhu, Kelembaban, dan Kecepatan Angin terhadap Peminjaman Sepeda")
    st.write("""
    Analisis bagaimana kondisi cuaca mempengaruhi jumlah sepeda yang dipinjam.
    """)

    opsi_analisis = st.selectbox(
        'Pilih Analisis:',
        ('Matriks Korelasi untuk Data Hour',
         'Matriks Korelasi untuk Data Day',
         'Diagram Pencar: Peminjaman Sepeda vs Suhu (Data Hour)',
         'Diagram Pencar: Peminjaman Sepeda vs Suhu (Data Day)',
         'Diagram Pencar: Peminjaman Sepeda vs Suhu Udara (Data Hour)',
         'Diagram Pencar: Peminjaman Sepeda vs Suhu Udara (Data Day)')
    )

    if opsi_analisis == 'Matriks Korelasi untuk Data Hour':
        st.subheader(opsi_analisis)
        # Matriks korelasi untuk data per jam
        matriks_korelasi_hour = hour_clean_terfilter[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(matriks_korelasi_hour, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
        ax.set_title('Matriks Korelasi (Data Hour)')
        st.pyplot(fig)
    elif opsi_analisis == 'Matriks Korelasi untuk Data Day':
        st.subheader(opsi_analisis)
        # Matriks korelasi untuk data per hari
        matriks_korelasi_day = day_terfilter[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(matriks_korelasi_day, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
        ax.set_title('Matriks Korelasi (Data Day)')
        st.pyplot(fig)
    elif opsi_analisis == 'Diagram Pencar: Peminjaman Sepeda vs Suhu (Data Hour)':
        st.subheader(opsi_analisis)
        # Diagram pencar peminjaman sepeda per jam terhadap suhu
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(x='temp', y='cnt', data=hour_clean_terfilter, alpha=0.5, ax=ax)
        ax.set_title('Peminjaman Sepeda per Jam vs. Suhu (Data Hour)')
        ax.set_xlabel('Suhu (temp)')
        ax.set_ylabel('Peminjaman Sepeda')
        ax.grid(True)
        st.pyplot(fig)
    elif opsi_analisis == 'Diagram Pencar: Peminjaman Sepeda vs Suhu (Data Day)':
        st.subheader(opsi_analisis)
        # Diagram pencar peminjaman sepeda per hari terhadap suhu
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(x='temp', y='cnt', data=day_terfilter, alpha=0.5, ax=ax)
        ax.set_title('Peminjaman Sepeda per Hari vs. Suhu (Data Day)')
        ax.set_xlabel('Suhu (temp)')
        ax.set_ylabel('Peminjaman Sepeda')
        ax.grid(True)
        st.pyplot(fig)
    elif opsi_analisis == 'Diagram Pencar: Peminjaman Sepeda vs Suhu Udara (Data Hour)':
        st.subheader(opsi_analisis)
        # Diagram pencar peminjaman sepeda per jam terhadap suhu udara
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(x='atemp', y='cnt', data=hour_clean_terfilter, alpha=0.5, ax=ax)
        ax.set_title('Peminjaman Sepeda per Jam vs. Suhu Udara (Data Hour)')
        ax.set_xlabel('Suhu Udara (atemp)')
        ax.set_ylabel('Peminjaman Sepeda')
        ax.grid(True)
        st.pyplot(fig)
    elif opsi_analisis == 'Diagram Pencar: Peminjaman Sepeda vs Suhu Udara (Data Day)':
        st.subheader(opsi_analisis)
        # Diagram pencar peminjaman sepeda per hari terhadap suhu udara
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(x='atemp', y='cnt', data=day_terfilter, alpha=0.5, ax=ax)
        ax.set_title('Peminjaman Sepeda per Hari vs. Suhu Udara (Data Day)')
        ax.set_xlabel('Suhu Udara (atemp)')
        ax.set_ylabel('Peminjaman Sepeda')
        ax.grid(True)
        st.pyplot(fig)
