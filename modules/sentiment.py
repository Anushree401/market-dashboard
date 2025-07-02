from textblob import TextBlob

def analyze_sentiment(text):
    # analyze the sentiment of the text, which means it will return a polarity score between -1 and 1, where -1 is negative, 0 is neutral, and 1 is positive
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def summarize_sentiment(texts):
    # summarize the sentiment based on the polarity and subjectivity scores 
    if not texts:
        return {"label":"No Data", "emoji":"❔", "score":0.0}
    
    polarities = []
    for text in texts:
        polarity, subjectivity = analyze_sentiment(text)
        polarities.append(polarity)
    
    avg = sum(polarities) / len(polarities)
    if avg>0.2: # the 0.2 threshold is used to determine if the sentiment is positive, meaning the average polarity score is greater than 0.2, number is chosen based on the distribution of polarity scores in the dataset
        # polarity means the sentiment score, which is a number between -1 and 1, where -1 is negative, 0 is neutral, and 1 is positive 
        label, emoji = "Positive", "🟢"
    elif avg<-0.2: # the -0.2 threshold is used to determine if the sentiment is negative, meaning the average polarity score is less than -0.2, number is chosen based on the distribution of polarity scores in the dataset
        label, emoji = "Negative", "🔴"
    else:
        label, emoji = "Neutral", "🟡"
    
    return {
        "label": label,
        "emoji": emoji,
        "score": round(avg, 3)  # round the score to 3 decimal places
    }