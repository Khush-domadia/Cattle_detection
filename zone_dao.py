from base import db
from base.com.vo.zone_vo import ZoneVO


class ZoneDAO:
    def insert_zone(self, zone_vo):
        db.session.add(zone_vo)
        db.session.commit()

    def view_zone(self):
        zone_vo_list = ZoneVO.query.all()
        return zone_vo_list

    def delete_zone(self, zone_vo):
        zone_vo_list = ZoneVO.query.get(zone_vo.zone_id)
        db.session.delete(zone_vo_list)
        db.session.commit()

    def edit_zone(self, zone_vo):
        zone_vo_list = ZoneVO.query.filter_by(zone_id=zone_vo.zone_id).all()
        return zone_vo_list

    def update_zone(self, zone_vo):
        db.session.merge(zone_vo)
        db.session.commit()
