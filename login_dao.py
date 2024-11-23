from base import db
from base.com.vo.login_vo import LoginVO


class LoginDAO:

    def view_login(self):
        login_vo_list = LoginVO.query.all()
        return login_vo_list

    def get_admin_user(self):
        admin_user = LoginVO.query.filter_by(login_role='admin').first()
        return admin_user
