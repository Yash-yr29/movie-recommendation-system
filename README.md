# 1. PROJECT OVERVIEW

This project is a Content-Based Movie Recommendation System built using Machine Learning.

The system recommends movies based on their similarity to a selected movie using metadata such as genres, keywords, cast, crew, overview, and language.

The project was developed in multiple versions to improve recommendation quality and demonstrate model experimentation.

---

# 2. DATASET

**Source:** The data is taken from Kaggle.

**Rows:** The dataset contains three different files: **[movies, credits, keywords]**, having around **45k observations**.

### 1. Movies

* adult
* belongs_to_collection
* budget
* genres
* homepage
* id
* imdb_id
* original_language
* original_title
* overview

### 2. Credits

* cast
* crew
* id

### 3. Keywords

* Contains a dictionary based on movie content

---

# 3. PROJECT TYPE

**Recommendation System**

This project belongs to one of the major Machine Learning project categories, Recommendation Systems.

The system was developed using:

* Natural Language Processing (NLP)
* Feature Engineering
* Vectorization
* Similarity Search

To improve recommendation quality, three different versions of the system were developed and compared.

## VERSION 1

Built a basic Content-Based Recommendation System using the following features:

* Overview
* Genres
* Keywords
* Cast
* Crew

Recommendations were generated using CountVectorizer and Cosine Similarity.

## VERSION 2

Enhanced the recommendation system by introducing:

* Original Language

This enabled the model to consider language preferences while generating recommendations, improving the relevance of movie suggestions.

## VERSION 3 (FINAL MODEL)

Developed a weighted recommendation system where different features were assigned different importance levels:

* Overview = 1x
* Genres = 5x
* Keywords = 5x
* Cast = 3x
* Crew = 2x
* Original Language = 5x

This version produced more accurate and meaningful recommendations by emphasizing important movie characteristics such as genres, keywords, and language.

---

# 4. WORKFLOW

* Data Load
* Data Preprocessing

  * Raw Dataset
  * Merge Data
  * Select Columns
  * Extract Genres
  * Extract Keywords
  * Extract Cast
  * Extract Crew
  * Add Title
  * Create Tags
  * Join Text
  * Lowercase
* Stemming
* CountVectorizer
* Cosine Similarity
* Recommend()
* Saving Model
* Deploy

---

# 5. TECHNOLOGY USED

* Python
* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Streamlit
* Joblib

---

# 6. Challenges Faced

* Handling nested dictionary columns
* Extracting cast and crew information
* Managing large similarity matrices
* Optimizing recommendation quality
* GitHub file size limitations

---

# 7 . URl

* https://movie-recommendation-system-29.streamlit.app

---

# 8. Future Improvements

* TF-IDF Vectorization
* Hybrid Recommendation System
* Deep Learning-Based Recommendations
* User Preference-Based Recommendations
* LLM-Powered Movie Assistant
