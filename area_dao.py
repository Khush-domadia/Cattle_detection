from base import db
from base.com.vo.area_vo import AreaVO
from base.com.vo.ward_vo import WardVO
from base.com.vo.zone_vo import ZoneVO


class AreaDAO:
    def insert_area(self, area_vo):
        db.session.add(area_vo)
        db.session.commit()

    def view_area(self):
        area_vo_list = db.session.query(ZoneVO, WardVO,
                                        AreaVO) \
            .filter(ZoneVO.zone_id == AreaVO.area_zone_id) \
            .filter(
            WardVO.ward_id == AreaVO.area_ward_id) \
            .all()
        return area_vo_list

    def delete_area(self, area_vo):
        area_vo_list = AreaVO.query.get(area_vo.area_id)
        db.session.delete(area_vo_list)
        db.session.commit()
        return area_vo_list

    def edit_area(self, area_vo):
        area_vo_list = AreaVO.query.filter_by(area_id=area_vo.area_id).all()
        return area_vo_list

    def update_area(self, area_vo):
        db.session.merge(area_vo)
        db.session.commit()

    def view_ajax_ward_camera(self, ward_vo):
        ward_vo_list = WardVO.query.filter_by(
            ward_zone_id=ward_vo.ward_zone_id).all()
        return ward_vo_list

    def view_ajax_area_camera(self, area_vo):
        area_vo_list = AreaVO.query.filter_by(
            area_ward_id=area_vo.area_ward_id).all()
        return area_vo_list
