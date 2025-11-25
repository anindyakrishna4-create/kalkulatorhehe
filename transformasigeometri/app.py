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

**Petunjuk:** Atur panjang dua sisi (*depan* dan *samping*) menggunakan slider di **Sidebar** (bilah samping) untuk melihat perubahan nilai.
""")

st.markdown("---")

# =============================================================
#           BAGIAN 1: INPUT (TETAP DI SIDEBAR)
# =============================================================

st.sidebar.header("🛠️ Atur Segitiga Siku-Siku")
st.sidebar.markdown("Atur panjang dua sisi. Sisi miring dihitung otomatis menggunakan Pythagoras.")

# Input menggunakan slider
sisi_depan = st.sidebar.slider("Sisi Depan (a)", min_value=1.0, max_value=20.0, value=3.0, step=0.1)
sisi_samping = st.sidebar.slider("Sisi Samping (b)", min_value=1.0, max_value=20.0, value=4.0, step=0.1)

# Hitung Sisi Miring (c) dengan Teorema Pythagoras: c² = a² + b²
sisi_miring = math.sqrt(sisi_depan**2 + sisi_samping**2)

st.sidebar.metric(
    label="Sisi Miring (c)", 
    value=f"{sisi_miring:.2f}"
)

# =============================================================
#           BAGIAN 2: OUTPUT (VISUALISASI & HASIL BERSEBELAHAN)
# =============================================================

# Membuat dua kolom: 
# Kolom Kiri (Visualisasi) mengambil 1.5 bagian lebar.
# Kolom Kanan (Hasil Perhitungan) mengambil 1 bagian lebar.
col_vis, col_hasil = st.columns([1.5, 1])

# --- Kolom Kiri: Visualisasi ---
with col_vis:
    st.subheader("🖼️ Visualisasi Segitiga Siku-Siku")
    st.markdown("Visualisasi dan panjang sisi-sisi yang dihitung:")
    
    # Menampilkan Diagram Segitiga
    # Menggunakan representasi visual dalam bentuk diagram
    st.markdown(
        """
        

[Image of a right-angled triangle with sides labeled 'a' (opposite), 'b' (adjacent), and 'c' (hypotenuse) and an angle labeled $\theta$]

        """, 
        unsafe_allow_html=True
    )

    # Label untuk sisi-sisi
    st.info(f"""
    * **Sisi Depan (a):** **{sisi_depan:.2f}**
    * **Sisi Samping (b):** **{sisi_samping:.2f}**
    * **Sisi Miring (c):** **{sisi_miring:.2f}**
    """)


# --- Kolom Kanan: Hasil Perhitungan ---
with col_hasil:
    st.subheader("📊 Perhitungan Trigonometri & Sudut")
    
    # Hitung Nilai Trigonometri (sin, cos, tan)
    sin_theta = sisi_depan / sisi_miring
    cos_theta = sisi_samping / sisi_miring
    tan_theta = sisi_depan / sisi_samping

    # Hitung Sudut (Theta) dalam derajat
    theta_rad = math.atan2(sisi_depan, sisi_samping)
    theta_deg = math.degrees(theta_rad)

    st.markdown(f"**Nilai untuk Sudut $\\theta$:**")
    
    # Tampilkan Rumus dan Hasil dalam Tabel
    st.table({
        "Fungsi": ["Sinus ($\sin \\theta$)", "Kosinus ($\cos \\theta$)", "Tangen ($\tan \\theta$)"],
        "Rumus": ["Depan / Miring", "Samping / Miring", "Depan / Samping"],
        "Nilai": [
            f"$\\frac{{a}}{{c}} = {sin_theta:.4f}$", 
            f"$\\frac{{b}}{{c}} = {cos_theta:.4f}$", 
            f"$\\frac{{a}}{{b}} = {tan_theta:.4f}$"
        ]
    })
    
    # Tampilkan Nilai Sudut
    st.markdown("---")
    st.markdown("**Nilai Sudut (Derajat):**")
    
    # Sudut Theta
    st.metric(
        label="Sudut $\\theta$", 
        value=f"{theta_deg:.2f}°",
        delta="Sudut yang dianalisis"
    )
    
    # Sudut Beta (Sudut lainnya)
    beta_deg = 90.0 - theta_deg
    st.metric(
        label="Sudut $\\beta$ (Sudut lainnya)", 
        value=f"{beta_deg:.2f}°",
        delta="Dihitung dari $90° - \\theta$"
    )
    
    st.metric(label="Sudut Siku-siku", value="90.00°")

# =============================================================
#           BAGIAN 3: KONSEP (DI BAWAH KOLOM)
# =============================================================

st.markdown("---")
st.subheader("💡 Konsep Dasar (SOH CAH TOA)")

st.success("""
* **SOH**: **S**inus = **O**pposite (Depan) / **H**ypotenuse (Miring)
* **CAH**: **C**osinus = **A**djacent (Samping) / **H**ypotenuse (Miring)
* **TOA**: **T**angen = **O**pposite (Depan) / **A**djacent (Samping)
""")
