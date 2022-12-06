# Some set up for the application 


from flask import Flask  # noqa
from flaskext.mysql import MySQL  # noqa

# create a MySQL object that we will use in other parts of the API
db = MySQL()


def create_app():
    app = Flask(__name__)

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'Record-Autograph-Unrivaled-Gear-Shifty0'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'admin'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'our_app'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)

    # Import the various routes
    from src.views import views  # noqa
    from src.teams.teams import teams_blueprint  # noqa
    from src.betters.betters import betters_blueprint  # noqa
    from src.betsnodds.bets import bets_blueprint  # noqa
    from src.betsnodds.odds import odds_blueprint # noqa
    from src.schedules.schedules import schedules_blueprint  # noqa
    from src.schedules.games.games import games_blueprint  # noqa
    from src.teams.athletes.athletes import athletes_blueprint  # noqa
    from src.teams.coaches.coaches import coaches_blueprint  # noqa

    # Register the routes that we just imported so they can be properly handled
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(teams_blueprint, url_prefix='/teams')
    app.register_blueprint(betters_blueprint, url_prefix='/betters')
    app.register_blueprint(bets_blueprint, url_prefix='/bets')
    app.register_blueprint(odds_blueprint, url_prefix='/odds')
    app.register_blueprint(schedules_blueprint, url_prefix='/schedules')
    app.register_blueprint(games_blueprint, url_prefix='/games')
    app.register_blueprint(athletes_blueprint, url_prefix='/athletes')
    app.register_blueprint(coaches_blueprint, url_prefix='/coaches')


    return app
