from flask import Flask, render_template
import pandas as pd
import os
from utils.data_prep import prepare_data
from utils.visualisations import generate_visualisations_plotly

app = Flask(__name__)

# Ensure necessary folders exist
os.makedirs("static", exist_ok=True)

# Prepare data and generate visualisations
df = prepare_data("imdb_top_1000_movies.csv")
generate_visualisations_plotly(df)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analytics')
def analytics():
    return render_template("analytics.html")

@app.route('/recommendations')
def recommendations():
    top_movies = df[df['rating'] > 8.5].head(10).to_dict(orient="records")
    return render_template("recommendations.html", recommendations=top_movies)

@app.route('/survey')
def survey():
    # Convert the DataFrame to a list of dictionaries for easier use in JavaScript
    movies_data = df[['title', 'release_year', 'rating', 'genre', 'gross(M)']].to_dict(orient='records')
    return render_template("survey.html", movies=movies_data)

if __name__ == '__main__':
    app.run(debug=True)
