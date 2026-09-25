import time
import streamlit as st

st.title("⏱️ เกมจับเวลาทายผลไม้")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""



# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans4.strip().lower()


    # ตรวจข้อ 1
    if u_ans1 == "สัปปะรด":
        st.success("✅ ข้อ 1: ใช่แล้ว คือ สัปปะรด🍍")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกจ่ะ มันคือสัปปะรด🍍 (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "กีวี่":
        st.success("✅ ข้อ 2: คอนเกรตตุเลชั่น คือ กีวี่")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกน้า มันคือกีวี่นะจ๊ะ (คุณตอบ '{u_ans2}')")

   # ตรวจข้อ 3
    if u_ans3 == "ทุเรียน":
        st.success("✅ ข้อ 3: ถุกต้องง มันคือ ทุเรียน")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ไม่ถูก มันคือทุเรียนไงล่ะ (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4
    if u_ans4 == "มะม่วง":
        st.success("✅ ข้อ 4: เยสส มะม่วงไงจ้ะ🥭")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูก คำตอบคือมะม่วงจ้า🥭 (คุณตอบ '{u_ans4}')")

  # ตรวจข้อ 5
    if u_ans5 == "กล้วย":
        st.success("✅ ข้อ 5: เยีย กล้วย🍌")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกจ้า มันคือกล้วยเนาะะ🍌 (คุณตอบ '{u_ans5}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 5:
        st.success("🎉 เฮ้ย! โหดจ้าดดดด")
    if score == 4:
        st.success("🔥 พยามดิว้าา")
    if score == 3:
        st.success("🔥 พยามดิว้าา")
    if score == 2:
        st.success("🔥 พยามดิว้าา")
    if score == 1:
        st.success("🔥 พยามดิว้าา")
    if score == 0:
        st.success("💀 กากว่ะว่ะ")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: มีเปลือกแข็ง มีตาเต็มตัว และมีใบแหลม ๆ อยู่ด้านบน รสชาติหวานอมเปรี้ยว",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: มีเปลือกสีน้ำตาล มีขนอ่อน ๆ ด้านนอก แต่ข้างในเป็นสีเขียว มีเมล็ดเล็ก ๆ สีดำเต็มไปหมด",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: มีหนาม เนื้อข้างในสีเหลือง บางคนชอบ บางคนไม่ชอบ",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: มีรูปร่างรี ๆ เปลือกอาจเป็นสีเขียวหรือสีเหลือง รสชาติเปรี้ยวหรือหวาน และนิยมนำไปกินคู่กับข้าวเหนียว",
    value=st.session_state.ans4_val,

)
ans5 = st.text_input(
    "ข้อ 5: มีเปลือกสีเหลืองเมื่อสุก รูปร่างโค้ง ๆ เนื้อนุ่มและรสหวาน มักออกผลเป็นหวี",
    value=st.session_state.ans5_val,
)
# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5


# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4 ตรงนี้


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)

st.divider()
st.write("นางสาววรัชญ์ชยา หล้าติ๊บ เลขที่ 5 ม.4/4")
st.write("นางสาวอาภาสิริ สิริสกุลทรัพย์ เลขที่ 15 ม.4/4")
st.write("นางสาวกชพร เดชะ เลขที่ 16 ม.4/4")
st.write("นางสาว พลอยปภัส ภูมิคำ เลขที่ 18 ม.4/4")
