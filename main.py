import streamlit as st
import pandas as pd
import plotly.express as px


DATA_URL = (
    "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"
)


st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    page_icon="🎬",
    layout="wide",
)


st.title("🎬 영화 데이터 그래프 도감 2 - 분포와 관계")
st.markdown(
    "1년간 박스오피스 10위권에 든 영화 가운데 해당 기간에 개봉한 "
    "216편의 데이터를 살펴봅니다."
)


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 여러 장르가 세로막대(|)로 구분된 경우 첫 번째 장르만 사용
    df["genre"] = (
        df["genre"]
        .fillna("미상")
        .astype(str)
        .str.split("|")
        .str[0]
        .str.strip()
    )

    return df


try:
    df = load_data()
except Exception as e:
    st.error("데이터를 불러오는 중 오류가 발생했습니다.")
    st.exception(e)
    st.stop()


# ---------------------------------------------------------
# 그래프 1. 장르별 영화 편수
# ---------------------------------------------------------
st.divider()
st.header("1. 장르별 영화 편수")

genre_counts = (
    df["genre"]
    .value_counts()
    .rename_axis("장르")
    .reset_index(name="영화 편수")
)

fig_genre = px.pie(
    genre_counts,
    names="장르",
    values="영화 편수",
    hole=0.48,
    title="장르별 영화 편수",
)

fig_genre.update_traces(
    textinfo="percent",
    hovertemplate=(
        "<b>%{label}</b><br>"
        "영화 편수: %{value}편<br>"
        "비율: %{percent}<extra></extra>"
    ),
)

fig_genre.update_layout(
    legend_title_text="장르",
    margin=dict(t=60, b=20, l=20, r=20),
)

st.plotly_chart(fig_genre, use_container_width=True)

st.markdown("#### 💡 이 그래프로 알 수 있는 것")
st.info("장르별로 영화가 몇 편씩 분포하는지 한눈에 비교할 수 있습니다.")


# ---------------------------------------------------------
# 데이터 미리보기
# ---------------------------------------------------------
st.divider()
st.header("데이터 미리보기")

display_columns = [
    "movieCd",
    "movieNm",
    "openDt",
    "genre",
    "nation",
    "first_scrn",
    "first_show",
    "first_week_audi",
    "total_audi",
    "days_in_top10",
]

st.dataframe(
    df[display_columns],
    use_container_width=True,
    hide_index=True,
)
