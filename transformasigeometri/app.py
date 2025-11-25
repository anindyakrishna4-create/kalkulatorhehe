import streamlit as st
import numpy as np
import math

# --- Konfigurasi Halaman ---
# Layout 'wide' tetap digunakan untuk memaksimalkan ruang di dalam tab
st.set_page_config(
    page_title="Virtual Lab Trigonometri Dasar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Judul dan Deskripsi ---
st.title("🔬 Virtual Lab: Trigonometri Dasar")
st.markdown("""
Aplikasi interaktif ini membantu Anda memahami konsep dasar **Sinus (sin)**, **Kosinus (cos)**, dan **Tangen (tan)** pada **segitiga siku-siku**.

**Petunjuk:** Atur panjang dua sisi di **Sidebar** (bilah samping) dan gunakan tab di bawah ini untuk melihat **Visualisasi** dan **Hasil Perhitungan**.
""")

st.markdown("---")

# =============================================================
#           BAGIAN 1: INPUT (TETAP DI SIDEBAR)
# =============================================================

st.sidebar.header("🛠️ Atur Segitiga Siku-Siku")
st.sidebar.markdown("Atur panjang dua sisi. Sisi miring dihitung otomatis menggunakan Teorema Pythagoras.")

# Input menggunakan slider
sisi_depan = st.sidebar.slider("Sisi Depan (a)", min_value=1.0, max_value=20.0, value=5.3, step=0.1)
sisi_samping = st.sidebar.slider("Sisi Samping (b)", min_value=1.0, max_value=20.0, value=4.0, step=0.1)

# Hitung Sisi Miring (c)
sisi_miring = math.sqrt(sisi_depan**2 + sisi_samping**2)

st.sidebar.metric(
    label="Sisi Miring (c)", 
    value=f"{sisi_miring:.2f}"
)

# =============================================================
#           BAGIAN 2: KONTEN UTAMA DALAM TAB
# =============================================================

tab_vis, tab_hasil = st.tabs(["🖼️ Visualisasi Segitiga", "📊 Hasil & Konsep"])

# --- Tab Kiri: Visualisasi Segitiga ---
with tab_vis:
    st.header("Visualisasi Segitiga Siku-Siku")
    st.markdown("Perhatikan posisi sisi **Depan (a)**, **Samping (b)**, dan **Miring (c)** relatif terhadap Sudut $\\theta$.")
    
    # Menampilkan Diagram Segitiga
    

[Image of a right-angled triangle with sides labeled 'a' (opposite), 'b' (adjacent), and 'c' (hypotenuse) and an angle labeled $\theta$]

    
    # Tampilkan panjang sisi-sisi
    st.info(f"""
    * **Sisi Depan (a):** **{sisi_depan:.2f}**
    * **Sisi Samping (b):** **{sisi_samping:.2f}**
    * **Sisi Miring (c):** **{sisi_miring:.2f}** (Dihitung dari $a^2 + b^2 = c^2$)
    """)

# --- Tab Kanan: Hasil & Konsep ---
with tab_hasil:
    st.header("Perhitungan Trigonometri")
    
    # Hitung Nilai Trigonometri (sin, cos, tan)
    sin_theta = sisi_depan / sisi_miring
    cos_theta = sisi_samping / sisi_miring
    tan_theta = sisi_depan / sisi_samping

    # Hitung Sudut (Theta) dalam derajat
    theta_rad = math.atan2(sisi_depan, sisi_samping)
    theta_deg = math.degrees(theta_rad)

    # Membagi konten hasil menjadi dua kolom kecil di dalam Tab
    col_rasio, col_sudut = st.columns([2, 1])

    with col_rasio:
        st.subheader("1. Rasio Trigonometri (SOH CAH TOA)")
        
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
        
        st.markdown("---")
        st.subheader("💡 Konsep Dasar")
        st.success("""
        * **SOH**: **S**inus = **O**pposite (Depan) / **H**ypotenuse (Miring)
        * **CAH**: **C**osinus = **A**djacent (Samping) / **H**ypotenuse (Miring)
        * **TOA**: **T**angen = **O**pposite (Depan) / **A**djacent (Samping)
        """)

    with col_sudut:
        st.subheader("2. Nilai Sudut")
        
        # Sudut Theta
        st.metric(
            label="Sudut $\\theta$", 
            value=f"{theta_deg:.2f}°",
            delta="Sudut yang dianalisis"
        )
        
        # Sudut Beta (Sudut lainnya)
        beta_deg = 90.0 - theta_deg
        st.metric(
            label="Sudut $\\beta$", 
            value=f"{beta_deg:.2f}°",
            delta="Sudut $90° - \\theta$"
        )
        
        # Sudut Siku-siku
        st.metric(label="Sudut Siku-siku", value="90.00°")
