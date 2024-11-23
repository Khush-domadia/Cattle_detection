from base import db
from base.com.vo.area_vo import AreaVO
from base.com.vo.camera_vo import CameraVO
from base.com.vo.ward_vo import WardVO
from base.com.vo.zone_vo import ZoneVO


class CameraDAO:
    def insert_camera(self, camera_vo):
        db.session.add(camera_vo)
        db.session.commit()

    def view_camera(self):
        camera_vo_list = db.session.query(ZoneVO, WardVO,
                                          AreaVO, CameraVO) \
            .filter(ZoneVO.zone_id == CameraVO.camera_zone_id) \
            .filter(WardVO.ward_id == CameraVO.camera_ward_id) \
            .filter(AreaVO.area_id == CameraVO.camera_area_id) \
            .all()
        return camera_vo_list

    def delete_camera(self, camera_vo):
        camera_vo_list = CameraVO.query.get(camera_vo.camera_id)
        db.session.delete(camera_vo_list)
        db.session.commit()
        return camera_vo_list

    def edit_camera(self, camera_vo):
        camera_vo_list = CameraVO.query.filter_by(
            camera_id=camera_vo.camera_id).all()
        db.session.commit()
        return camera_vo_list

    def update_camera(self, camera_vo):
        db.session.merge(camera_vo)
        db.session.commit()

    def count_cameras(self):
        camera_count_list=CameraVO.query.count()
        return camera_count_list

    def view_ajax_ward_detection(self, ward_vo):
        ward_vo_list = WardVO.query.filter_by(
            ward_zone_id=ward_vo.ward_zone_id).all()
        return ward_vo_list

    def view_ajax_area_detection(self, area_vo):
        area_vo_list = AreaVO.query.filter_by(
            area_ward_id=area_vo.area_ward_id).all()
        return area_vo_list

    def view_ajax_camera_detection(self, camera_vo):
        camera_vo_list = CameraVO.query.filter_by(
            camera_area_id=camera_vo.camera_area_id).all()
        return camera_vo_list