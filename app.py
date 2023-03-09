from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import db, SECRET_KEY
from models.movie import Movie
from models.dialogue import Dialogue
from models.cast import Cast
from os import environ, path, getcwd
from dotenv import load_dotenv
load_dotenv(path.join(getcwd(), '.env'))



def create_app():
    global db
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI') 
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Successfully")
    
    
    with app.app_context():
        
        
        @app.route('/', methods=['GET', 'POST'])
        def home():
            if request.method == 'POST':
                # Extract movie data from request
                movie_name = request.form['movie_name']
                movie_duration = request.form['movie_duration']

                # Create movie record and commit to database
                movie = Movie(movie_name=movie_name, movie_duration=movie_duration)
                db.session.add(movie)
                db.session.commit()

                # Extract cast data from request
                cast_name = request.form['cast_name']
                cast_gender = request.form['cast_gender']
                cast_character = request.form['cast_character']

                # Use newly created movie id to create cast record
                cast = Cast(cast_name=cast_name, cast_gender=cast_gender, cast_character=cast_character, movie_id=movie.id)
                db.session.add(cast)
                db.session.commit()
                
                # Extract dialogue data from request
                dialogue = request.form['dialogue']
                start_time = request.form['start_time']
                end_time = request.form['end_time']
                
                # Use newly created cast id to create dialogue record
                dialogue = Dialogue(dialogue=dialogue, start_time=start_time, end_time=end_time, cast_id=cast.id)
                db.session.add(dialogue)
                db.session.commit()

            all_movies = Movie.query.all()
            all_casts = Cast.query.all()
            all_dialogues = Dialogue.query.all()
            return render_template("home.html", all_movies = all_movies,all_casts = all_casts, all_dialogues = all_dialogues)

                                   
                


        @app.route('/update_movie/<int:movie_id>', methods=['GET', 'POST'])
        def update_movie(movie_id):

            if request.method == 'POST':
                movie_name = request.form['movie_name']
                movie_duration = request.form['movie_duration']
                movie = Movie.query.filter_by(id=movie_id).first()
                movie.movie_name = movie_name
                movie.movie_duration = movie_duration
                db.session.commit()
                return redirect("/")
            movie = Movie.query.filter_by(id=movie_id).first() 
            return render_template('update_movie.html', movie=movie)


        @app.route('/delete_movie/<int:movie_id>')
        def delete_movie(movie_id):
            movies = Movie.query.filter_by(id=movie_id).first()
            db.session.delete(movies)
            db.session.commit()
            return redirect("/")
        
        
        @app.route('/update_cast/<int:cast_id>', methods=['GET', 'POST'])
        def update_cast(cast_id):
            
            if request.method == 'POST':
                cast_name = request.form['cast_name']
                cast_gender = request.form['cast_gender']
                cast_character = request.form['cast_character']
                cast = Cast.query.filter_by(id=cast_id).first()
                cast.cast_name = cast_name
                cast.cast_gender = cast_gender
                cast.cast_character = cast_character
                db.session.commit()
                return redirect("/")
            cast = Cast.query.filter_by(id=cast_id).first() 
            return render_template('update_cast.html', cast=cast)

            
            
        @app.route('/delete_cast/<int:cast_id>')
        def delete_cast(cast_id): 
            
            cast = Cast.query.filter_by(id=cast_id).first()
            db.session.delete(cast)
            db.session.commit()
            return redirect("/")
        
        
        @app.route('/update_dialogue/<int:dialogue_id>', methods=['GET', 'POST'])
        def update_dialogue(dialogue_id):
            
            if request.method == 'POST':
                dialogue = request.form['dialogue']
                start_time = request.form['start_time']
                end_time = request.form['end_time']
                dialogues = Dialogue.query.filter_by(id=dialogue_id).first()
                dialogues.dialogue = dialogue
                dialogues.start_time = start_time
                dialogues.end_time = end_time
                db.session.commit()
                return redirect("/")
            dialogue = Dialogue.query.filter_by(id=dialogue_id).first() 
            return render_template('update_dialogue.html', dialogue=dialogue)
                
            
            
        @app.route('/delete_dialogue/<int:dialogue_id>')
        def delete_dialogue(dialogue_id): 
            dialogue = Dialogue.query.filter_by(id=dialogue_id).first()
            db.session.delete(dialogue)
            db.session.commit()
            return redirect("/")
        
           

        #db.drop_all()
        db.create_all()
        db.session.commit()

        return app
        
        
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)    