from flask import request, render_template, redirect, jsonify

from base import app
from base.com.dao import camera_dao
from base.com.dao.area_dao import AreaDAO
from base.com.dao.camera_dao import CameraDAO
from base.com.dao.ward_dao import WardDAO
from base.com.dao.zone_dao import ZoneDAO
from base.com.vo.area_vo import AreaVO
from base.com.vo.camera_vo import CameraVO
from base.com.vo.ward_vo import WardVO


@app.route('/load_camera')
def load_camera():
    zone_dao = ZoneDAO()
    zone_vo_list = zone_dao.view_zone()
    return render_template('admin/addCamera.html',
                           zone_vo_list=zone_vo_list)


@app.route('/admin/ajax_ward_camera')
def admin_ajax_ward_camera():
    ward_vo = WardVO()
    area_dao = AreaDAO()

    camera_zone_id = request.args.get('cameraZoneId')
    ward_vo.ward_zone_id = camera_zone_id

    camera_vo_list = area_dao.view_ajax_ward_camera(
        ward_vo)
    ajax_camera_ward = [i.as_dict() for i in
                        camera_vo_list]
    return jsonify(ajax_camera_ward)


@app.route('/admin/ajax_area_camera')
def admin_ajax_area_camera():
    area_vo = AreaVO()
    area_dao = AreaDAO()

    camera_ward_id = request.args.get('cameraWardId')
    area_vo.area_ward_id = camera_ward_id

    camera_vo_list = area_dao.view_ajax_area_camera(
        area_vo)
    ajax_camera_area = [i.as_dict() for i in
                        camera_vo_list]

    return jsonify(ajax_camera_area)


@app.route('/admin/insert_camera', methods=['POST'])
def admin_insert_camera():
    camera_zone_id = request.form.get('cameraZoneId')
    camera_ward_id = request.form.get('cameraWardId')
    camera_area_id = request.form.get('cameraAreaId')
    camera_name = request.form.get('cameraName')
    camera_code = request.form.get('cameraCode')
    camera_link = request.form.get('cameraLink')

    camera_vo = CameraVO()
    camera_dao = CameraDAO()

    camera_vo.camera_zone_id = camera_zone_id
    camera_vo.camera_ward_id = camera_ward_id
    camera_vo.camera_area_id = camera_area_id
    camera_vo.camera_name = camera_name
    camera_vo.camera_code = camera_code
    camera_vo.camera_link = camera_link

    camera_dao.insert_camera(camera_vo)
    return redirect('/admin/view_camera')


@app.route('/admin/view_camera')
def admin_view_camera():
    camera_dao = CameraDAO()
    camera_vo_list = camera_dao.view_camera()
    return render_template('admin/viewCamera.html',
                           camera_vo_list=camera_vo_list)

@app.route('/admin/delete_camera')
def admin_delete_camera():
    camera_vo = CameraVO()
    camera_dao = CameraDAO()

    camera_id = request.args.get('cameraId')
    camera_vo.camera_id = camera_id

    camera_dao.delete_camera(camera_vo)
    return redirect('/admin/view_camera')


@app.route('/admin/edit_camera', methods=['GET'])
def admin_edit_camera_view():
    camera_vo = CameraVO()
    camera_dao = CameraDAO()
    zone_dao = ZoneDAO()
    ward_vo = WardVO()
    area_vo = AreaVO()
    ward_dao = WardDAO()
    area_dao = AreaDAO()

    camera_id = request.args.get('cameraId')
    camera_vo.camera_id = camera_id
    camera_vo_list = camera_dao.edit_camera(camera_vo)
    camera_vo_dict = camera_vo_list[0].as_dict()
    camera_zone_id = camera_vo_dict.get("camera_zone_id")
    ward_vo.ward_zone_id = camera_zone_id
    ward_vo_list = ward_dao.view_ajax_ward_area(ward_vo)
    camera_ward_id = camera_vo_dict.get("camera_ward_id")
    area_vo.area_ward_id = camera_ward_id
    area_vo_list = area_dao.view_ajax_area_camera(area_vo)

    zone_vo_list = zone_dao.view_zone()
    return render_template('admin/editCamera.html',
                           zone_vo_list=zone_vo_list,
                           ward_vo_list=ward_vo_list,
                           area_vo_list=area_vo_list,
                           camera_vo_list=camera_vo_list)


@app.route('/admin/update_camera', methods=['POST'])
def update_camera():
    camera_id = request.form.get('cameraId')
    camera_name = request.form.get('cameraName')
    camera_code = request.form.get('cameraCode')
    camera_link = request.form.get('cameraLink')
    camera_zone_id = request.form.get('cameraZoneId')
    camera_ward_id = request.form.get('cameraWardId')
    camera_area_id = request.form.get('cameraAreaId')

    camera_vo = CameraVO()
    camera_dao = CameraDAO()

    camera_vo.camera_id = camera_id
    camera_vo.camera_name = camera_name
    camera_vo.camera_code = camera_code
    camera_vo.camera_link = camera_link
    camera_vo.camera_zone_id = camera_zone_id
    camera_vo.camera_ward_id = camera_ward_id
    camera_vo.camera_area_id = camera_area_id

    camera_dao.update_camera(camera_vo)
    return redirect('/admin/view_camera')
