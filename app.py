import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Veri Yükleme (Cache ile hızlandırma)
@st.cache_data
def load_data():
    df = pd.read_csv('tmdb_5000_movies.csv')
    df.dropna(inplace=True)
    df['tags'] = df['genres'] + " " + df['overview']
    return df

movies = load_data()

# 2. Algoritma (Cache ile tekrar çalışmasını önle)
@st.cache_resource
def get_similarity():
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    return cosine_similarity(vectors)

similarity = get_similarity()

# 3. Streamlit Arayüzü
st.title("🎬 Film Öneri Sistemi")
selected_movie = st.selectbox("Lütfen bir film seçin:", movies['title'].values)

if st.button("Önerileri Getir"):
    idx = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    st.write(f"**{selected_movie}** filmini izleyenler şunları da beğendi:")
    for i in movies_list:
        st.success(movies.iloc[i[0]].title)