# -*- coding: utf-8 -*-
import tornado.web
import json
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    
    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id: return None
        return self.db.get("SELECT * FROM _user_info WHERE _user_id = %s", int(user_id))
    
    def check_xsrf_cookie(self):
        token = (self.get_argument("_xsrf", None) or
                 self.request.headers.get("X-Xsrftoken") or
                 self.request.headers.get("X-Csrftoken"))
        if not token:
            self.xsrf_token
            #raise tornado.web.HTTPError(403)
        if self.xsrf_token != token:
            self.xsrf_token
            #raise tornado.web.HTTPError(403)
    @classmethod
    def code(cls,code):
        info = {'type':cls.__name__,'code':code,'msg':_response_types.get(code,'unkown')}
        return json.dumps(info,encoding='UTF-8', ensure_ascii=False)
            
_response_types = {1000: "ok",
                1001: "缺少参数或有参数为空",
                1002: "参数格式不符要求",
                1003: "用户已存在",
                1004: "用户未注册",
                1005: "用户名、密码不匹配",
                1006: "未登录"}