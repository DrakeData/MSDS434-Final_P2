from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# ---- MAIN TAB SECTION ----
# emoji cheatsheet: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="MSDS 434: Final Project", 
    page_icon=":musical_note:", 
    layout="wide"
    )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_music = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_euaveaxu.json')

img_heatmap = Image.open("images/heatmap1.png")
img_scatter1 = Image.open("images/energy_vs_loud.png")
img_scatter2 = Image.open("images/acouts_vs_pop.png")
img_automl1 = Image.open("images/automl_performance.png").resize((800, 300))
img_automl2 = Image.open("images/automl_confidence.png").resize((800, 300))
img_automl3 = Image.open("images/automl_accracy.png")


# ---- HEADER SECTION ----
with st.container():
    st.title("Spotify Tracks - Bop or Flop?")
    st.markdown('''Spotify, the popular music streaming platform, not only provides access to a vast library of songs but also offers valuable track data that includes information on attributes 
    such as popularity, tempo, duration, and key. One of the most intriguing uses of Spotify's track data is in the field of machine learning, where it can be used to train models to predict 
    the success of a song. For this project, I analyzed  Spotify's track attributes [from Kaggle](https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets?select=tracks.csv) to develop an
    algorithm that can classify songs as either "bops" or "flops" based on their characteristics. 
    ''')

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("About the Data")
        st.markdown('''The Spotify track data set for this project was pulled [from Kaggle](https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets?select=tracks.csv) and it had 
        over 580,000 unique tracks and their audio features. Some of the features include popularity, duration, tempo, key, and many others. This data is valuable for music enthusiasts, researchers, 
        and businesses who can use it to gain insights into consumer behavior, music trends, and preferences. The Spotify data set is an excellent resource for anyone interested in exploring 
        the intersection of music and data.
        ''')
        st.markdown("For the complete data dictonary of the data set, please [see my README](https://github.com/DrakeData/MSDS434-Final_P2#audio-features) for this project.")
    with right_column:
        st_lottie(lottie_music, height=500, key="music")

with st.container():

    st.write("---")
    st.header("EDA")

    st.markdown('''Exploratory Data Analysis (EDA) was performed on the Spotify data set to gain insights into the relationships between various attributes such as energy, 
    volume, and popularity. The analysis involved the use of visualizations to identify patterns and trends in the data, and to gain a better understanding of the underlying factors that 
    contribute to the success of a song on the Spotify platform.''')

    tab1, tab2, tab3 = st.tabs(["Correlations", "Energy Vs. Loudness", "Popularity Vs. Acousticness"])
    with tab1:
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Correlations")
            st.markdown('''To investigate correlations between different attributes of the Spotify data set, a correlation matrix was computed and visualized using heatmaps. 
            This allowed for the identification of strong positive or negative relationships between different attributes, which provided insights into how certain characteristics may 
            impact the popularity of a song.
            ''')
            st.markdown('''**Observatioins:**''')
            st.markdown('''- Strong possitive correlation with energy and volume''')
            st.markdown('''- Negative correlation with popularity and acousticness''')
        with right_column:
             st.image(img_heatmap)
    
    with tab2:
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Energy Vs. Loudness")
            st.markdown('''In the Spotify data set, there is a strong positive correlation between Energy and Loudness, indicating that songs with higher energy tend to also be louder. 
            This correlation suggests that these two attributes are closely related and may play an important role in the success of a song on the Spotify platform.''')

            st.markdown('''**Note:** To better visualize the correlation between two variables in the Spotify data set, the data set was reduced to 2346 samples by randomly selecting 
            data points from the original data set. This was done to make the scatter plot less cluttered and to help highlight any trends or patterns that may 
            exist between the two variables being analyzed.
            ''')
        with right_column:
            st.image(img_scatter1)

    with tab3:
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Popularity Vs. Acousticness")
            st.markdown('''There is a negative correlation between popularity and acousticness, which suggests that songs with high levels of acousticness are less likely to be 
            popular on the platform. This relationship may be due to the fact that highly acoustic songs may not be as appealing to the general public, who may prefer more upbeat 
            and energetic tracks.''')

            st.markdown('''**Note:** To better visualize the correlation between two variables in the Spotify data set, the data set was reduced to 2346 samples by randomly selecting 
            data points from the original data set. This was done to make the scatter plot less cluttered and to help highlight any trends or patterns that may 
            exist between the two variables being analyzed.
            ''')
        with right_column:
            st.image(img_scatter2)

with st.container():
    st.write("---")
    st.header("Machine Learning - Logistic Regression Model")
    st.markdown('''Using Google Cloud Platform's (GCP) AutoML, I was able to build a logistic regression model to predict whether a song is a "bop" or a "flop" based on its 
    Spotify track attributes with 87.3% accuracy score, 57.6% precision score and 8.5% recall score.
    ''')
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Model's Performance Metrics:")
        st.image(img_automl1)
    with right_column:
        st.subheader("Model's Confidence:")
        st.image(img_automl2)

with st.container():
    st.write("---")
    st.header("Machine Learning - Make Prediction")

    col1, col2, col3 = st.columns([3,6,3])
    with col1:
        st.write("")
    with col2:
        st.image(img_automl3)
    with col3:
        st.write("")
    st.markdown('''The above bar graph is a visual representation of the accuracy of a machine learning model in predicting whether a song is a "bop" or a "flop" 
    based on its attributes. The graph shows the number of correct and incorrect predictions made by the model with a random sample size of 22,625 tracks.
    ''')