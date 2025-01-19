# src/chatbot/chat_handler.py
from ..recommender.book_recommender import BookRecommender
from ..data_preprocessing.preprocessor import TextPreprocessor

class ChatHandler:
    def __init__(self, recommender):
        self.recommender = recommender
        self.preprocessor = TextPreprocessor()
        self.conversation_history = []

    def handle_message(self, user_message):
        """Process user message and return appropriate response."""
        processed_message = self.preprocessor.preprocess(user_message)
        self.conversation_history.append(("user", user_message))

        # Add basic intent recognition
        if "recommend" in processed_message or "suggest" in processed_message:
            recommendations = self.recommender.get_recommendations(processed_message)
            response = self.format_recommendations(recommendations)
        else:
            response = "How can I help you find your next favorite book?"

        self.conversation_history.append(("bot", response))
        return response

    def format_recommendations(self, recommendations):
        """Format book recommendations into a readable response."""
        response = "Based on your interests, here are some books you might enjoy:\n\n"
        for _, book in recommendations.iterrows():
            response += f"- {book['title']} by {book['author']}\n"
        return response
