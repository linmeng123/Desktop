import os

from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

from app.settings import BASE_DIR

db = SQLAlchemy()
migrate = Migrate()
toolbar = DebugToolbarExtension()
# simple
# cache = Cache(config={'CACHE_TYPE': 'simple'})

# redis
cache = Cache(config={
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'Atom-',
})

# filesystem  CACHE_DIR
cache = Cache(config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': os.path.join(BASE_DIR, 'cache'),
})

def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    Bootstrap(app=app)
    # toolbar.init_app(app)
    cache.init_app(app)

