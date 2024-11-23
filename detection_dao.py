from base import db
from base.com.vo.area_vo import AreaVO
from base.com.vo.camera_vo import CameraVO
from base.com.vo.ward_vo import WardVO
from base.com.vo.zone_vo import ZoneVO
from base.com.vo.detection_vo import DetectionVO


class DetectionDAO:
    def insert_detection(self, detection_vo):
        db.session.add(detection_vo)
        db.session.commit()

    def view_detection(self):
        detection_vo_list = db.session.query(ZoneVO, WardVO,
                                          AreaVO, CameraVO,DetectionVO) \
            .filter(ZoneVO.zone_id == DetectionVO.detection_zone_id) \
            .filter(WardVO.ward_id == DetectionVO.detection_ward_id) \
            .filter(AreaVO.area_id == DetectionVO.detection_area_id) \
            .filter(CameraVO.camera_id == DetectionVO.detection_camera_id) \
            .all()

        return detection_vo_list

    def delete_detection(self, detection_id):
        detection_vo_list = DetectionVO.query.get(detection_id)
        db.session.delete(detection_vo_list)
        db.session.commit()
        return detection_vo_list

    def count_detection(self):
        detection_count_list = DetectionVO.query.count()
        return detection_count_list