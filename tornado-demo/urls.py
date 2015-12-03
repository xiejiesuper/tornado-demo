# -*- coding: utf-8 -*-
import handlers.auth 
#auth
urls = [
        (r"/signup", handlers.auth.Signup),
        (r"/login", handlers.auth.Login),
        (r"/index", handlers.auth.index),
        (r"/warning", handlers.auth.warning),
       ]
