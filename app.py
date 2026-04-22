import streamlit as st
from src.pipeline.recommender_pipeline import RecommendationPipeline

st.set_page_config(page_title="Anime Recommnder", layout="wide")


@st.cache_resource
def get_recommendation_pipeline():
    return RecommendationPipeline()


pipeline = get_recommendation_pipeline()

st.title("Anime Recommender System")
query = st.text_input(
    "Enter your anime preferences (e.g., light-hearted anime with school settings): "
)
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)
