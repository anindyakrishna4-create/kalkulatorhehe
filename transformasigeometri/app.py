import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="🔬 Virtual Lab Peluang Matematika",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("🔬 Virtual Lab Peluang Matematika")
    st.markdown("""
    Selamat datang di lab interaktif untuk memahami konsep **Peluang (Probabilitas)**. 
    Anda dapat mensimulasikan percobaan acak berkali-kali dan melihat bagaimana peluang empiris (hasil percobaan) mendekati peluang teoritis.
    """)
    st.markdown("---")

    # --- Pengaturan Layout dengan Tabs ---
    tab_koin, tab_dadu = st.tabs(["🪙 Pelemparan Koin", "🎲 Pelemparan Dadu"])
    
    # --- Tab 1: Simulasi Koin ---
    with tab_koin:
        st.header("🪙 Simulasi Pelemparan Koin")
        st.write("Pelemparan koin memiliki dua hasil yang mungkin: **Angka (A)** atau **Gambar (G)**. Peluang teoritis masing-masing adalah $P(A) = 0.5$ dan $P(G) = 0.5$.")
        
        # Kolom untuk Input Koin
        col_input_koin, col_visual_koin = st.columns([1, 1.5])

        with col_input_koin:
            st.subheader("Pengaturan Percobaan")
            n_koin = st.slider("Jumlah Pelemparan (N)", 10, 1000, 100, step=10, key='n_koin')
            st.markdown("---")
            
            # Button untuk menjalankan simulasi
            if st.button("Lakukan Simulasi Koin", key='run_koin'):
                # Simulasi: 0=Angka, 1=Gambar
                hasil_koin = np.random.randint(0, 2, n_koin)
                
                jumlah_angka = np.sum(hasil_koin == 0)
                jumlah_gambar = np.sum(hasil_koin == 1)
                
                # Peluang Empiris
                peluang_angka_empiris = jumlah_angka / n_koin
                peluang_gambar_empiris = jumlah_gambar / n_koin
                
                st.subheader("✅ Hasil Percobaan")
                st.info(f"Total Pelemparan: **{n_koin}** kali")
                st.metric(label="Jumlah Angka (A)", value=jumlah_angka)
                st.metric(label="Peluang Angka Empiris", value=f"{peluang_angka_empiris:.4f}", delta=f"Peluang Teoritis: 0.5")
                st.metric(label="Jumlah Gambar (G)", value=jumlah_gambar)
                st.metric(label="Peluang Gambar Empiris", value=f"{peluang_gambar_empiris:.4f}", delta=f"Peluang Teoritis: 0.5")
                
                # Simpan hasil untuk visualisasi
                st.session_state['hasil_koin'] = {
                    'n': n_koin,
                    'angka': jumlah_angka,
                    'gambar': jumlah_gambar,
                    'peluang_angka': peluang_angka_empiris
                }
            
            # Menampilkan hasil visualisasi jika simulasi sudah dijalankan
            if 'hasil_koin' in st.session_state:
                data = st.session_state['hasil_koin']
                
                with col_visual_koin:
                    st.subheader("📈 Visualisasi Hasil Koin")
                    
                    fig, ax = plt.subplots(figsize=(7, 5))
                    
                    hasil_labels = ['Angka', 'Gambar']
                    hasil_counts = [data['angka'], data['gambar']]
                    
                    # Membuat bar chart untuk jumlah hasil
                    ax.bar(hasil_labels, hasil_counts, color=['skyblue', 'lightcoral'])
                    ax.axhline(data['n'] / 2, color='green', linestyle='--', label='Harapan Teoritis (N/2)')
                    
                    ax.set_title(f"Distribusi Hasil dari {data['n']} Pelemparan")
                    ax.set_ylabel("Jumlah Hasil")
                    ax.legend()
                    st.pyplot(fig)
                    
                    # Scatter plot Peluang Empiris vs Teoritis
                    fig_peluang, ax_peluang = plt.subplots(figsize=(7, 5))
                    ax_peluang.scatter(['Angka', 'Gambar'], [data['peluang_angka'], 1 - data['peluang_angka']], color='blue', zorder=5)
                    ax_peluang.axhline(0.5, color='red', linestyle='-', label='Peluang Teoritis (0.5)')
                    ax_peluang.set_ylim(0, 1)
                    ax_peluang.set_title("Peluang Empiris vs. Teoritis")
                    ax_peluang.set_ylabel("Peluang")
                    ax_peluang.legend()
                    st.pyplot(fig_peluang)


    # --- Tab 2: Simulasi Dadu ---
    with tab_dadu:
        st.header("🎲 Simulasi Pelemparan Dadu Tunggal")
        st.write("Dadu memiliki enam hasil yang mungkin: 1, 2, 3, 4, 5, atau 6. Peluang teoritis setiap sisi adalah $P(x) = 1/6 \\approx 0.1667$.")
        
        # Kolom untuk Input Dadu
        col_input_dadu, col_visual_dadu = st.columns([1, 1.5])
        
        with col_input_dadu:
            st.subheader("Pengaturan Percobaan")
            n_dadu = st.slider("Jumlah Pelemparan (N)", 10, 1000, 200, step=10, key='n_dadu')
            target_sisi = st.selectbox("Pilih Sisi Target (A)", range(1, 7), key='target_sisi')
            st.markdown("---")
            
            if st.button("Lakukan Simulasi Dadu", key='run_dadu'):
                # Simulasi: hasil dari 1 sampai 6
                hasil_dadu = np.random.randint(1, 7, n_dadu)
                
                # Hitung frekuensi setiap sisi
                frekuensi = np.bincount(hasil_dadu)[1:] # [1:] karena dadu mulai dari 1
                
                # Total frekuensi untuk setiap sisi
                jumlah_target = frekuensi[target_sisi - 1]
                
                # Peluang Empiris
                peluang_target_empiris = jumlah_target / n_dadu
                
                st.subheader("✅ Hasil Percobaan")
                st.info(f"Total Pelemparan: **{n_dadu}** kali")
                st.metric(label=f"Jumlah Muncul Sisi {target_sisi}", value=jumlah_target)
                st.metric(label=f"Peluang Empiris $P({target_sisi})$", value=f"{peluang_target_empiris:.4f}", delta=f"Peluang Teoritis: 0.1667")
                
                # Simpan hasil untuk visualisasi
                st.session_state['hasil_dadu'] = {
                    'n': n_dadu,
                    'frekuensi': frekuensi,
                    'target': target_sisi,
                    'peluang_target': peluang_target_empiris
                }
                
            # Menampilkan hasil visualisasi jika simulasi sudah dijalankan
            if 'hasil_dadu' in st.session_state:
                data = st.session_state['hasil_dadu']
                
                with col_visual_dadu:
                    st.subheader("📈 Visualisasi Hasil Dadu")
                    
                    fig, ax = plt.subplots(figsize=(7, 5))
                    sisi = range(1, 7)
                    
                    # Bar chart frekuensi
                    ax.bar(sisi, data['frekuensi'], color='salmon')
                    ax.axhline(data['n'] / 6, color='darkgreen', linestyle='--', label='Harapan Teoritis (N/6)')
                    
                    ax.set_title(f"Distribusi Frekuensi dari {data['n']} Pelemparan Dadu")
                    ax.set_xlabel("Sisi Dadu")
                    ax.set_ylabel("Frekuensi Muncul")
                    ax.set_xticks(sisi)
                    ax.legend()
                    st.pyplot(fig)

# Menjalankan fungsi utama
if __name__ == '__main__':
    main()
