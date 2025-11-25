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
    Selamat datang! Lab ini dirancang untuk mengilustrasikan **Hukum Bilangan Besar** (Law of Large Numbers), 
    yaitu bagaimana peluang empiris (hasil percobaan) semakin mendekati peluang teoritis ketika **jumlah percobaan (N) ditingkatkan**.
    """)
    st.markdown("---")

    # --- Pengaturan Layout dengan Tabs ---
    tab_koin, tab_dadu = st.tabs(["🪙 Pelemparan Koin", "🎲 Pelemparan Dadu"])
    
    # --- Tab 1: Simulasi Koin ---
    with tab_koin:
        st.header("🪙 Simulasi Pelemparan Koin")
        st.info("Peluang Teoritis: Angka ($P(A)$) dan Gambar ($P(G)$) masing-masing adalah $0.5$ (50%).")
        
        # Kolom untuk Input Koin
        col_input_koin, col_visual_koin = st.columns([1, 1.5])

        with col_input_koin:
            st.subheader("1. Pengaturan Percobaan")
            st.markdown("*Gunakan slider untuk menentukan berapa kali koin akan dilempar secara virtual.*")
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
                
                st.subheader("2. Hasil Percobaan (Peluang Empiris)")
                st.info(f"Total Pelemparan: **{n_koin}** kali")
                
                st.metric(label="Jumlah Angka (A)", value=jumlah_angka)
                st.metric(label="Peluang Angka Empiris", value=f"{peluang_angka_empiris:.4f}", delta=f"Teoritis: 0.5")
                st.metric(label="Jumlah Gambar (G)", value=jumlah_gambar)
                st.metric(label="Peluang Gambar Empiris", value=f"{peluang_gambar_empiris:.4f}", delta=f"Teoritis: 0.5")
                
                # Simpan hasil untuk visualisasi
                st.session_state['hasil_koin'] = {
                    'n': n_koin,
                    'angka': jumlah_angka,
                    'gambar': jumlah_gambar,
                    'peluang_angka': peluang_angka_empiris
                }
            
            # Panduan Tambahan
            st.markdown("---")
            st.subheader("💡 Panduan Penggunaan")
            st.markdown("1. **Mulai dari N kecil** (misalnya 100), lalu jalankan simulasi.")
            st.markdown("2. **Perhatikan** perbedaan antara Peluang Empiris dan Teoritis.")
            st.markdown("3. **Tingkatkan N** (misalnya menjadi 1000) dan ulangi simulasi.")
            st.markdown("4. **Amati**, semakin besar N, peluang empiris seharusnya semakin dekat ke 0.5 (hukum bilangan besar).")


        # Menampilkan hasil visualisasi jika simulasi sudah dijalankan
        if 'hasil_koin' in st.session_state:
            data = st.session_state['hasil_koin']
            
            with col_visual_koin:
                st.subheader("3. Visualisasi Hasil Koin")
                
                # 3a. Plot Frekuensi
                st.caption("Grafik menunjukkan frekuensi muncul Angka dan Gambar dibandingkan harapan teoritis.")
                fig, ax = plt.subplots(figsize=(7, 4))
                
                hasil_labels = ['Angka', 'Gambar']
                hasil_counts = [data['angka'], data['gambar']]
                
                ax.bar(hasil_labels, hasil_counts, color=['skyblue', 'lightcoral'])
                ax.axhline(data['n'] / 2, color='green', linestyle='--', label='Harapan Teoritis')
                
                ax.set_title(f"Frekuensi Hasil dari {data['n']} Pelemparan")
                ax.set_ylabel("Jumlah Hasil")
                ax.legend()
                st.pyplot(fig)
                
                # 3b. Plot Peluang
                st.caption("Titik biru menunjukkan seberapa dekat Peluang Empiris dengan garis Peluang Teoritis (0.5).")
                fig_peluang, ax_peluang = plt.subplots(figsize=(7, 4))
                ax_peluang.scatter(['Angka', 'Gambar'], [data['peluang_angka'], 1 - data['peluang_angka']], color='blue', zorder=5)
                ax_peluang.axhline(0.5, color='red', linestyle='-', label='Peluang Teoritis')
                ax_peluang.set_ylim(0, 1)
                ax_peluang.set_title("Peluang Empiris vs. Teoritis")
                ax_peluang.set_ylabel("Peluang")
                ax_peluang.legend()
                st.pyplot(fig_peluang)


    # --- Tab 2: Simulasi Dadu ---
    with tab_dadu:
        st.header("🎲 Simulasi Pelemparan Dadu Tunggal")
        st.info("Peluang Teoritis: Setiap sisi ($P(1), P(2), \dots, P(6)$) adalah $1/6 \\approx 0.1667$.")
        
        col_input_dadu, col_visual_dadu = st.columns([1, 1.5])
        
        with col_input_dadu:
            st.subheader("1. Pengaturan Percobaan")
            st.markdown("*Tentukan N dan sisi target untuk dihitung peluangnya.*")
            n_dadu = st.slider("Jumlah Pelemparan (N)", 10, 1000, 200, step=10, key='n_dadu')
            target_sisi = st.selectbox("Pilih Sisi Target (A)", range(1, 7), key='target_sisi')
            st.markdown("---")
            
            if st.button("Lakukan Simulasi Dadu", key='run_dadu'):
                # Simulasi: hasil dari 1 sampai 6
                hasil_dadu = np.random.randint(1, 7, n_dadu)
                
                # Hitung frekuensi setiap sisi
                frekuensi = np.bincount(hasil_dadu)[1:] 
                
                # Total frekuensi untuk sisi target
                jumlah_target = frekuensi[target_sisi - 1]
                
                # Peluang Empiris
                peluang_target_empiris = jumlah_target / n_dadu
                
                st.subheader("2. Hasil Percobaan (Peluang Empiris)")
                st.info(f"Total Pelemparan: **{n_dadu}** kali")
                st.metric(label=f"Jumlah Muncul Sisi {target_sisi}", value=jumlah_target)
                st.metric(label=f"Peluang Empiris $P({target_sisi})$", value=f"{peluang_target_empiris:.4f}", delta=f"Teoritis: 0.1667")
                
                # Simpan hasil untuk visualisasi
                st.session_state['hasil_dadu'] = {
                    'n': n_dadu,
                    'frekuensi': frekuensi,
                    'target':
