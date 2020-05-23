import tornado.ioloop
import tornado.web #web应用api
import tornado.options
from tornado.options import define, options

from handlers.main import IndexHandler, ExploreHandler, PostHandler, UpdateHandler
from handlers.users import RegisterHandler, LoginHandler
from handlers.photo import PhotographyHandler, TravelHandler, FashionHandler, AboutHandler, ContactHandler, SingleHandler
from handlers.chat import RoomHandler, EchoWebSocket

define("port", default="8888", help="Listening port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/explore", ExploreHandler),
            (r"/post/(?P<post_id>[0-9]+)", PostHandler),
            (r"/register", RegisterHandler),  #注册
            (r"/login", LoginHandler),        #登录
            (r"/update", UpdateHandler),      #图片上传
            (r"/photography", PhotographyHandler),#摄影
            (r"/travel", TravelHandler),      #旅行
            (r"/fashion", FashionHandler),    #时尚
            (r"/about", AboutHandler),        # 关于我
            (r"/contact", ContactHandler),    # 联系我
            (r"/room", RoomHandler),      #在线咨询
            (r"/echoweb", EchoWebSocket),

        ]

        setting = dict(
            debug=True,
            template_path="templates", #配置模板路径
            static_path="statics",
            xsrf_cookies=True,     #拦截个人信息的作用 ，跨站点请求伪造保护
            cookie_secret="sdwededad-deddfdfed",
            pycket={
                'engine': 'redis',
                'storage': {
                    'host': '192.168.2.162',  #ip
                    'port': 6379,
                    'db_sessions': 7,
                    'max_connections': 2 ** 31,
                },
                'cookies': {
                    # 设置过期时间
                    'expires_days': 2,
                    #‘expires‘:None, #秒
                },
            },
            login_url="/login",
        )

        super().__init__(handlers, **setting)

if __name__ == "__main__": #只有在当前文件运行的时候才会执行
    tornado.options.parse_command_line()  #命令行
    application = Application()  #实例化
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start() #开启tornado服务