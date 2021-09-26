from core import db
from core.entity.banks_entity import BankEntity


def update_bank(post_data, id):
    db.session.query(BankEntity).filter_by(id=id).update(post_data)
    db.session.commit()
    db.session.close()
