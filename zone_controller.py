from flask import request, render_template, redirect

from base import app
from base.com.dao.zone_dao import ZoneDAO
from base.com.vo.zone_vo import ZoneVO


@app.route('/load_zone')
def load_zone():
    return render_template('admin/addZone.html')


@app.route('/admin/insert_zone', methods=['POST'])
def admin_insert_zone():
    zone_name = request.form.get('zoneName')
    zone_code = request.form.get('zoneCode')

    zone_vo = ZoneVO()
    zone_dao = ZoneDAO()

    zone_vo.zone_name = zone_name
    zone_vo.zone_code = zone_code

    zone_dao.insert_zone(zone_vo)
    return redirect('/admin/view_zone')


@app.route('/admin/view_zone')
def admin_view_zone():
    zone_dao = ZoneDAO()
    zone_vo_list = zone_dao.view_zone()
    return render_template('admin/viewZone.html',
                           zone_vo_list=zone_vo_list)


@app.route('/admin/delete_zone')
def admin_delete_zone():
    zone_vo = ZoneVO()
    zone_dao = ZoneDAO()

    zone_id = request.args.get('zoneId')
    zone_vo.zone_id = zone_id

    zone_dao.delete_zone(zone_vo)
    return redirect('/admin/view_zone')


@app.route('/admin/edit_zone', methods=['GET'])
def admin_edit_zone_view():
    zone_vo = ZoneVO()
    zone_dao = ZoneDAO()

    zone_id = request.args.get('zoneId')
    zone_vo.zone_id = zone_id

    zone_vo_list = zone_dao.edit_zone(zone_vo)
    return render_template('admin/editZone.html',
                           zone_vo_list=zone_vo_list)


@app.route('/admin/update_zone', methods=['POST'])
def admin_update_zone():
    zone_id = request.form.get('zoneId')
    zone_name = request.form.get('zoneName')
    zone_code = request.form.get('zoneCode')

    zone_vo = ZoneVO()
    zone_dao = ZoneDAO()

    zone_vo.zone_id = zone_id
    zone_vo.zone_name = zone_name
    zone_vo.zone_code = zone_code

    zone_dao.update_zone(zone_vo)
    return redirect('/admin/view_zone')
