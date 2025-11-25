import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Virtual Lab Transformasi Geometri (Bangun Datar)",
    layout="wide", 
    initial_sidebar_state="collapsed" 
)

def create_plot(original_points, transformed_points, title):
    """Fungsi untuk membuat plot Matplotlib untuk Poligon"""
    fig, ax = plt.subplots(figsize=(8, 8)) 

    # Batas plot dan Grid
    limit = 10
    # Mengatur batas plot secara dinamis
    all_points = np.vstack([original_points, transformed_points])
    max_coord = int(np.ceil(np.max(np.abs(all_points)))) + 2
    limit = max(10, max_coord) 
    
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_xticks(np.arange(-limit, limit + 1, 1))
    ax.set_yticks(np.arange(-limit, limit + 1, 1))
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_aspect('equal', adjustable='box')
    
    # Sumbu X dan Y
    ax.axhline(0, color='gray', linewidth=1)
    ax.axvline(0, color='gray', linewidth=1)

    # --- Plotting Poligon ---
    original_closed = np.vstack([original_points, original_points[0]])
    transformed_closed = np.vstack([transformed_points, transformed_points[0]])

    # 1. Plot dan Isi (Fill) Bentuk Asli (Biru)
    ax.fill(original_points[:, 0], original_points[:, 1], 'blue', alpha=0.2, label='Bentuk Asli')
    ax.plot(original_closed[:, 0], original_closed[:, 1], 'b-', linewidth=1.5)

    # 2. Plot dan Isi (Fill) Bentuk Hasil Transformasi (Merah)
    ax.fill(transformed_points[:, 0], transformed_points[:, 1], 'red', alpha=0.4, label='Bentuk Transformasi')
    ax.plot(transformed_closed[:, 0], transformed_closed[:, 1], 'r--', linewidth=2)
    
    # Menambahkan label untuk setiap titik asli
    labels = ['P', 'Q', 'R']
    for i, (x, y) in enumerate(original_points):
        ax.text(x + 0.1, y + 0.1, f'{labels[i]}({x}, {y})', color='blue', fontsize=10)
    
    # Menambahkan label untuk setiap titik transformasi
    labels_prime = ['P\'', 'Q\'', 'R\'']
    for i, (x, y) in enumerate(transformed_points):
        ax.text(x + 0.1, y + 0.1, f"{labels_prime[i]}", color='red', fontsize=10, weight='bold')


    ax.set_title(title, fontsize=14)
    ax.legend(loc='lower right')
    st.pyplot(fig)

# --- Callback untuk menyimpan pilihan tab ---
def set_transform_type(t_type):
    st.session_state.transform_type = t_type

def main():
    """Fungsi utama aplikasi Streamlit"""
    st.title("🔬 Virtual Lab Transformasi Geometri: Bangun Datar")
    st.markdown("Eksperimen bagaimana Rotasi, Dilatasi, Refleksi, dan Translasi mengubah posisi dan bentuk suatu **Segitiga (PQR)**.")
    st.markdown("---")

    # Inisialisasi state awal
    if 'transform_type' not in st.session_state:
        st.session_state.transform_type = 'Translasi'

    # --- Pilihan Transformasi menggunakan Tabs ---
    # Menggunakan on_click pada container tab untuk mengatur state
    tab_trans, tab_rot, tab_dil, tab_ref = st.tabs(["➡️ Translasi", "🔄 Rotasi", "拡大 Dilatasi", "↔️ Refleksi"])
    
    # Mengatur state saat tab dibuka (Ini menggantikan tombol "Pilih X")
    with tab_trans:
        st.write("---")
        set_transform_type('Translasi')
        st.write("Translasi memindahkan bangun sejauh jarak dan arah yang sama.")
    with tab_rot:
        st.write("---")
        set_transform_type('Rotasi')
        st.write("Rotasi memutar bangun mengelilingi pusat O(0,0) sejauh sudut $\\alpha$.")
    with tab_dil:
        st.write("---")
        set_transform_type('Dilatasi')
        st.write("Dilatasi mengubah ukuran bangun berdasarkan faktor skala (k) dari pusat O(0,0).")
    with tab_ref:
        st.write("---")
        set_transform_type('Refleksi')
        st.write("Refleksi membalik objek melintasi suatu garis cermin.")

    # Tipe transformasi yang sedang aktif
    transform_type = st.session_state.transform_type
    
    # --- Main Layout: Two Columns (Input vs. Output) ---
    # Tampilan akan diperbarui saat widget input di kolom kiri berubah
    col_input, col_plot = st.columns([1, 1.5]) 
    
    # --- Kolom Kiri: Input & Kontrol ---
    with col_input:
        st.header("1. Input Koordinat Awal Segitiga")
        
        # Input Titik PQR
        col_p, col_q, col_r = st.columns(3)
        
        with col_p:
            st.subheader("Titik P")
            # Gunakan key unik agar Streamlit melacak perubahannya
            P_x = st.number_input("P - Koordinat X", value=1, step=1, key='Px_in')
            P_y = st.number_input("P - Koordinat Y", value=1, step=1, key='Py_in')

        with col_q:
            st.subheader("Titik Q")
            Q_x = st.number_input("Q - Koordinat X", value=3, step=1, key='Qx_in')
            Q_y = st.number_input("Q - Koordinat Y", value=4, step=1, key='Qy_in')

        with col_r:
            st.subheader("Titik R")
            R_x = st.number_input("R - Koordinat X", value=5, step=1, key='Rx_in')
            R_y = st.number_input("R - Koordinat Y", value=2, step=1, key='Ry_in')
        
        # Membuat array NumPy dari titik-titik (vertices)
        original_points = np.array([
            [P_x, P_y], [Q_x, Q_y], [R_x, R_y]
        ], dtype=float)

        transformed_points = original_points.copy()

        st.markdown("---")
        st.header(f"2. Pengaturan Parameter Transformasi: {transform_type}")
        
        # --- Logika Perhitungan Transformasi (Disinkronkan) ---
        
        if transform_type == 'Translasi':
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                tx = st.slider("Pergeseran X (a)", -5, 5, 2)
            with col_t2:
                ty = st.slider("Pergeseran Y (b)", -5, 5, 1)
            T = np.array([tx, ty])
            transformed_points = original_points + T
            st.success(f"Vektor Translasi T = ({tx}, {ty})")

        elif transform_type == 'Rotasi':
            angle_deg = st.slider("Sudut Rotasi (Derajat)", -180, 180, 90, 15)
            angle_rad = np.radians(angle_deg)
            R = np.array([
                [np.cos(angle_rad), -np.sin(angle_rad)],
                [np.sin(angle_rad), np.cos(angle_rad)]
            ])
            transformed_points = np.dot(original_points, R.T)
            st.success(f"Sudut Rotasi = {angle_deg}° (Pusat Rotasi O(0,0))")
            
        elif transform_type == 'Dilatasi':
            k = st.slider("Faktor Skala (k)", -3.0, 3.0, 2.0, 0.1)
            transformed_points = original_points * k
            st.success(f"Faktor Skala k = {k} (Pusat Dilatasi O(0,0))")
        
        elif transform_type == 'Refleksi':
            reflection_axis = st.selectbox(
                "Pilih Garis Cermin:",
                ('Sumbu X (y=0)', 'Sumbu Y (x=0)', 'Garis y=x', 'Garis y=-x')
            )
            
            M = np.array([[1, 0], [0, -1]]) # Default: Sumbu X
            result_notation = "P'($x$, -$y$)"
            
            if reflection_axis == 'Sumbu Y (x=0)':
                M = np.array([[-1, 0], [0, 1]])
                result_notation = "P'(-$x$, $y$)"
            elif reflection_axis == 'Garis y=x':
                M = np.array([[0, 1], [1, 0]])
                result_notation = "P'($y$, $x$)"
            elif reflection_axis == 'Garis y=-x':
                M = np.array([[0, -1], [-1, 0]])
                result_notation = "P'(-$y$, -$x$)"
            
            transformed_points = np.dot(original_points, M.T)
            st.success(f"Refleksi: {result_notation}")
        
        
        st.markdown("---")
        st.header("3. Hasil Koordinat P'Q'R'")
        
        # Menampilkan koordinat hasil transformasi
        labels = ['P\'', 'Q\'', 'R\'']
        for i, (x, y) in enumerate(transformed_points):
            st.write(f"**{labels[i]}** = ({round(x, 2)}, {round(y, 2)})")

    # --- Kolom Kanan: Plot Output ---
    with col_plot:
        # Grafik akan otomatis diperbarui karena transformed_points sudah terhitung di kolom kiri
        st.header(f"Visualisasi Transformasi: **{transform_type}**")
        create_plot(original_points, transformed_points, f"Visualisasi {transform_type} pada Segitiga PQR")


if __name__ == '__main__':
    main()
