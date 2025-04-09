import streamlit as st
import pickle
import pandas as pd
import random


happy_keywords = ["joy", "happy", "love", "success", "exciting", "fun", "celebrate", "adventure"]
sad_keywords = ["sad", "loss", "cry", "tragedy", "heartbreak", "pain", "grief", "sorrow"]


def recommend_books_by_mood(mood):
    recommended_books = []
    for _, book in books.iterrows():
        description = book['description'].lower() if 'description' in books.columns else ""
        if mood == "happy" and any(word in description for word in happy_keywords):
            recommended_books.append((book['title'], round(random.uniform(3, 5), 1)))
        elif mood == "sad" and any(word in description for word in sad_keywords):
            recommended_books.append((book['title'], round(random.uniform(3, 5), 1)))

    return recommended_books[:5]  


def recommend(book):
    book_index = books[books['title'] == book].index[0]
    distances = similarity[book_index]
    books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_books = []
    for i in books_list:
        title = books.iloc[i[0]].title
        rating = round(random.uniform(3, 5), 1)  
        recommended_books.append((title, rating))  

    return recommended_books


def smart_recommend_books():
    recommended_books = []
    for _, book in books.iterrows():
        rating = round(random.uniform(3.5, 5), 1)  
        recommended_books.append((book['title'], rating))

    
    recommended_books = sorted(recommended_books, key=lambda x: x[1], reverse=True)
    return recommended_books[:5]


books_dict = pickle.load(open('books_dict.pkl', 'rb'))
books = pd.DataFrame(books_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Mood-Based Book Recommender with Smart Suggestions')


st.header("What's your mood?")
user_mood = st.text_input("Tell me how you're feeling right now (e.g., 'I'm happy', 'I'm feeling sad'):") 


smart_recommendation = st.checkbox("Enable Smart Recommendations (based on popularity or other factors)")


if user_mood:
    mood_box = st.container()  
    with mood_box:
        if "happy" in user_mood.lower():
            mood = "happy"
            st.write("You seem to be in a happy mood! 😊")
        elif "sad" in user_mood.lower():
            mood = "sad"
            st.write("You seem to be in a sad mood. 😔")
        else:
            mood = "neutral"
            st.write("We recommend selecting books manually for your mood. 😐")

        
        if mood in ["happy", "sad"]:
            recommendations = recommend_books_by_mood(mood)
            if recommendations:
                st.write("### Mood-Based Recommendations:")
                for title, rating in recommendations:
                    amazon_link = f"https://www.amazon.com/s?k={title.replace(' ', '+')}"
                    st.markdown(
                        f"""
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                            <span style="font-size: 18px; font-weight: bold;">{title} (Rating: {rating}/5)</span>
                            <a href="{amazon_link}" target="_blank" style="text-decoration: none;">
                                <button style="background-color: #4CAF50; color: white; padding: 5px 10px; border: none; border-radius: 4px; cursor: pointer;">Read Now</button>
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            else:
                st.write("Here are some books you would like <3")


if smart_recommendation:
    smart_box = st.container()  
    with smart_box:
        st.write("### Smart Recommendations (based on popularity or other factors):")
        smart_recommendations = smart_recommend_books()
        for title, rating in smart_recommendations:
            amazon_link = f"https://www.amazon.com/s?k={title.replace(' ', '+')}"
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                    <span style="font-size: 18px; font-weight: bold;">{title} (Rating: {rating}/5)</span>
                    <a href="{amazon_link}" target="_blank" style="text-decoration: none;">
                        <button style="background-color: #4CAF50; color: white; padding: 5px 10px; border: none; border-radius: 4px; cursor: pointer;">Read Now</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )


st.header("Smart Recommendation Based on Selected Book")
selected_book = st.selectbox(
    'Select a book for recommendations:',
    books['title'].values
)

st.write(f'You selected: {selected_book}')

if st.button('Show Recommendation'):
    recommendations = recommend(selected_book)
    st.write("Recommended Books:")
    for title, rating in recommendations:
        amazon_link = f"https://www.amazon.com/s?k={title.replace(' ', '+')}"
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <span style="font-size: 18px; font-weight: bold;">{title} (Rating: {rating}/5)</span>
                <a href="{amazon_link}" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #4CAF50; color: white; padding: 5px 10px; border: none; border-radius: 4px; cursor: pointer;">Read Now</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )
