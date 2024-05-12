from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies = movies_data[["original_title","poster_link","release_date", "runtime","weighted_rating"]]

# variables to store data
like_movies = []
not_like_movies = []
did_not_watch = []



# method to fetch data from database
def assign_value():
  global all_movies
  m_data = {
    "original_title": all_movies.iloc[0,0],
    "poster_link" : all_movies.iloc[0,1],
    "release_date": all_movies.iloc[0,2] or "n/a",
    "duration" : all_movies.iloc[0,3],
    "rating" : all_movies.iloc[0,4] /2
  }
  return m_data

# /movies api
@app.route("/movies")
def get_movie():
  movies_data = assign_value()
  return jsonify({
    "data":movies_data, 
    "status" : "success"
  })


# /like api
@app.route("/like")
def liked_movie():
  global all_movies
  movies_data = assign_value()
  liked_movie.append (movies_data)
  all_movies.drop([0],inplace=True)
  all_movies = all_movies.reset_index(drop=True)
  return jsonify({
    "status" : "success"
  })
@app.route("/liked")
def liked():
  global like_movies
  return jsonify({
    'data' : like_movies,
    "status" : "success"
  })


# /dislike api
@app.route("/dislike")
def disliked_movie():
  global all_movies
  movies_data = assign_value()
  not_like_movies.append(movies_data)
  all_movies.drop([0], inplace=True)
  all_movies = all_movies.reset_index(drop=True)
  return jsonify({
    "status" : "success"
  })

# /did_not_watch api
@app.route("/did_not_watch")
def did_not_watch():
  global all_movies
  movies_data = assign_value()
  did_not_watch.append(movies_data)
  all_movies.drop([0],inplace=True )
  all_movies = all_movies.reset_index(drop=True)
  return jsonify({
    "status" : "success"
  })

if __name__ == "__main__":
  app.run()