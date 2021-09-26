from flask_sqlalchemy.model import BindMetaMixin
from sqlalchemy.orm import DeclarativeMeta


class NoNameMeta(BindMetaMixin, DeclarativeMeta):
    pass