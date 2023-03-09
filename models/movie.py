from config import db


class Movie(db.Model):
    
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(100), nullable=False)
    movie_duration = db.Column(db.String(20), nullable=False)
    casts = db.relationship('Cast', backref='movie', lazy=True)
    
    

# # Create a dictionary to store all the data
# data = {
#     'movies': [],
#     'casts': [],
#     'dialogues': []
# }


# # Endpoint to add a new movie
# @app.route('/movies', methods=['POST'])
# def add_movie():
#     movie = request.json
#     data['movies'].append(movie)
#     return jsonify({'message': 'Movie added successfully'})

# # Endpoint to update an existing movie
# @app.route('/movies/<int:movie_id>', methods=['PUT'])
# def update_movie(movie_id):
#     movie = request.json
#     data['movies'][movie_id] = movie
#     return jsonify({'message': 'Movie updated successfully'})


# # Endpoint to delete a movie
# @app.route('/movies/<int:movie_id>', methods=['DELETE'])
# def delete_movie(movie_id):
#     del data['movies'][movie_id]
#     return jsonify({'message': 'Movie deleted successfully'})

# # Endpoint to add a new cast
# @app.route('/casts', methods=['POST'])
# def add_cast():
#     cast = request.json
#     data['casts'].append(cast)
#     return jsonify({'message': 'Cast added successfully'})


# # Endpoint to update an existing cast
# @app.route('/casts/<int:cast_id>', methods=['PUT'])
# def update_cast(cast_id):
#     cast = request.json
#     data['casts'][cast_id] = cast
#     return jsonify({'message': 'Cast updated successfully'})


# # Endpoint to delete a cast
# @app.route('/casts/<int:cast_id>', methods=['DELETE'])
# def delete_cast(cast_id):





