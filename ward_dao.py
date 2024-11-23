from base import db
from base.com.vo.ward_vo import WardVO
from base.com.vo.zone_vo import ZoneVO


class WardDAO:
    def insert_ward(self, ward_vo):
        db.session.add(ward_vo)
        db.session.commit()

    def view_ward(self):
        ward_vo_list = (db.session.query(WardVO, ZoneVO)
                        .join(ZoneVO, WardVO.ward_zone_id == ZoneVO.zone_id)
                        .all())
        return ward_vo_list

    def delete_ward(self, ward_vo):
        ward_vo_list = WardVO.query.get(ward_vo.ward_id)
        db.session.delete(ward_vo_list)
        db.session.commit()

    def edit_ward(self, ward_vo):
        ward_vo_list = WardVO.query.filter_by(
            ward_id=ward_vo.ward_id)
        return ward_vo_list

    def update_ward(self, ward_vo):
        db.session.merge(ward_vo)
        db.session.commit()

    def view_ajax_ward_area(self, ward_vo):
        ward_vo_list = WardVO.query.filter_by(
            ward_zone_id=ward_vo.ward_zone_id).all()
        return ward_vo_list
