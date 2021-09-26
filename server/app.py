from flask_migrate import Migrate
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

from core import app
from core.entity.custom_meta import NoNameMeta

if __name__ == '__main__':
    app.run(host='0.0.0.0')
