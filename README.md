# MOVIE-RECOMMENDATION-

# Movie Recommendation System (TMDB 5000 Dataset)

This project builds multiple movie recommendation systems using the TMDB 5000 Movies and Credits datasets. It covers popularity-based, weighted-rating-based, hybrid, and content-based recommendation approaches using Python, Pandas, and scikit-learn.

---

## Dataset

The project uses two CSV files:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

Both datasets contain 4,803 movies and are merged using the common `id` column.

---

## Libraries Used

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* pickle

---

## Data Preprocessing

1. Load both datasets using pandas.
2. Rename `movie_id` in credits data to `id`.
3. Merge movies and credits dataframes on `id`.
4. Drop unnecessary columns such as homepage, duplicate title columns, and production countries.
5. Handle missing values where required.

Final merged dataset shape:

* Rows: 4,803
* Columns: 27

---

## Recommendation Systems Implemented

### 1. Weighted Rating Based Recommendation

A weighted average rating is calculated to balance movie ratings with vote counts.

Formula used:

Weighted Score = ((R × v) + (C × m)) / (v + m)

Where:

* R = average rating of the movie
* v = number of votes
* C = mean rating across all movies
* m = vote count threshold (90th percentile)

Movies are ranked based on this weighted score.

---

### 2. Popularity Based Recommendation

Movies are ranked purely based on their popularity score provided in the dataset. This method favors trending or widely viewed movies.

---

### 3. Hybrid Recommendation System

Since popularity and weighted ratings have different scales, MinMax normalization is applied.

Steps:

1. Normalize popularity and weighted average scores.
2. Combine both scores using equal weights.

Final hybrid score:

score_mix = 0.5 × popularity_scaled + 0.5 × weighted_average_scaled

Movies are ranked using this combined score.

---

### 4. Content-Based Recommendation System

This system recommends movies based on textual similarity of movie overviews.

Steps:

1. Remove rows with missing overview values.
2. Convert movie overviews into TF-IDF vectors.
3. Compute similarity matrix using sigmoid kernel.
4. Recommend movies based on highest similarity scores.

Example:

* If a user watches **John Carter**, the system recommends movies with similar plot descriptions.

---

## Recommendation Function

A helper function `give_recommendation(movie_title, model)` is implemented to return the top similar movies for a given title using the similarity matrix.

---

## Visualization

* Boxplot for vote count distribution
* Bar plots for:

  * Top movies by weighted rating
  * Top movies by popularity
  * Top movies by hybrid score

---

## Model Persistence

To reuse the trained models:

* Movie metadata is saved as `movies_dict.pkl`
* Similarity matrix is saved as `similarity.pkl`

These files can be loaded later for deployment (e.g., Streamlit app).

---

## Future Work

* Build a full content-based recommender UI
* Deploy the recommendation system using Streamlit
* Add user-based collaborative filtering

---

## How to Run

1. Place both CSV files in the project directory.
2. Run the notebook or Python script sequentially.
3. Use `give_recommendation()` to get movie suggestions.

---

## Output

* Ranked movie recommendations
* Visual insights into popularity and ratings
* Saved model files for deployment

---

This project demonstrates end-to-end development of multiple recommendation systems using real-world movie data.
