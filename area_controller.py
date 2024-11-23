from flask import request, render_template, redirect, jsonify

from base import app
from base.com.dao.area_dao import AreaDAO
from base.com.dao.ward_dao import WardDAO
from base.com.dao.zone_dao import ZoneDAO
from base.com.vo.area_vo import AreaVO
from base.com.vo.ward_vo import WardVO

@app.route('/load_area')
def load_area():
    zone_dao = ZoneDAO()
    zone_vo_list = zone_dao.view_zone()
    return render_template('admin/addArea.html',
                           zone_vo_list=zone_vo_list)

@app.route('/admin/ajax_ward_area')
def admin_ajax_ward_area():
    ward_vo = WardVO()
    ward_dao = WardDAO()
    area_zone_id = request.args.get('areaZoneId')
    ward_vo.ward_zone_id = area_zone_id
    area_vo_list = ward_dao.view_ajax_ward_area(
        ward_vo)
    ajax_area_ward = [i.as_dict() for i in
                      area_vo_list]
    return jsonify(ajax_area_ward)

@app.route('/admin/insert_area', methods=['POST'])
def admin_insert_area():
    area_name = request.form.get('areaName')
    area_code = request.form.get('areaCode')
    area_zone_id = request.form.get('areaZoneId')
    area_ward_id = request.form.get('areaWardId')

    area_vo = AreaVO()
    area_dao = AreaDAO()

    area_vo.area_name = area_name
    area_vo.area_code = area_code
    area_vo.area_zone_id = area_zone_id
    area_vo.area_ward_id = area_ward_id

    area_dao.insert_area(area_vo)
    return redirect('/admin/view_area')

@app.route('/admin/view_area')
def admin_view_area():
    area_dao = AreaDAO()
    area_vo_list = area_dao.view_area()
    return render_template('admin/viewArea.html',
                           area_vo_list=area_vo_list)

@app.route('/admin/delete_area')
def admin_delete_area():
    area_vo = AreaVO()
    area_dao = AreaDAO()

    area_id = request.args.get('areaId')
    area_vo.area_id = area_id

    area_dao.delete_area(area_vo)
    return redirect('/admin/view_area')

@app.route('/admin/edit_area', methods=['GET'])
def admin_edit_area_view():
    zone_dao = ZoneDAO()
    ward_dao = WardDAO()
    ward_vo = WardVO()
    area_dao = AreaDAO()
    area_vo = AreaVO()

    area_id = request.args.get('areaId')
    area_vo.area_id = area_id
    area_vo_list = area_dao.edit_area(area_vo)
    area_vo_dict = area_vo_list[0].as_dict()
    area_zone_id = area_vo_dict.get("area_zone_id")
    ward_vo.ward_zone_id = area_zone_id
    zone_vo_list = zone_dao.view_zone()
    ward_vo_list = ward_dao.view_ajax_ward_area(ward_vo)

    return render_template('admin/editArea.html',
                           zone_vo_list=zone_vo_list,
                           ward_vo_list=ward_vo_list,
                           area_vo_list=area_vo_list)


@app.route('/admin/update_area', methods=['POST'])
def admin_update_area():
    area_zone_id = request.form.get('areaZoneId')
    area_ward_id = request.form.get('areaWardId')
    area_id = request.form.get('areaId')
    area_name = request.form.get('areaName')
    area_code = request.form.get('areaCode')

    area_vo = AreaVO()
    area_dao = AreaDAO()

    area_vo.area_zone_id = area_zone_id
    area_vo.area_ward_id = area_ward_id
    area_vo.area_id = area_id
    area_vo.area_name = area_name
    area_vo.area_code = area_code

    area_dao.update_area(area_vo)
    return redirect('/admin/view_area')
