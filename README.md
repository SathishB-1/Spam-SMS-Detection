# Spam-SMS-Detection

## Introduction:
With the massive growth of mobile communication, spam messages have become a persistent problem, often carrying scams, ads, or malicious links. These unwanted messages not only clutter inboxes but also pose potential security threats.

This project aims to automatically classify SMS messages as either spam or ham (non-spam) using a machine learning technique called Support Vector Machine (SVM).

SVM is a powerful and widely used classification algorithm, known for its effectiveness in high-dimensional spaces like text data. By training the model on labeled SMS data, we can create a system that flags spam messages before they reach users.

## How It Works:
The project follows a typical text classification pipeline:

## 1. Dataset
We use a labeled dataset of SMS messages, each tagged as either:

spam – Unwanted promotional or scam messages

ham – Legitimate (non-spam) messages

Example:

mathematica
Copy
Edit
Label: spam | Message: "You won a free ticket to Bahamas! Call now..."
Label: ham  | Message: "Are we still on for dinner tonight?"
## 2. Text Preprocessing
Since machine learning models can't work directly with raw text, we preprocess the messages:

Lowercasing

Removing punctuation and stopwords

Tokenization

Stemming or lemmatization (optional)

## 3. Feature Extraction
We convert text into numerical features using:

Bag of Words (BoW) or

TF-IDF (Term Frequency-Inverse Document Frequency)

This transforms messages into vectors that represent word importance across the dataset.

## 4. Model Training
We use a Support Vector Machine (SVM) classifier:

It finds the optimal hyperplane that separates spam and ham messages.

Works well in high-dimensional text data.

We split the data into training and test sets and fit the SVM model on the training set.

## 5. Model Evaluation
We evaluate the model using metrics such as:

Accuracy

Precision

Recall

F1-score

These help us understand how well the model is detecting spam while minimizing false positives.

## 6. Prediction
Once trained, the model can predict whether a new SMS is spam or not, helping prevent unwanted content from reaching users.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

