# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import torndb
import urls

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="album", help="database name")
define("mysql_user", default="root", help="bdatabase user")
define("mysql_password", default="", help="database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls.urls
        settings = dict(
            xsrf_cookies=True,
            cookie_secret="aB7e44l6SxOzp0sgsVBHkEd0LybETUu5l2j3+mZ1q/Y=",
            debug=True,
            login_url="/warning",
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)



if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
