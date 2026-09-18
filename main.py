import pandas as pd
import plotly.express as px
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    page_icon="🎬",
    layout="wide",
)

# 앱 제목
st.title("🎬 영화 데이터 그래프 도감 2 - 분포와 관계")


# 데이터 불러오기 및 전처리
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"
    df = pd.read_csv(url)

    # 장르 전처리: 세로막대 기호(|)로 여러 개 적힌 영화는 첫 번째 장르만 사용
    df["genre"] = df["genre"].astype(str).str.split("|").str[0]

    return df


df = load_data()

# -------------------------------------------------------------------
# 첫 번째 그래프: 장르별 영화 편수 (도넛 그래프)
# -------------------------------------------------------------------
st.header("1. 장르별 영화 편수")

# 장르별 편수 집계
genre_counts = df["genre"].value_counts().reset_index()
genre_counts.columns = ["genre", "count"]

# 도넛 그래프 생성 (hole 파라미터로 중앙을 비움)
fig = px.pie(
    genre_counts,
    names="genre",
    values="count",
    hole=0.4,
    title="장르별 영화 편수 및 비율",
    labels={"genre": "장르", "count": "편수"},
)

# 마우스 호버 시 편수(value)와 비율(percent)이 표시되도록 설정
fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    hovertemplate="<b>장르</b>: %{label}<br><b>편수</b>: %{value}편<br><b>비율</b>: %{percent}<extra></extra>",
)

# 그래프 화면 출력
st.plotly_chart(fig, use_container_width=True)

# '이 그래프로 알 수 있는 것' 영역
st.container()
st.subheader("💡 이 그래프로 알 수 있는 것")
st.info(
    "박스오피스 상위권 영화 중 가장 비중이 높은 주요 장르와 각 장르별 편수 분포 비율을 파악할 수 있습니다."
)

st.divider()
