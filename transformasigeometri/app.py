import streamlit as st
import numpy as np
import math

# --- Konfigurasi Halaman ---
# Layout 'wide' sangat penting agar konten bisa mengisi lebar layar
st.set_page_config(
    page_title="Virtual Lab Trigonometri Dasar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Judul dan Deskripsi ---
st.title("🔬 Virtual Lab: Trigonometri Dasar")
st.markdown("""
Aplikasi interaktif ini membantu Anda memahami konsep dasar **Sinus (sin)**, **Kosinus (cos)**, dan **Tangen (tan)** pada **segitiga siku-siku**.

**Petunjuk:** Atur panjang dua sisi (*depan* dan *samping*) menggunakan slider di **Sidebar** (bilah samping) untuk melihat perubahan nilai secara real-time.
""")

st.markdown("---")

# =============================================================
#           BAGIAN 1: INPUT (TETAP DI SIDEBAR)
# =============================================================

st.sidebar.header("🛠️ Atur Segitiga Siku-Siku")
st.sidebar.markdown("Atur panjang dua sisi. Sisi miring dihitung otomatis menggunakan Teorema Pythagoras.")

# Input menggunakan slider
sisi_depan = st.sidebar.slider("Sisi Depan (a)", min_value=1.0, max_value=20.0, value=3.0, step=0.1)
sisi_samping = st.sidebar.slider("Sisi Samping (b)", min_value=1.0, max_value=20.0, value=4.0, step=0.1)

# Hitung Sisi Miring (c)
sisi_miring = math.sqrt(sisi_depan**2 + sisi_samping**2)

st.sidebar.metric(
    label="Sisi Miring (c)", 
    value=f"{sisi_miring:.2f}"
)

# =============================================================
#           BAGIAN 2: VISUALISASI (Lebar Penuh)
# =============================================================

st.header("🖼️ Visualisasi Segitiga Siku-Siku")

# Menampilkan Diagram Segitiga
# Menggunakan visualisasi untuk menjelaskan Sisi Depan, Samping, dan Miring relatif terhadap sudut theta
st.markdown(
    """
    

[Image of a right-angled triangle with sides labeled 'a' (opposite), 'b' (adjacent), and 'c' (hypotenuse) and an angle labeled $\theta$]

    """, 
    unsafe_allow_html=True
)

# Tampilkan panjang sisi-sisi hasil input dan perhitungan
st.info(f"""
* **Sisi Depan (a):** **{sisi_depan:.2f}**
* **Sisi Samping (b):** **{sisi_samping:.2f}**
* **Sisi Miring (c):** **{sisi_miring:.2f}** (Dihitung dari $a^2 + b^2 = c^2$)
""")

st.markdown("---")

# =============================================================
#           BAGIAN 3: HASIL PERHITUNGAN (Lebar Penuh)
# =============================================================

st.header("📊 Hasil Perhitungan Trigonometri & Sudut")

# Hitung Nilai Trigonometri (sin, cos, tan)
sin_theta = sisi_depan / sisi_miring
cos_theta = sisi_samping / sisi_miring
tan_theta = sisi_depan / sisi_samping

# Hitung Sudut (Theta) dalam derajat
theta_rad = math.atan2(sisi_depan, sisi_samping)
theta_deg = math.degrees(theta_rad)

# --- Tabulasi Hasil Utama ---
# Menggunakan tabs untuk memisahkan hasil trigonometri dan nilai sudut agar lebih terorganisir
tab_rasio, tab_sudut, tab_konsep = st.tabs(["Rasio Trigonometri", "Nilai Sudut", "Konsep SOH CAH TOA"])

with tab_rasio:
    st.subheader("Rasio $\sin, \cos, \tan$ untuk Sudut $\\theta$")
    
    # Tampilkan Rumus dan Hasil dalam Tabel
    st.table({
        "Fungsi": ["Sinus ($\sin \\theta$)", "Kosinus ($\cos \\theta$)", "Tangen ($\tan \\theta$)"],
        "Rumus": ["Depan / Miring", "Samping / Miring", "Depan / Samping"],
        "Nilai Hitungan": [
            f"$\\frac{{a}}{{c}} = {sin_theta:.4f}$", 
            f"$\\frac{{b}}{{c}} = {cos_theta:.4f}$", 
            f"$\\frac{{a}}{{b}} = {tan_theta:.4f}$"
        ]
    })

with tab_sudut:
    st.subheader("Nilai Sudut-Sudut Segitiga")
    
    col_teta, col_beta, col_siku = st.columns(3)
    
    # Sudut Theta
    col_teta.metric(
        label="Sudut $\\theta$", 
        value=f"{theta_deg:.2f}°",
        delta="Sudut yang dianalisis"
    )
    
    # Sudut Beta (Sudut lainnya)
    beta_deg = 90.0 - theta_deg
    col_beta.metric(
        label="Sudut $\\beta$ (Sudut lainnya)", 
        value=f"{beta_deg:.2f}°",
        delta="Dihitung dari $90° - \\theta$"
    )
    
    # Sudut Siku-siku
    col_siku.metric(label="Sudut Siku-siku", value="90.00°")

with tab_konsep:
    st.subheader("Mengingat Konsep Dasar")
    st.success("""
    * **SOH**: **S**inus = **O**pposite (Depan) / **H**ypotenuse (Miring)
    * **CAH**: **C**osinus = **A**djacent (Samping) / **H**ypotenuse (Miring)
    * **TOA**: **T**angen = **O**pposite (Depan) / **A**djacent (Samping)
    """)
