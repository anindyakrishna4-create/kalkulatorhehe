import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Fungsi untuk menggambar grafik
def plot_transformation(points, transformation_matrix, transformation_name):
    fig, ax = plt.subplots()

    # Plot titik asli
    points_original = np.array(points)
    ax.plot(points_original[:, 0], points_original[:, 1], 'bo-', label="Titik Asli")

    # Terapkan transformasi
    transformed_points = np.dot(transformation_matrix, points_original.T).T

    # Plot titik setelah transformasi
    ax.plot(transformed_points[:, 0], transformed_points[:, 1], 'ro-', label=f"Titik setelah {transformation_name}")

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.axhline(0, color='black',linewidth=1)
    ax.axvline(0, color='black',linewidth=1)
    ax.grid(True)
    ax.set_aspect('equal')
    ax.set_title(f"Transformasi {transformation_name}")
    ax.legend()

    st.pyplot(fig)

# Fungsi untuk refleksi dan translasi
def reflection_matrix(axis='x'):
    if axis == 'x':
        return np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        return np.array([[-1, 0], [0, 1]])

def translation_matrix(dx=0, dy=0):
    return np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

# Fungsi utama untuk aplikasi
def main():
    st.title("Virtual Lab: Refleksi dan Translasi dalam Geometri")

    # Penjelasan singkat
    st.markdown("""
    Di dalam lab ini, kamu dapat melakukan transformasi geometrik pada titik dalam bidang 2D.
    Pilih jenis transformasi yang ingin dilakukan: Refleksi (X atau Y) atau Translasi (Geser Titik).
    """)

    # Input titik
    st.sidebar.header("Masukkan Titik")
    x = st.sidebar.number_input("Titik X", -10, 10, 2)
    y = st.sidebar.number_input("Titik Y", -10, 10, 3)

    points = [(x, y)]
    st.sidebar.write(f"Titik Asli: {points}")

    # Pilihan transformasi
    transform_type = st.selectbox("Pilih Transformasi", ("Refleksi", "Translasi"))

    if transform_type == "Refleksi":
        axis = st.selectbox("Pilih Sumbu Refleksi", ("X", "Y"))
        if axis == 'X':
            transformation_matrix = reflection_matrix('x')
            transformation_name = "Refleksi terhadap sumbu X"
        else:
            transformation_matrix = reflection_matrix('y')
            transformation_name = "Refleksi terhadap sumbu Y"
        plot_transformation(points, transformation_matrix, transformation_name)

    elif transform_type == "Translasi":
        dx = st.slider("Geser sumbu X", -10, 10, 5)
        dy = st.slider("Geser sumbu Y", -10, 10, 5)
        transformation_matrix = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
        transformation_name = f"Translasi (dx={dx}, dy={dy})"
        plot_transformation(points, transformation_matrix, transformation_name)

if __name__ == "__main__":
    main()

