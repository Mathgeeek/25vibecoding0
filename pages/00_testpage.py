import streamlit as st

# ------------------ 페이지 설정 ------------------
st.set_page_config(page_title="MBTI 수학 학습 전략", page_icon="📘")

# ------------------ 사이드바 메뉴 ------------------
st.sidebar.title("📚 메뉴")
st.sidebar.markdown("- [메인 화면](https://mathgeek.streamlit.app)")
st.sidebar.markdown("- **MBTI 수학 전략 가이드** ← 현재 페이지")
st.sidebar.markdown("- [MBTI 수학자 매칭](https://mathgeek.streamlit.app/수학자_추천)")

# ------------------ 데이터 정의 ------------------
mbti_info = {
    "INFP": {
        "성향 요약": "이상주의적이고 창의적인 직관형",
        "선호하는 학습 방식": "개념의 의미와 철학적 배경에 관심이 많고, 직관적으로 수학을 이해하려 함.",
        "소홀히 할 수 있는 부분": "반복 연습의 필요성을 간과하고, 계산 실수를 가볍게 여길 수 있음.",
        "극복 전략 및 실천 팁": "개념 학습 후 문제 풀이 계획을 일일 단위로 짜고, '실수노트'를 만들어 반복 실수 유형을 기록하며 점검."
    },
    "INTP": {
        "성향 요약": "논리적이고 분석적인 이론 중심형",
        "선호하는 학습 방식": "공식보다 원리를 이해하는 데 집중하며, 깊이 있는 문제에 도전하는 것을 선호함.",
        "소홀히 할 수 있는 부분": "기초 계산을 소홀히 하거나, '아는 문제'를 반복 학습하지 않음.",
        "극복 전략 및 실천 팁": "매일 기초 연산 타이머 학습을 포함하고, '알지만 틀리는 문제' 목록을 따로 정리하여 주기적으로 복습."
    },
    "ESTJ": {
        "성향 요약": "계획적이고 실천력 강한 현실주의자",
        "선호하는 학습 방식": "교과서 중심, 체계적인 학습 계획 수립 후 차근차근 실행하는 방식 선호.",
        "소홀히 할 수 있는 부분": "공식에 의존해 문제를 풀고, 원리에 대한 질문을 간과할 수 있음.",
        "극복 전략 및 실천 팁": "개념 요약 후 '왜 이 공식이 성립하는가?'를 직접 설명하거나 친구에게 가르치며 원리 이해 강화."
    },
    "ENFP": {
        "성향 요약": "호기심 많고 활기찬 탐험가",
        "선호하는 학습 방식": "다양한 유형의 문제를 경험하고, 재미있는 방식으로 학습하려 함.",
        "소홀히 할 수 있는 부분": "체계적인 복습을 놓치기 쉬우며, 감정 기복에 따라 학습 지속력이 흔들릴 수 있음.",
        "극복 전략 및 실천 팁": "1일 1복습 타임을 정해 루틴화하고, 학습 내용을 '나만의 방식'으로 요약 정리해보며 감정적 만족도 확보."
    },
}

# ------------------ 본문 ------------------
st.title("📘 MBTI 유형별 수학 학습 전략 가이드")
st.markdown("MBTI에 따라 당신에게 잘 맞는 수학 학습 방식과 주의할 점, 보완 전략을 알려드릴게요!\n")

mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_info.keys()))

if mbti:
    info = mbti_info[mbti]

    st.markdown(f"### 🧠 {mbti} | {info['성향 요약']}")

    # 블록 1: 선호하는 학습 방식
    st.markdown("""
    <div style='background-color:#f0f8ff; padding:15px; border-radius:10px; margin-bottom:15px;'>
        <h4 style='color:#007acc;'>✅ 선호하는 학습 방식</h4>
        <p style='font-size:16px;'>{}</p>
    </div>
    """.format(info['선호하는 학습 방식']), unsafe_allow_html=True)

    # 블록 2: 소홀히 할 수 있는 부분
    st.markdown("""
    <div style='background-color:#fff8dc; padding:15px; border-radius:10px; margin-bottom:15px;'>
        <h4 style='color:#e67300;'>🚨 주의할 점</h4>
        <p style='font-size:16px;'>{}</p>
    </div>
    """.format(info['소홀히 할 수 있는 부분']), unsafe_allow_html=True)

    # 블록 3: 극복 전략 및 팁
    st.markdown("""
    <div style='background-color:#e6ffe6; padding:15px; border-radius:10px;'>
        <h4 style='color:#2e8b57;'>💡 추천 학습 전략</h4>
        <p style='font-size:16px;'>{}</p>
    </div>
    """.format(info['극복 전략 및 실천 팁']), unsafe_allow_html=True)
