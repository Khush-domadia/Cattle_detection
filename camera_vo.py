from sqlalchemy import ForeignKey

from base import db
from base.com.vo.area_vo import AreaVO
from base.com.vo.ward_vo import WardVO
from base.com.vo.zone_vo import ZoneVO


class CameraVO(db.Model):
    __tablename__ = 'camera_table'
    camera_id = db.Column('camera_id', db.Integer, primary_key=True,
                          autoincrement=True)
    camera_name = db.Column('camera_name', db.String(255), nullable=False)
    camera_code = db.Column('camera_code', db.Integer, nullable=False)
    camera_link = db.Column('camera_link', db.String(500), nullable=False)
    camera_zone_id = db.Column('camera_zone_id', db.Integer,
                               ForeignKey(ZoneVO.zone_id,
                                          ondelete='CASCADE',
                                          onupdate='CASCADE'),
                               nullable=False)
    camera_ward_id = db.Column('camera_ward_id', db.Integer,
                               ForeignKey(WardVO.ward_id,
                                          ondelete='CASCADE',
                                          onupdate='CASCADE'),
                               nullable=False)
    camera_area_id = db.Column('camera_area_id', db.Integer,
                               ForeignKey(AreaVO.area_id,
                                          ondelete='CASCADE',
                                          onupdate='CASCADE'),
                               nullable=False)

    def as_dict(self):
        return {
            'camera_id': self.camera_id,
            'camera_name': self.camera_name,
            'camera_code': self.camera_code,
            'camera_link': self.camera_link,
            'camera_zone_id': self.camera_zone_id,
            'camera_ward_id': self.camera_ward_id,
            'camera_area_id': self.camera_area_id
        }


db.create_all()
