import streamlit as st
import numpy as np
import math

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Virtual Lab Trigonometri Dasar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Judul dan Deskripsi ---
st.title("🔬 Virtual Lab: Trigonometri Dasar")
st.markdown("""
Aplikasi interaktif ini membantu Anda memahami konsep dasar **Sinus (sin)**, **Kosinus (cos)**, dan **Tangen (tan)** pada **segitiga siku-siku**.

**Petunjuk:** Ubah panjang sisi-sisi *depan*, *samping*, atau *miring* menggunakan *slider* di *sidebar* (bilah samping).
""")

st.markdown("---")

# --- Bagian Input Sisi Segitiga (Sidebar) ---
st.sidebar.header("🛠️ Atur Segitiga Siku-Siku")
st.sidebar.markdown("Atur panjang dua sisi, sisi ketiga akan dihitung menggunakan Teorema Pythagoras.")

# Input menggunakan slider, memastikan nilai minimal > 0
sisi_depan = st.sidebar.slider("Sisi Depan (a)", min_value=1.0, max_value=20.0, value=3.0, step=0.1)
sisi_samping = st.sidebar.slider("Sisi Samping (b)", min_value=1.0, max_value=20.0, value=4.0, step=0.1)

# Hitung Sisi Miring (c) dengan Teorema Pythagoras: c² = a² + b²
sisi_miring = math.sqrt(sisi_depan**2 + sisi_samping**2)

st.sidebar.metric(
    label="Sisi Miring (c)", 
    value=f"{sisi_miring:.2f}"
)

# --- Bagian Utama (Visualisasi & Hasil) ---

col_vis, col_hasil = st.columns([1.5, 1])

with col_vis:
    st.subheader("🖼️ Visualisasi Segitiga Siku-Siku")
    st.markdown("Berikut adalah representasi visual dari segitiga Anda:")
    
    # Menampilkan Diagram Segitiga
    # Menggunakan representasi visual dalam bentuk diagram dengan label a, b, c dan sudut teta
    st.markdown(
        """
        

[Image of a right-angled triangle with sides labeled 'a' (opposite), 'b' (adjacent), and 'c' (hypotenuse) and an angle labeled $\theta$]

        """, 
        unsafe_allow_html=True
    )

    # Label untuk sisi-sisi
    st.markdown(f"""
    * **Sisi Depan (a):** **{sisi_depan:.2f}**
    * **Sisi Samping (b):** **{sisi_samping:.2f}**
    * **Sisi Miring (c):** **{sisi_miring:.2f}**
    """)


with col_hasil:
    st.subheader("📊 Perhitungan Trigonometri")
    
    # Hitung Nilai Trigonometri (sin, cos, tan)
    sin_theta = sisi_depan / sisi_miring
    cos_theta = sisi_samping / sisi_miring
    tan_theta = sisi_depan / sisi_samping

    # Hitung Sudut (Theta) dalam radian, lalu konversi ke derajat
    theta_rad = math.atan2(sisi_depan, sisi_samping)
    theta_deg = math.degrees(theta_rad)

    st.markdown(f"Untuk **Sudut $\\theta$**:")
    
    # Tampilkan Rumus dan Hasil
    st.markdown("""
    | Fungsi | Rumus | Nilai |
    | :--- | :--- | :--- |
    | **Sinus ($\sin \\theta$)** | Depan / Miring | $\\frac{{a}}{{c}} = \\frac{{{sisi_depan:.2f}}}{{{sisi_miring:.2f}}} = **{sin_theta:.4f}**$ |
    | **Kosinus ($\cos \\theta$)** | Samping / Miring | $\\frac{{b}}{{c}} = \\frac{{{sisi_samping:.2f}}}{{{sisi_miring:.2f}}} = **{cos_theta:.4f}**$ |
    | **Tangen ($\tan \\theta$)** | Depan / Samping | $\\frac{{a}}{{b}} = \\frac{{{sisi_depan:.2f}}}{{{sisi_samping:.2f}}} = **{tan_theta:.4f}**$ |
    """)

    st.markdown("---")
    
    # Tampilkan Nilai Sudut
    st.subheader("Nilai Sudut")
    
    # Sudut siku-siku (90 derajat)
    st.metric(label="Sudut Siku-siku", value="90.00°")
    
    # Sudut Theta
    st.metric(
        label="Sudut $\\theta$ (Derajat)", 
        value=f"{theta_deg:.2f}°",
        help="Dihitung dari $\\arctan(\\frac{{a}}{{b}})$"
    )
    
    # Sudut Beta (Sudut lainnya)
    beta_deg = 90.0 - theta_deg
    st.metric(
        label="Sudut $\\beta$ (Derajat)", 
        value=f"{beta_deg:.2f}°",
        help="Dihitung dari $90° - \\theta$"
    )

# --- Bagian Penjelasan Konsep ---
st.markdown("---")
st.subheader("💡 Konsep Dasar (SOH CAH TOA)")

st.info("""
* **SOH** $\rightarrow$ **S**inus = **O**pposite (Depan) / **H**ypotenuse (Miring)
* **CAH** $\rightarrow$ **C**osinus = **A**djacent (Samping) / **H**ypotenuse (Miring)
* **TOA** $\rightarrow$ **T**angen = **O**pposite (Depan) / **A**djacent (Samping)
""")
