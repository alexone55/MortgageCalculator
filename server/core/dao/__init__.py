from core import db


def save_model(model):
    db.session.add(model)
    db.session.commit()
    db.session.close()


def find_by_id(clazz, id):
    model = db.session.query(clazz).filter_by(id=id)
    db.session.commit()
    db.session.close()
    return model


def delete_by_id(clazz, id):
    db.session.query(clazz).filter_by(id=id).delete()
    db.session.commit()
    db.session.close()
