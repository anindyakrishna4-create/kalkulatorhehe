# ... (Baris di sekitar tombol 'Lakukan Simulasi Koin')

            if st.button("Lakukan Simulasi Koin", key='run_koin'):
                # Simulasi: 0=Angka, 1=Gambar
                hasil_koin = np.random.randint(0, 2, n_koin)
                
                jumlah_angka = np.sum(hasil_koin == 0)
                jumlah_gambar = np.sum(hasil_koin == 1)
                
                # Peluang Empiris
                peluang_angka_empiris = jumlah_angka / n_koin
                peluang_gambar_empiris = jumlah_gambar / n_koin # <--- BARU: Hitung secara eksplisit
                
                # Simpan hasil ke session state
                st.session_state['hasil_koin'] = {
                    'n': n_koin,
                    'angka': jumlah_angka,
                    'gambar': jumlah_gambar,
                    'peluang_angka': peluang_angka_empiris,
                    'peluang_gambar': peluang_gambar_empiris # <--- BARU: Simpan nilai gambar
                }
            
            st.subheader("2. Hasil Percobaan (Peluang Empiris)")
            
            # Tampilkan hasil metrik hanya jika simulasi sudah dijalankan
            if st.session_state['hasil_koin']:
                data = st.session_state['hasil_koin']
                
                st.info(f"Total Pelemparan: **{data['n']}** kali")
                
                st.metric(label="Jumlah Angka (A)", value=data['angka'])
                st.metric(label="Peluang Angka Empiris", value=f"{data['peluang_angka']:.4f}", delta=f"Teoritis: 0.5")
                # BARIS PERBAIKAN: Menggunakan data['peluang_gambar'] yang sudah disimpan
                st.metric(label="Peluang Gambar Empiris", value=f"{data['peluang_gambar']:.4f}", delta=f"Teoritis: 0.5")
            # ...
