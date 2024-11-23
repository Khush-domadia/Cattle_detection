from base import db


class ZoneVO(db.Model):
    __tablename__ = 'zone_table'
    zone_id = db.Column('zone_id', db.Integer, primary_key=True,
                        autoincrement=True)
    zone_name = db.Column('zone_name', db.String(255), nullable=False)
    zone_code = db.Column('zone_code', db.Integer, nullable=False)

    def as_dict(self):
        return {
            'zone_id': self.zone_id,
            'zone_name': self.zone_name,
            'zone_code': self.zone_code
        }


db.create_all()
