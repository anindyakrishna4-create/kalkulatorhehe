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

    # === INISIALISASI SESSION STATE ===
    if 'hasil_koin' not in st.session_state:
        st.session_state['hasil_koin'] = None
    if 'hasil_dadu' not in st.session_state:
        st.session_state['hasil_dadu'] = None
    
    # --- Pengaturan Layout dengan Tabs ---
    tab_koin, tab_dadu = st.tabs(["🪙 Pelemparan Koin", "🎲 Pelemparan Dadu"])
    
    # ----------------------------------------------------------------------
    # --- Tab 1: Simulasi Koin ---
    # ----------------------------------------------------------------------
    with tab_koin:
        st.header("🪙 Simulasi Pelemparan Koin")
        st.info("Peluang Teoritis: Angka ($P(A)$) dan Gambar ($P(G)$) masing-masing adalah $0.5$ (50%).")
        
        col_input_koin, col_visual_koin = st.columns([1, 1.5])

        with col_input_koin:
            st.subheader("1. Pengaturan Percobaan")
            st.markdown("*Gunakan slider untuk menentukan berapa kali koin akan dilempar secara virtual.*")
            n_koin = st.slider("Jumlah Pelemparan (N)", 10, 1000, 100, step=10, key='n_koin_slider')
            st.markdown("---")
            
            if st.button("Lakukan Simulasi Koin", key='run_koin'):
                hasil_koin = np.random.randint(0, 2, n_koin)
                
                jumlah_angka = np.sum(hasil_koin == 0)
                jumlah_gambar = np.sum(hasil_koin == 1)
                
                peluang_angka_empiris = jumlah_angka / n_koin
                peluang_gambar_empiris = jumlah_gambar / n_koin
                
                st.session_state['hasil_koin'] = {
                    'n': n_koin,
                    'angka': jumlah_angka,
                    'gambar': jumlah_gambar,
                    'peluang_angka': peluang_angka_empiris,
                    'peluang_gambar': peluang_gambar_empiris
                }
            
            st.subheader("2. Hasil Percobaan (Peluang Empiris)")
            
            if st.session_state['hasil_koin']:
                data = st.session_state['hasil_koin']
                
                st.info(f"Total Pelemparan: **{data['n']}** kali")
                
                st.metric(label="Jumlah Angka (A)", value=data['angka'])
                st.metric(label="Peluang Angka Empiris", value=f"{data['peluang_angka']:.4f}", delta=f"Teoritis: 0.5")
                st.metric(label="Peluang Gambar Empiris", value=f"{data['peluang_gambar']:.4f}", delta=f"Teoritis: 0.5")
            else:
                st.warning("Tekan 'Lakukan Simulasi Koin' untuk melihat hasil.")

            st.markdown("---")
            st.subheader("💡 Panduan Penggunaan")
            st.markdown("1. **Mulai dari N kecil** (misalnya 100), lalu jalankan simulasi.")
            st.markdown("2. **Tingkatkan N** (misalnya menjadi 1000) dan ulangi simulasi untuk melihat konvergensi.")


        if st.session_state['hasil_koin']:
            data = st.session_state['hasil_koin']
            
            with col_visual_koin:
                st.subheader("3. Visualisasi Hasil Koin")
                
                # 3a. Plot Frekuensi
                st.caption("Frekuensi muncul Angka dan Gambar dibandingkan harapan teoritis.")
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
                st.caption("Peluang Empiris (titik biru) dibandingkan Peluang Teoritis (garis merah).")
                fig_peluang, ax_peluang = plt.subplots(figsize=(7, 4))
                ax_peluang.scatter(['Angka', 'Gambar'], [data['peluang_angka'], data['peluang_gambar']], color='blue', zorder=5) 
                ax_peluang.axhline(0.5, color='red', linestyle='-', label='Peluang Teoritis')
                ax_peluang.set_ylim(0, 1)
                ax_peluang.set_title("Peluang Empiris vs. Teoritis")
                ax_peluang.set_ylabel("Peluang")
                ax_peluang.legend()
                st.pyplot(fig_peluang)


    # ----------------------------------------------------------------------
    # --- Tab 2: Simulasi Dadu ---
    # ----------------------------------------------------------------------
    with tab_dadu:
        st.header("🎲 Simulasi Pelemparan Dadu Tunggal")
        st.info("Peluang Teoritis: Setiap sisi ($P(x)$) adalah $1/6 \\approx 0.1667$.")
        
        col_input_dadu, col_visual_dadu = st.columns([1, 1.5])
        
        with col_input_dadu:
            st.subheader("1. Pengaturan Percobaan")
            st.markdown("*Tentukan N dan sisi target untuk dihitung peluangnya.*")
            n_dadu = st.slider("Jumlah Pelemparan (N)", 10, 1000, 200, step=10, key='n_dadu_slider')
            target_sisi = st.selectbox("Pilih Sisi Target (A)", range(1, 7), key='target_sisi_select')
            st.markdown("---")
            
            if st.button("Lakukan Simulasi Dadu", key='run_dadu'):
                hasil_dadu = np.random.randint(1, 7, n_dadu)
                
                frekuensi = np.bincount(hasil_dadu)[1:] 
                
                jumlah_target =
