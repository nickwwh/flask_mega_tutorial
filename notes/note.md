# Running flask
* Initialise FLASK_APP to the main .py file
* set FLASK_DEBUG=1 to debug & autoreload scripts

# Structure
* Store services separately in each folder
* Store config.py and set in __init\_\_.py
* routes.py contains all the links handles all the requests (controller?)
* templates folder stores all the templates specific to the app


# Templates
* Uses Jinjja

# Database 
* Use flask-sqlalchemy & flask-migrate
* `flask db init` creates a migration repository
    * Each changes to the database a migration script is added to the repo

* The `flask db migrate` command does not make any changes to the database, it just generates the migration script. To apply the changes to the database, the `flask db upgrade` command must be used.
* With this method, it is easier to make changes to both development and production environment. 
    * Generate & upload the migration scripts via `flask db migrate` then on production, apply the changes using `flask db upgrade`
* undo last migration via `flask db downgrade`
* For a one-to-many relationship, a db.relationship field is normally defined on the "one" side, and is used as a convenient way to get access to the "many"

# Login
* Installl flask-login
* Add login manager to __init__.py `login = LoginManager(app)`
* gives 4 functions
    * `is_authenticated`: if user has valid credentials
    * `is_active`: true if user account is active
    * `is_anonymous`: false for regular users, True for special anonymous user
    * `get_id()`: returns unique identifier for user
* user class must inherit `Usermixin` class 
* Keeps track of logged in users by storing userid in user session.
    * does not interact with db so in models need to add user_loader function


# Password
* Hash yo passwords
* werkzeug.security import generate_password_hash, check_password_hash
*