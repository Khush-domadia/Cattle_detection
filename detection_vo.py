from base import db
from base.com.vo.zone_vo import ZoneVO
from base.com.vo.ward_vo import WardVO
from base.com.vo.area_vo import AreaVO
from base.com.vo.camera_vo import CameraVO


class DetectionVO(db.Model):
    __tablename__ = 'detection_table'
    detection_id = db.Column('detection_id', db.Integer, primary_key=True,
                        autoincrement=True)
    input_image_name = db.Column('input_image_name', db.String(255),
                                 nullable=False)
    input_image_path = db.Column('input_image_path', db.String(255),
                                 nullable=False)
    output_image_name = db.Column('output_image_name', db.String(255),
                                 nullable=False)
    output_image_path = db.Column('output_image_path', db.String(255),
                                 nullable=False)
    avi_image_name = db.Column('avi_image_name', db.String(255),
                                  nullable=False)
    avi_image_path = db.Column('avi_image_path', db.String(255),
                                  nullable=False)
    detection_zone_id = db.Column('detection_zone_id', db.Integer,
                               db.ForeignKey(ZoneVO.zone_id,
                                          ondelete='CASCADE',
                                          onupdate='CASCADE'),
                               nullable=False)
    detection_ward_id = db.Column('detection_ward_id', db.Integer,
                               db.ForeignKey(WardVO.ward_id,
                                          ondelete='CASCADE',
                                          onupdate='CASCADE'),
                               nullable=False)
    detection_area_id = db.Column('detection_area_id', db.Integer,
                               db.ForeignKey(AreaVO.area_id,
                                          ondelete='CASCADE',
                                          onupdate='CASCADE'),
                               nullable=False)
    detection_camera_id = db.Column('detection_camera_id', db.Integer,
                             db.ForeignKey(CameraVO.camera_id,
                                           ondelete='CASCADE',
                                           onupdate='CASCADE'),
                             nullable=False)
    def as_dict(self):
        return {
            'detection_id': self.detection_id,
            'input_image_name': self.input_image_name,
            'input_image_path': self.input_image_path,
            'output_image_name': self.output_image_name,
            'output_image_path': self.output_image_path,
            'avi_image_name': self.avi_image_name,
            'avi_image_path': self.avi_image_path,
            'detection_zone_id': self.detection_zone_id,
            'detection_ward_id': self.detection_ward_id,
            'detection_area_id': self.detection_area_id,
            'detection_camera_id': self.detection_camera_id

        }


db.create_all()
