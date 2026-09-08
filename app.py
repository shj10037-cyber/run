import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="행운의 포춘쿠키 🥠", page_icon="🥠", layout="centered")

# 포춘쿠키 운세 메시지 리스트
FORTUNES = [
    "오늘 당신에게 뜻밖의 좋은 기회가 찾아옵니다!",
    "소소한 행동이 큰 행복으로 돌아오는 하루입니다.",
    "걱정하던 일이 의외로 쉽게 풀릴 것입니다.",
    "좋은 인연을 만나 새로운 자극을 받게 됩니다.",
    "차분한 마음을 유지하면 원하는 결과를 얻을 수 있습니다.",
    "오늘의 선택이 머지않아 큰 성공으로 연결됩니다.",
    "주변 사람에게 먼저 미소를 건네보세요. 운이 따라옵니다.",
    "잠시 쉬어가도 괜찮습니다. 더 멀리 가기 위한 준비 단계입니다.",
]

# 행운의 아이템/숫자/색상 리스트
LUCKY_ITEMS = ["선글라스", "텀블러", "파란색 펜", "노트", "초콜릿"]
LUCKY_COLORS = ["파스텔 블루", "레몬 옐로우", "에메랄드 그린", "체리 레드", "라벤더"]

# 상태 초기화
if "fortune" not in st.session_state:
    st.session_state.fortune = None
if "lucky_number" not in st.session_state:
    st.session_state.lucky_number = None
if "lucky_item" not in st.session_state:
    st.session_state.lucky_item = None
if "lucky_color" not in st.session_state:
    st.session_state.lucky_color = None

st.title("🥠 오늘 나의 행운의 포춘쿠키")
st.write("버튼을 눌러 포춘쿠키를 깨뜨리고 오늘의 운세를 확인하세요!")

st.divider()

# 운세 뽑기 버튼
if st.button("🥠 포춘쿠키 열어보기", use_container_width=True):
    st.session_state.fortune = random.choice(FORTUNES)
    st.session_state.lucky_number = random.randint(1, 45)
    st.session_state.lucky_item = random.choice(LUCKY_ITEMS)
    st.session_state.lucky_color = random.choice(LUCKY_COLORS)

# 결과 출력
if st.session_state.fortune:
    st.balloon()  # 축하 효과 Animation
    st.success("✨ **오늘의 메시지**")
    st.subheader(f'"{st.session_state.fortune}"')

    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="🍀 행운의 숫자", value=st.session_state.lucky_number)
    with col2:
        st.metric(label="🎁 행운의 아이템", value=st.session_state.lucky_item)
    with col3:
        st.metric(label="🎨 행운의 컬러", value=st.session_state.lucky_color)

    if st.button("🔄 다시 뽑기"):
        st.session_state.fortune = None
        st.rerun()
