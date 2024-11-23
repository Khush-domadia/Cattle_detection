import os

from flask import request, render_template, redirect, jsonify
from werkzeug.utils import secure_filename

from base import app
from base.com.dao.camera_dao import CameraDAO
from base.com.dao.detection_dao import DetectionDAO
from base.com.dao.zone_dao import ZoneDAO
from base.com.vo.area_vo import AreaVO
from base.com.vo.camera_vo import CameraVO
from base.com.vo.detection_vo import DetectionVO
from base.com.vo.ward_vo import WardVO
from base.service.detect import add_detection, avi_to_mp4

input = 'base/static/adminResourses/input/'
app.config['input'] = input

output = 'base/static/adminResourses/output/'
app.config['output'] = output

avi_video = 'base/static/adminResourses/avi_video/'
app.config['avi_video'] = avi_video


@app.route('/load_detection')
def load_detection():
    zone_dao = ZoneDAO()
    zone_vo_list = zone_dao.view_zone()
    return render_template('admin/addDetection.html',
                           zone_vo_list=zone_vo_list)


@app.route('/admin/ajax_ward_detection')
def admin_ajax_ward_detection():
    ward_vo = WardVO()
    camera_dao = CameraDAO()

    detection_zone_id = request.args.get('detectionZoneId')
    ward_vo.ward_zone_id = detection_zone_id

    detection_vo_list = camera_dao.view_ajax_ward_detection(
        ward_vo)
    ajax_detection_ward = [i.as_dict() for i in
                           detection_vo_list]
    return jsonify(ajax_detection_ward)


@app.route('/admin/ajax_area_detection')
def admin_ajax_area_detection():
    area_vo = AreaVO()
    camera_dao = CameraDAO()

    detection_ward_id = request.args.get('detectionWardId')
    area_vo.area_ward_id = detection_ward_id

    detection_vo_list = camera_dao.view_ajax_area_detection(
        area_vo)
    ajax_detection_area = [i.as_dict() for i in
                           detection_vo_list]

    return jsonify(ajax_detection_area)


@app.route('/admin/ajax_camera_detection')
def admin_ajax_camera_detection():
    camera_vo = CameraVO()
    camera_dao = CameraDAO()

    detection_area_id = request.args.get('detectionAreaId')
    camera_vo.camera_area_id = detection_area_id

    detection_vo_list = camera_dao.view_ajax_camera_detection(camera_vo)
    ajax_detection_camera = [i.as_dict() for i in detection_vo_list]
    return jsonify(ajax_detection_camera)


@app.route('/admin/insert_detection', methods=['POST'])
def admin_insert_detection():
    detection_id = request.form.get('detectionId')
    detection_zone_id = request.form.get('detectionZoneId')
    detection_ward_id = request.form.get('detectionWardId')
    detection_area_id = request.form.get('detectionAreaId')
    detection_camera_id = request.form.get('detectionCameraId')
    input_image = request.files.get('inputImage')

    input_image_name = secure_filename(input_image.filename)
    input_image_path = os.path.join(app.config['input'])
    input_image.save(os.path.join(input_image_path, input_image_name))

    detection_dao = DetectionDAO()
    detection_vo = DetectionVO()

    detection_vo.detection_id = detection_id
    detection_vo.detection_zone_id = detection_zone_id
    detection_vo.detection_ward_id = detection_ward_id
    detection_vo.detection_area_id = detection_area_id
    detection_vo.detection_camera_id = detection_camera_id
    detection_vo.input_image_name = input_image_name
    detection_vo.input_image_path = input_image_path.replace("base", "..")
    input_image_name_1 = input_image_name.replace(".mp4", "")

    out=add_detection(source=input_image_path + input_image_name,
                  name=input_image_name_1)
    print(out)
    output_image_name = secure_filename("output_video_" +
                                        input_image.filename)
    output_image_path = os.path.join(app.config['output'])

    detection_vo.output_image_name = output_image_name
    detection_vo.output_image_path = output_image_path.replace("base", "..")

    avi_image_name = secure_filename(
        "output_video_" + input_image_name_1 + ".avi")
    avi_image_path = os.path.join(app.config['avi_video'])

    detection_vo.avi_image_name = avi_image_name
    detection_vo.avi_image_path = avi_image_path.replace("base", "..")
    detection_dao.insert_detection(detection_vo)

    avi_to_mp4()

    return redirect("/admin/view_detection")


@app.route('/admin/view_detection')
def admin_view_detection():
    detection_dao = DetectionDAO()
    detection_vo_list = detection_dao.view_detection()
    # print("detection_vo_list>>>>>",detection_vo_list)
    return render_template('admin/viewDetection.html',
                           detection_vo_list=detection_vo_list)


@app.route('/admin/delete_detection')
def admin_delete_detection():
    detection_dao = DetectionDAO()
    detection_vo = DetectionVO()
    detection_id = request.args.get('detectionId')
    detection_vo.detection_id = detection_id
    detection_vo_list = detection_dao.delete_detection(detection_id)
    file_path = (detection_vo_list.input_image_path.replace("..",
                                                            "base") +
                 detection_vo_list.input_image_name)
    file_path_one = (detection_vo_list.output_image_path.replace("..",
                                                                 "base") +
                     detection_vo_list.output_image_name)
    file_path_two = (detection_vo_list.avi_image_path.replace("..",
                                                              "base") +
                     detection_vo_list.avi_image_name)
    os.remove(file_path)
    os.remove(file_path_one)
    os.remove(file_path_two)
    return redirect("/admin/view_detection")
