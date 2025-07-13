import streamlit as st
from scipy.optimize import linprog
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Konfigurasi halaman
st.set_page_config(page_title="Optimasi Produksi", page_icon="📈", layout="centered")

# ===============================
# Sidebar untuk inputan
st.sidebar.title("🔧 Input Parameter")
num_products = st.sidebar.number_input("Jumlah Produk", min_value=2, max_value=1000, value=2)

st.sidebar.markdown("### 💰 Keuntungan per Unit Produk")
profit = []
for i in range(num_products):
    p = st.sidebar.number_input(f"Produk {i+1}", value=10)
    profit.append(p)

num_constraints = st.sidebar.number_input("Jumlah Kendala (misal bahan baku, waktu, tenaga kerja)", min_value=1, value=2)

st.sidebar.markdown("### ⚙️ Koefisien Kendala dan Batasannya")
A = []
b = []
for j in range(num_constraints):
    st.sidebar.markdown(f"**Kendala {j+1}**")
    row = []
    for i in range(num_products):
        a = st.sidebar.number_input(f"Koefisien Produk {i+1} (Kendala {j+1})", value=1)
        row.append(a)
    A.append(row)
    b_value = st.sidebar.number_input(f"Batas Kendala {j+1}", value=100)
    b.append(b_value)

# ===============================
# Header aplikasi
st.title("📈 Aplikasi Optimasi Produksi")
st.write("Maksimalkan keuntungan produksi dengan beberapa kendala menggunakan Linear Programming.")

# ===============================
# Convert input ke numpy array
A = np.array(A)
b = np.array(b)
c = -np.array(profit)  # dikali -1 karena linprog meminimasi

# ===============================
# Solve linear programming ketika tombol ditekan
if st.button("🚀 Hitung Solusi Optimal"):
    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    if res.success:
        st.success("✅ Solusi Optimal Ditemukan!")
        col1, col2 = st.columns(2)
        produksi = []
        keuntungan_per_produk = []
        with col1:
            total_profit = 0
            for i, x in enumerate(res.x):
                prod_profit = x * profit[i]
                total_profit += prod_profit
                produksi.append(x)
                keuntungan_per_produk.append(prod_profit)
                st.write(f"**Produksi Produk {**
