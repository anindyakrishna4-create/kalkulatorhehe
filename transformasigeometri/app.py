import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="🔬 Virtual Lab Peluang Matematika",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNGSI UTAMA ---
def main():
    st.title("🔬 Virtual Lab Peluang Matematika")
    st.markdown("""
    Selamat datang! Lab ini dirancang untuk mengilustrasikan **Hukum Bilangan Besar** (Law of Large Numbers), 
    yaitu bagaimana peluang empiris (hasil percobaan) semakin mendekati peluang teoritis ketika **jumlah percobaan (N) ditingkatkan**.
    """)
    st.markdown("---")

    # === INISIALISASI SESSION STATE UNTUK MENCEGAH KEY ERROR ===
    # Ini memastikan bahwa 'hasil_koin' dan 'hasil_dadu' selalu ada, meskipun nilainya None
    if 'hasil_koin' not in st.session_state:
        st.session_state['hasil_koin'] = None
    if 'hasil_dadu' not in st.session_state:
        st.session_state['hasil_dadu'] = None
    
    # --- Pengaturan Layout dengan Tabs ---
    tab_koin, tab_dadu = st.tabs(["🪙 Pelemparan Koin", "🎲 Pelemparan Dadu"])
    
    # --- Tab 1: Simulasi Koin ---
    with tab_koin:
        st.header("🪙 Simulasi Pelemparan Koin")
        st.info("Peluang Teoritis: Angka ($P(A)$) dan Gambar ($P(G)$) masing-masing adalah $0.5$ (50%).")
        
        col_input_koin, col_visual_koin = st.columns([1, 1.5])

        with col_input_koin:
            st.subheader("1. Pengaturan Percobaan")
            st.markdown("*Gunakan slider untuk menentukan berapa kali koin akan dilempar secara virtual.*")
            n_koin = st.slider("Jumlah Pelemparan (N)", 10, 1000, 100, step=10, key='n_koin_slider')
            st.markdown("---")
            
            # Button untuk menjalankan simulasi
            if st.button("Lakukan Simulasi Koin", key='run_koin'):
                # Simulasi: 0=Angka, 1=Gambar
                hasil_koin = np.random.randint(0, 2, n_koin)
                
                jumlah_angka = np.sum(hasil_koin == 0)
                jumlah_gambar = np.sum(hasil_koin == 1)
                
                # Peluang Empiris
                peluang_angka_empiris = jumlah_angka / n_koin
                
                # Simpan hasil ke session state
                st.session_state['hasil_koin'] = {
                    'n': n_koin,
                    'angka': jumlah_angka,
                    'gambar': jumlah_gambar,
                    'peluang_angka': peluang_angka_empiris
                }
            
            st.subheader("2. Hasil Percobaan (Peluang Empiris)")
            
            # Tampilkan hasil metrik hanya jika simulasi sudah dijalankan
            if st.session_state['hasil_koin']:
                data = st.session_state['hasil_koin']
                
                st.info(f"Total Pelemparan: **{data['n']}** kali")
                
                st.metric(label="Jumlah Angka (A)", value=data['angka'])
                st.metric(label="Peluang Angka Empiris", value=f"{data['peluang_angka']:.4f}", delta=f"Teoritis: 0.5")
                st.metric(label="Jumlah Gambar (G)", value=data['gambar'])
                st.metric(label="Peluang Gambar Empiris", value=f"{1 - data['peluang_angka']:.4f}", delta=f"Teoritis: 0.5")
            else:
                st.warning("Tekan 'Lakukan Simulasi Koin' untuk melihat hasil.")

            # Panduan Tambahan
            st.markdown("---")
            st.subheader("💡 Panduan Penggunaan")
            st.markdown("1. **Mulai dari N kecil** (misalnya 100), lalu jalankan simulasi.")
            st.markdown("2. **Tingkatkan N** (misalnya menjadi 1000) dan ulangi simulasi untuk melihat konvergensi.")


        # Menampilkan visualisasi jika data ada
        if st.session_state['hasil_koin']:
