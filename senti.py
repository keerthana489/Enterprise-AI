from textblob import TextBlob
Y = input("Type your Sentence:")
edu =TextBlob(Y)
X = edu.sentiment.polarity
#negative = X<o and neutral = 0 and positive X>0 && X<=1
if X<0:
    print("Negative")
elif X == 0:
    print("Neutral")
elif X>0 and X<=1:
    print("Positive")