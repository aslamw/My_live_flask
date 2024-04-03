from .table import Daily, daily_shema, dailys_shema
from .. import db


class CRUDaily:
    def registe_text(id, text):
        form_daily = Daily(id, text)

        db.session.add_all([form_daily])
        db.session.commit()

        return daily_shema.dump(form_daily)

    def get_all_id(id):
        daily = Daily.query.filter(Daily.id_user == id).all()

        if daily is None:
            return False

        return dailys_shema.dump(daily)

    def get_id(id, id_user):
        daily = Daily.query.filter(
            db.and_(Daily.id == id, Daily.id_user == id_user)
        ).first()

        if daily is None:
            return False

        return daily

    def update(daily, text):
        daily.annotation = text

        db.session.commit()

        return daily_shema.dump(daily)

    def delete(daily):
        db.session.delete(daily)
        db.session.commit()
