from base import db
from base.com.vo.zone_vo import ZoneVO


class WardVO(db.Model):
    __tablename__ = 'ward_table'
    ward_id = db.Column('ward_id', db.Integer, primary_key=True,
                        autoincrement=True)
    ward_name = db.Column('ward_name', db.String(255), nullable=False)
    ward_code = db.Column('ward_code', db.Integer, nullable=False)
    ward_zone_id = db.Column('ward_zone_id', db.Integer,
                             db.ForeignKey(ZoneVO.zone_id,
                                           ondelete='CASCADE',
                                           onupdate='CASCADE'),
                             nullable=False)

    def as_dict(self):
        return {
            'ward_id': self.ward_id,
            'ward_name': self.ward_name,
            'ward_code': self.ward_code,
            'ward_zone_id': self.ward_zone_id
        }


db.create_all()
