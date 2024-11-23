from base import db
from base.com.vo.ward_vo import WardVO
from base.com.vo.zone_vo import ZoneVO


class AreaVO(db.Model):
    __tablename__ = 'area_table'
    area_id = db.Column('area_id', db.Integer, primary_key=True,
                        autoincrement=True)
    area_name = db.Column('area_name', db.String(255), nullable=False)
    area_code = db.Column('area_code', db.Integer, nullable=False)
    area_zone_id = db.Column('area_zone_id', db.Integer,
                             db.ForeignKey(ZoneVO.zone_id,
                                           ondelete='CASCADE',
                                           onupdate='CASCADE'),
                             nullable=False)
    area_ward_id = db.Column('area_ward_id', db.Integer,
                             db.ForeignKey(WardVO.ward_id,
                                           ondelete='CASCADE',
                                           onupdate='CASCADE'),
                             nullable=False)

    def as_dict(self):
        return {
            'area_id': self.area_id,
            'area_name': self.area_name,
            'area_code': self.area_code,
            'area_zone_id': self.area_zone_id,
            'area_ward_id': self.area_ward_id
        }


db.create_all()
