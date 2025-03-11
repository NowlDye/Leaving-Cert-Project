import plotly.express as px

def generate_visualisations_plotly(df):
    # Bar Chart: Top Genres
    top_genres = df['genre'].value_counts().head(10)
    fig_bar = px.bar(
        x=top_genres.index,
        y=top_genres.values,
        labels={'x': 'Genre', 'y': 'Number of Movies'},
        title="Top 10 Movie Genres",
        color=top_genres.index,
        color_continuous_scale='Viridis'
    )
    fig_bar.update_layout(
        xaxis_title='Genre',
        yaxis_title='Number of Movies',
        xaxis_tickangle=45
    )
    fig_bar.write_html("static/genre_bar_chart.html")

    # Scatter Plot: Gross Earnings vs IMDb Rating
    fig_scatter = px.scatter(
        df,
        x='rating',
        y='gross(M)',
        color='genre',
        title="Gross Earnings (in Millions) vs IMDb Rating",
        labels={'rating': 'IMDb Rating', 'gross(M)': 'Gross Earnings (in Millions)'},
        color_discrete_sequence=px.colors.qualitative.Set1,
        opacity=0.7
    )
    fig_scatter.update_layout(
        xaxis_title="IMDb Rating",
        yaxis_title="Gross Earnings (in Millions)",
        legend_title="Genre"
    )
    fig_scatter.write_html("static/gross_vs_rating_scatter.html")
