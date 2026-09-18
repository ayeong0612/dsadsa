
import pandas as pd
import plotly.express as px
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    page_icon="🎬",
    layout="wide",
)

# 제목
st.title("🎬 영화 데이터 그래프 도감 2 - 분포와 관계")


# 데이터 로드 및 전처리
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"
    df = pd.read_csv(url)

    # 장르 전처리: 세로막대 기호(|)로 여러 개 적힌 경우 첫 번째 장르만 추출
    df["genre"] = df["genre"].astype(str).str.split("|").str[0]

    return df


df = load_data()

# Section 1: 장르별 영화 편수 (도넛 그래프)
st.header("1. 장르별 영화 편수 분포")

# 장르별 편수 집계
genre_counts = df["genre"].value_counts().reset_index()
genre_counts.columns = ["장르", "편수"]

# Plotly 도넛 그래프 생성
fig = px.pie(
    genre_counts,
    values="편수",
    names="장르",
    hole=0.4,
    title="장르별 영화 비율 및 편수",
    hover_data=["편수"],
)

# 마우스 호버 시 편수와 비율이 함께 표시되도록 설정
fig.update_traces(textposition="inside", textinfo="percent+label")

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# 그래프 설명 구역
st.subheader("💡 이 그래프로 알 수 있는 것")
st.write(
    "박스오피스 상위권 영화 중 특정 주요 장르가 차지하는 비중과 장르별 제작 편수 분포를 한눈에 파악할 수 있습니다."
)

st.divider()
