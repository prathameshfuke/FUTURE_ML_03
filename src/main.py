import pandas as pd
from chatbot.chat_handler import ChatHandler
from recommender.book_recommender import BookRecommender

def load_data():
    """Load and prepare books dataset."""
    # You'll need to replace this with your actual data loading logic
    books_df = pd.read_csv('data/books.csv')
    return books_df

def main():
    # Initialize components
    books_df = load_data()
    recommender = BookRecommender(books_df)
    chat_handler = ChatHandler(recommender)

    print("Book Recommendation Chatbot")
    print("Type 'quit' to exit")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        response = chat_handler.handle_message(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
