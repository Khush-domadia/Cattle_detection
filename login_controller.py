# from flask import render_template, request,redirect,flash
#
# from base import app
# from base.com.dao.login_dao import LoginDAO
# from base.com.dao.camera_dao import CameraDAO
# from base.com.dao.detection_dao import DetectionDAO
#
# @app.route('/')
# def load_login():
#     return render_template('admin/adminLogin.html')
#
#
# @app.route('/admin/load_dashboard', methods=['GET', 'POST'])
# def admin_load_dashboard():
#     username = request.form.get('userName')
#     password = request.form.get('password')
#     login_dao = LoginDAO()
#     # camera_dao = CameraDAO()
#     # camera_count_list = camera_dao.count_cameras()
#     # print(">>>>>>>>",camera_count_list)
#     # detection_dao = DetectionDAO()
#     # detection_count_list = detection_dao.count_detection()
#     # print(">>>>>>>>", detection_count_list)
#     login_vo_list = login_dao.view_login()
#     login_list = [i.as_dict() for i in login_vo_list]
#     if request.method == 'POST':
#         if (login_list[0]["login_username"] == username and
#                 login_list[0]["login_password"]==password) :
#             # flash('Login successful!')
#             return render_template('admin/index.html')
#         else:
#             # flash('Incorrect username or password!')
#             return redirect('/')
#     else:
#         return render_template('admin/index.html')



from flask import render_template, request, redirect, session, flash
from base import app
from base.com.dao.login_dao import LoginDAO

@app.route('/')
def load_login():
    return render_template('admin/adminLogin.html')

@app.route('/admin/load_dashboard', methods=['GET', 'POST'])
def admin_load_dashboard():
    if request.method == 'POST':
        username = request.form.get('userName')
        password = request.form.get('password')
        login_dao = LoginDAO()
        login_vo_list = login_dao.view_login()
        login_list = [i.as_dict() for i in login_vo_list]
        if any(user['login_username'] == username and user['login_password'] == password for user in login_list):
            session['logged_in'] = True
            return render_template('admin/index.html')
        else:
            flash('Incorrect username or password!')
            return redirect('/')
    else:
        if session.get('logged_in'):
            return render_template('admin/index.html')
        else:
            flash('Please log in to access the dashboard!')
            return redirect('/')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')
