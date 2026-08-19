'''Main app server code'''
from flask import Flask, request, render_template
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
app = Flask("Sentiment Analyzer")
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    '''route sentiment'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    return f"The given text has been identified to produce {label.split('_')[1]} with a score of {score}."
@app.route("/")
def render_index_page():
    '''route index'''
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)