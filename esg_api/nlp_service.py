import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class NLPService:
    def __init__(self):
        # Ensure required NLTK resources are downloaded
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        
        self.stop_words = set(stopwords.words('english'))

    def process_query(self, query):
        # Tokenize the query using word_tokenize
        words = word_tokenize(query.lower())
        # Remove stop words and keep alphanumeric words
        filtered_words = [word for word in words if word.isalnum() and word not in self.stop_words]
        return filtered_words
