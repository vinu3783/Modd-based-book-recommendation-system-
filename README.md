# Modd-based-book-recommendation-system-
# 📚 Mood-Based Book Recommendation System

A smart recommendation system that suggests books to users based on their current *mood* using sentiment analysis or mood selection. The system aims to personalize reading experiences by connecting emotions with literature.

---

## 🎯 Features

- 🎭 Detects user mood via:
  - Manual mood selection (Happy, Sad, Excited, etc.)
  - Text-based sentiment analysis (optional)
- 📖 Recommends books aligned with the user's emotional state
- 🔍 Book info includes title, author, genre, and brief summary
- 💾 Dynamic recommendation logic based on genres and user mood
- 🖼 Clean and intuitive UI (optional)
- 🧠 Built using NLP & content-based filtering

---

## 🛠 Tech Stack

> Customize this section as per your version

- *Frontend*: HTML, CSS, JavaScript / Streamlit / Tkinter (GUI)
- *Backend*: Python (Flask / Django)
- *Machine Learning*: NLP (TextBlob / NLTK / Hugging Face Transformers)
- *Recommendation Engine*: Content-based filtering using cosine similarity
- *Data*: Custom CSV / Goodreads / Google Books API
- *Optional*: SQLite / JSON storage

- 
The Mood-Based Recommendation System is a smart application that suggests books based on the user's current mood, previous reads, and personalized preferences. By analyzing user responses to a set of emotion-driven and interest-based questions, the system delivers tailored recommendations that enhance user engagement and satisfaction.



Download Dataset from this link:
https://zenodo.org/records/4265096/files/books_1.Best_Books_Ever.csv?download=1

Run evry Cell of IPYNB file to get:
1)books_dict.pkl
2)similarity.pkl

Then run app.py in terminal : streamlit run app.py

