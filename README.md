
# Book Recommendation Chatbot

This project is a conversational AI chatbot that recommends books based on user preferences. It uses Natural Language Processing (NLP) techniques and a book dataset to suggest books based on the user's query. 

## Features:
- **NLP Techniques:** Uses NLTK for tokenization, stop word removal, and lemmatization.
- **Book Recommendations:** The chatbot suggests books based on the user's query using a TF-IDF based recommendation system.
- **Dataset:** The project uses a book dataset containing book titles, authors, and other metadata.

## Tools & Libraries:
- Python
- NLTK
- Pandas
- Scikit-learn
- Kaggle API
- Matplotlib (for data visualization)
- Seaborn (for data visualization)

## Dataset:
This project uses a dataset available from Kaggle. It includes information about books such as:
- Book-Title
- Book-Author
- Year of Publication
- Publisher
- Image URLs

### Dataset Download:
- The dataset can be downloaded via Kaggle API or manually from [Kaggle Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset).

## Setup & Installation:

### Prerequisites:
- Python 3.x
- Install the required Python packages:
  ```bash
  pip install nltk pandas scikit-learn matplotlib seaborn kaggle
  ```

### Running the Chatbot:
1. Download the dataset and place it in the project directory.
2. Run the script:
   ```bash
   python book_recommendation_chatbot.py
   ```

### Sample Interaction:
```
You: Recommend me some books on data science
Bot: Based on your interests, here are some books you might enjoy:
- "Data Science for Business" by Foster Provost (2013)
- "Python for Data Analysis" by Wes McKinney (2018)
...
```

## Visualizations:
The project includes visualizations of:
- Publications over the years.
- Top publishers.
- Top authors.

## License:
This project is licensed under the MIT License.

## Acknowledgements:
- **Dataset:** Kaggle Books Dataset by Saurabh Bagchi
- **Libraries:** NLTK, Scikit-learn, Pandas, Matplotlib, Seaborn
