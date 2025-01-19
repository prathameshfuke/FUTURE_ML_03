import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class BookRecommender:
    def __init__(self, books_df):
        self.books_df = books_df
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        self.prepare_features()

    def prepare_features(self):
        """Prepare TF-IDF features from book descriptions."""
        self.tfidf_matrix = self.tfidf.fit_transform(
            self.books_df['description'].fillna('')
        )

    def get_recommendations(self, query, n=5):
        """Get book recommendations based on user query."""
        query_vector = self.tfidf.transform([query])
        similarities = cosine_similarity(query_vector, self.tfidf_matrix)
        similar_indices = similarities[0].argsort()[-n:][::-1]
        return self.books_df.iloc[similar_indices]
