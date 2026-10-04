import streamlit as st
bahasa = st.selectbox("Pilih bahasa / Choose language / 选择语言",
                 ["1: Bahasa Malaysia", "2: English", "3: 中文"])
if bahasa.startswith("1"):
     st.title("Kalkulator Asas")
     num1 = st.number_input("Sila menulis nombor pertama:", value=0)
     num2 = st.number_input("Sila menulis nombor kedua:", value=0)
     operasi = st.selectbox("Sila pilih operasi aritmetik:", 
                        ["1: Tambah (+)", "2: Kurang (-)", "3: Darab (*)", "4: Bahagi (/)"])
     if operasi.startswith("1"):
      hasil = num1 + num2
      st.success(f"Keputusan: {hasil}")
     elif operasi.startswith("2"):
      hasil = num1 - num2
      st.success(f"Keputusan: {hasil}")
     elif operasi.startswith("3"):
      hasil = num1 * num2
      st.success(f"Keputusan: {hasil}")
     elif operasi.startswith("4"):
         if num2 != 0:
          hasil = num1 / num2
          st.success(f"Keputusan: {hasil}")
         else:
          st.error("Ralat matematik! Sila pastikan nombor kedua bukan 0.")
if bahasa.startswith("2"):
     st.title("Simple Calculator")
     num1 = st.number_input("Please enter the first number:", value=0)
     num2 = st.number_input("Please enter the second number:", value=0)
     operasi = st.selectbox("Choose an arithmetic operation:", 
                        ["1: Addition (+)", "2: Subtraction (-)", "3: Multiplication (*)", "4: Division (/)"])
     if operasi.startswith("1"):
      hasil = num1 + num2
      st.success(f"Results: {hasil}")
     elif operasi.startswith("2"):
      hasil = num1 - num2
      st.success(f"Results: {hasil}")
     elif operasi.startswith("3"):
      hasil = num1 * num2
      st.success(f"Results: {hasil}")
     elif operasi.startswith("4"):
         if num2 != 0:
          hasil = num1 / num2
          st.success(f"Results: {hasil}")
         else:
          st.error("Math error! Please ensure the second number is not 0.")

if bahasa.startswith("3"):
     st.title("基础计算器")
     num1 = st.number_input("请输入第一个数字:", value=0)
     num2 = st.number_input("请输入第二个数字:", value=0)
     operasi = st.selectbox("请选择一个算术运算:", 
                        ["1: 加法 (+)", "2: 减法 (-)", "3: 乘法 (*)", "4: 除法 (/)"])
     if operasi.startswith("1"):
      hasil = num1 + num2
      st.success(f"结果: {hasil}")
     elif operasi.startswith("2"):
      hasil = num1 - num2
      st.success(f"结果: {hasil}")
     elif operasi.startswith("3"):
      hasil = num1 * num2
      st.success(f"结果: {hasil}")
     elif operasi.startswith("4"):
         if num2 != 0:
          hasil = num1 / num2
          st.success(f"结果: {hasil}")
         else:
          st.error("检测到错误! 请确保第二个数字不是0。")
 
