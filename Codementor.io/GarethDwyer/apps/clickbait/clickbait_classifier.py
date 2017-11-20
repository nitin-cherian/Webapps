# clickbait_classifier.py


# Import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


# globals
DATA_SET_FILE = "clickbait.txt"


def is_clicbait(text):
    svm, vectorizer = classifier()

    # Vectorize the text. Input needs to be an iterable
    vector = vectorizer.transform([text])

    # Predict using the classifier
    prediction = svm.predict(vector)

    # if prediction is 1, return True else False
    return True if prediction[0] == '1' else False


def load_data(file):
    # Load data from dataset into Python lists
    with open(file) as f:
        lines = [line.strip().split("\t") for line in f]

    headlines, labels = zip(*lines)
    return headlines, labels


def classifier():
    headlines, labels = load_data(DATA_SET_FILE)

    # Break dataset into train and test sets
    train_headlines = headlines[:8000]
    test_headlines = headlines[8000:]
    train_labels = labels[:8000]
    test_labels = labels[8000:]

    # Create a vectorizer and classifier
    vectorizer = TfidfVectorizer()
    svm = LinearSVC()

    # Transform our text data into numerical vectors
    train_vector = vectorizer.fit_transform(train_headlines)

    # Train the classifier
    svm.fit(train_vector, train_labels)

    # Test accuracy of our classifier
    test_vector = vectorizer.transform(test_headlines)
    predictions = svm.predict(test_vector)
    print(accuracy_score(predictions, test_labels))

    return svm, vectorizer


def main():
    classifier()


if __name__ == '__main__':
    main()
