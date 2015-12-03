# -*- coding: utf-8 -*-
import tornado.web
import hashlib
from basehandler import BaseHandler
class Signup(BaseHandler):
    def post(self):
        userId = self.get_argument("userID", None)
        password = self.get_argument("password", None)
        username = self.get_argument("username", None)
        if userId and password and username:
            if len(userId)==11 and userId.isdigit() and len(password)>=6:
                count = self.db.get('select 1 from _user_info where _user_id = %d limit 1;'%(long(userId)))
                if count:
                    self.write(self.code(1003))
                else:
                    m = hashlib.md5()  
                    m.update(password)
                    pasd = m.hexdigest()
                    sql = "INSERT INTO _user_info (_user_id,_user_name,_user_pwd,_user_phone) VALUES (%d,'%s','%s','%s')"%(long(userId),username,pasd,userId)
                    self.db.execute(sql)
                    self.write(self.code(1000))
            else:
                self.write(self.code(1002))
        else:
            self.write(self.code(1001))
         
class Login(BaseHandler):
    def post(self):
        userId = self.get_argument("userID", None)
        password = self.get_argument("password", None)
        if userId and password:
            user = self.db.get('select * from _user_info where _user_id = "%s" limit 1;'%(userId))
            if user==None:
                self.write(self.code(1004))
            else:
                m = hashlib.md5()  
                m.update(password)
                pasd = m.hexdigest()
                if user['_user_pwd']==pasd:
                    self.set_secure_cookie("user",userId )
                    self.write(self.code(1000))
                else:
                    self.write(self.code(1005))
        else:
            self.write(self.code(1001))
           
class index(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        print self.get_current_user()
        self.write('ok')
        
#未登录警告信息        
class warning(BaseHandler):
    def get(self):
        self.write(self.code(1006))