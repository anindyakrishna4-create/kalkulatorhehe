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

    # === INISIALISASI SESSION STATE UNTUK STABILITAS ===
    if 'hasil_koin' not in st.session_state:
        st.session_state['hasil_koin'] = None
    if 'hasil_dadu' not in st.session_state:
        st.session_state['hasil_dadu'] = None
    
    # --- Pengaturan Layout dengan Tabs ---
    tab_koin, tab_dadu = st.tabs(["🪙 Pelemparan Koin", "🎲 Pelemparan Dadu"])
    
    # --- Tab 1: Simulasi Koin (Sudah Stabil) ---
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
                peluang_gambar_empiris = jumlah_gambar / n_koin 
                
                # Simpan hasil ke session state
                st.session_state['hasil_koin'] = {
                    'n': n_koin,
                    'angka': jumlah_angka,
                    'gambar': jumlah_gambar,
                    'peluang_angka': peluang_angka_empiris,
                    'peluang_gambar': peluang_gambar_empiris 
                }
            
            st.subheader("2. Hasil Percobaan (Peluang Empiris)")
            
            # Tampilkan hasil metrik
            if st.session_state['hasil_koin']:
                data = st.session_state['hasil_koin']
                
                st.info(f"Total Pelemparan: **{data['n']}** kali")
                
                st.metric(label="Jumlah Angka (A)", value=data['angka'])
                st.metric(label="Peluang Angka Empiris", value=f"{data['peluang_angka']:.4f}", delta=f"Teoritis: 0.5")
                st.metric(label="Peluang Gambar Empiris", value=f"{data['peluang_gambar']:.4f}", delta=f"Teoritis: 0.5")
            else:
                st.warning("Tekan 'Lakukan Simulasi Koin' untuk melihat hasil.")

            # Panduan Tambahan
            st.markdown("---")
            st.subheader("💡 Panduan Penggunaan")
            st.markdown("1. **Mulai dari N kecil** (misalnya 100), lalu jalankan simulasi.")
            st.markdown("2. **Tingkatkan N** (misalnya menjadi 1000) dan ulangi simulasi untuk melihat konvergensi.")


        # Menampilkan visualisasi
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


    # --- Tab 2: Simulasi Dadu (Fokus Perbaikan Ada di Sini) ---
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
            
            # --- Perbaikan Logika Simulasi Dadu ---
            # Kami perlu menyimpan target_sisi yang dipilih saat tombol ditekan, karena selectbox bisa berubah setelahnya
            
            if st.button("Lakukan Simulasi Dadu", key='run_dadu'):
                # Simulasi: hasil dari 1 sampai 6
                hasil_dadu = np.random.randint(1, 7, n_dadu)
                
                # Hitung frekuensi setiap sisi
                # np.bincount menghitung frekuensi, [1:] untuk mengabaikan index 0 (karena hasil dadu 1-6)
                frekuensi = np.bincount(hasil_dadu)[1:] 
                
                jumlah_target = frekuensi[target_sisi - 1]
                peluang_target_empiris = jumlah_target / n_dadu
                
                # Simpan hasil ke session state
                st.session_state['hasil_dadu'] = {
                    'n': n_dadu,
                    'frekuensi': frekuensi,
                    'target': target_sisi, # Simpan target yang digunakan saat simulasi
                    'peluang_target': peluang_target_empiris
                }
            
            st.subheader("2. Hasil Percobaan (Peluang Empiris)")

            # Tampilkan hasil metrik
            if st.session_state['hasil_dadu']:
                data = st.session_state['hasil_dadu']
                
                # Jika pengguna mengubah target_sisi setelah simulasi, hitung ulang metrik
                # agar metrik selalu sesuai dengan 'target_sisi' yang sedang dipilih di selectbox, 
                # meskipun grafiknya menampilkan hasil simulasi sebelumnya.
                current_target_freq = data['frekuensi'][target_sisi - 1] 
                current_target_peluang = current_target_freq / data['n']

                st.info(f"Total Pelemparan: **{data['n']}** kali")
                st.metric(label=f"Jumlah Muncul Sisi {target_sisi}", value=current_target_freq)
                st.metric(label=f"Peluang Empiris $P({target_sisi})$", value=f"{current_target_peluang:.4f}", delta=f"Teoritis: 0.1667")
            else:
                st.warning("Tekan 'Lakukan Simulasi Dadu' untuk melihat hasil.")

            # Panduan Tambahan
            st.markdown("---")
            st.subheader("💡 Panduan Penggunaan")
            st.markdown("1. **Pilih Sisi Target** (misalnya 4) di kotak pilihan.")
            st.markdown("2. **Tekan tombol simulasi**.")
            st.markdown("3. **Ubah N** dan ulangi simulasi untuk melihat grafik frekuensi mendekati garis Harapan Teoritis.")

                
        # Menampilkan visualisasi
        if st.session_state['hasil_dadu'] is not None:
            data = st.session_state['hasil_dadu']
            
            with col_visual_dadu:
                st.subheader("3. Visualisasi Hasil Dadu")
                st.caption("Frekuensi kemunculan setiap sisi dadu dibandingkan harapan teoritis.")
                
                fig, ax = plt.subplots(figsize=(7, 5))
                sisi = range(1, 7)
                
                # Highlight sisi target yang digunakan saat simulasi terakhir
                colors = ['salmon'] * 6
                # Cek target yang tersimpan di state untuk highlight
                highlighted_target = data['target']
                colors[highlighted_target - 1] = 'red' 
                
                ax.bar(sisi, data['frekuensi'], color=colors)
                ax.axhline(data['n'] / 6, color='darkgreen', linestyle='--', label='Harapan Teoritis (N/6)')
                
                ax.set_title(f"Distribusi Frekuensi dari {data['n']} Pelemparan Dadu")
                ax.set_xlabel("Sisi Dadu")
                ax.set_ylabel("Frekuensi Muncul")
                ax.set_xticks(sisi)
                ax.legend()
                st.pyplot(fig)


if __name__ == '__main__':
    main()
