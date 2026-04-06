import streamlit as st

st.set_page_config(page_title="Tool Tài Xỉu 2026", layout="centered")
st.title("🤖 TOOL SOI CẦU TÀI XỈU")

if 'lich_su' not in st.session_state:
    st.session_state.lich_su = ""

# Giao diện nút bấm to cho iPhone 11
c1, c2 = st.columns(2)
with c1:
    if st.button("🔴 TÀI", use_container_width=True):
        st.session_state.lich_su += "T"
with c2:
    if st.button("🔵 XỈU", use_container_width=True):
        st.session_state.lich_su += "X"

if st.button("🔄 XÓA LÀM LẠI"):
    st.session_state.lich_su = ""

st.info(f"Cầu hiện tại: {st.session_state.lich_su}")

def phan_tich(s):
    if len(s) < 3: return "Đang chờ nhập đủ 3 ván..."
    # Logic cầu 1-1
    if s[-3:] == "TXT": return "Dự đoán: XỈU (Cầu 1-1)"
    if s[-3:] == "XTX": return "Dự đoán: TÀI (Cầu 1-1)"
    # Logic cầu bệt
    if s[-3:] == "TTT": return "Dự đoán: XỈU (Bẻ bệt)"
    if s[-3:] == "XXX": return "Dự đoán: TÀI (Bẻ bệt)"
    # Logic nghiêng
    if s.count("T") > s.count("X"): return "Dự đoán: XỈU (Nghiêng Tài)"
    return "Dự đoán: TÀI (Nghiêng Xỉu)"

if st.session_state.lich_su:
    st.success(phan_tich(st.session_state.lich_su))
