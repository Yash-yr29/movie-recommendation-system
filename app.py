import streamlit as st

from helper import movies
from helper import recommend

st.set_page_config(
    page_title="AI Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# Sidebar
with st.sidebar:

    st.header("🎬 About")

    st.write("""
    AI Movie Recommendation System

    Algorithm:
    Content-Based Filtering

    Similarity:
    Cosine Similarity

    Dataset:
    TMDB 5000 Movies
    """)

    st.divider()

    st.write("Model Version: 3")

# Main Title
st.title("🎬 AI Movie Recommendation System")

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Movies", "5000")

with col2:
    st.metric("Model", "Version 3")

with col3:
    st.metric("Similarity", "Cosine")

st.divider()

# Movie Selection
selected_movie = st.selectbox(
    "Search Movie",
    movies['title'].values
)

if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.subheader("🎯 Recommended Movies")

    for i in range(0, len(recommendations), 3):

        cols = st.columns(3)

        for j, col in enumerate(cols):

            if i + j < len(recommendations):

                with col:

                    st.markdown(
                        f"""
                        <div style="
                            background-color:#0f5132;
                            padding:20px;
                            border-radius:15px;
                            text-align:center;
                            min-height:120px;
                            margin-bottom:20px;
                        ">
                            <h4>{recommendations[i+j]}</h4>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )