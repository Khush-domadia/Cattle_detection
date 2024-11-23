from flask import request, render_template, redirect

from base import app
from base.com.dao.ward_dao import WardDAO
from base.com.dao.zone_dao import ZoneDAO
from base.com.vo.ward_vo import WardVO


@app.route('/load_ward')
def load_ward():
    zone_dao = ZoneDAO()
    zone_vo_list = zone_dao.view_zone()

    return render_template('admin/addWard.html',
                           zone_vo_list=zone_vo_list)


@app.route('/admin/insert_ward', methods=['POST'])
def admin_insert_ward():
    ward_name = request.form.get('wardName')
    ward_code = request.form.get('wardCode')
    ward_zone_id = request.form.get('wardZoneId')

    ward_vo = WardVO()
    ward_dao = WardDAO()

    ward_vo.ward_name = ward_name
    ward_vo.ward_code = ward_code
    ward_vo.ward_zone_id = ward_zone_id

    ward_dao.insert_ward(ward_vo)
    return redirect('/admin/view_ward')


@app.route('/admin/view_ward')
def admin_view_ward():
    ward_dao = WardDAO()
    ward_vo_list = ward_dao.view_ward()
    return render_template('admin/viewWard.html',
                           ward_vo_list=ward_vo_list)


@app.route('/admin/delete_ward')
def admin_delete_ward():
    ward_vo = WardVO()
    ward_dao = WardDAO()

    ward_id = request.args.get('wardId')
    ward_vo.ward_id = ward_id

    ward_dao.delete_ward(ward_vo)
    return redirect('/admin/view_ward')


@app.route('/admin/edit_ward', methods=['GET'])
def admin_edit_ward_view():
    ward_vo = WardVO()
    ward_dao = WardDAO()
    zone_dao = ZoneDAO()

    ward_id = request.args.get('wardId')
    ward_vo.ward_id = ward_id

    ward_vo_list = ward_dao.edit_ward(ward_vo)
    zone_vo_list = zone_dao.view_zone()
    return render_template('admin/editWard.html',
                           zone_vo_list=zone_vo_list,
                           ward_vo_list=ward_vo_list)


@app.route('/admin/update_ward', methods=['POST'])
def admin_update_ward():
    ward_id = request.form.get('wardId')
    ward_name = request.form.get('wardName')
    ward_code = request.form.get('wardCode')
    ward_zone_id = request.form.get('wardZoneId')

    ward_vo = WardVO()
    ward_dao = WardDAO()

    ward_vo.ward_id = ward_id
    ward_vo.ward_name = ward_name
    ward_vo.ward_code = ward_code
    ward_vo.ward_zone_id = ward_zone_id

    ward_dao.update_ward(ward_vo)
    return redirect('/admin/view_ward')
