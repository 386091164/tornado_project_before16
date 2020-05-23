import tornado.web


class PhotographyHandler(tornado.web.RequestHandler):
    """
    摄影
    """
    def get(self):
        return self.render("photography.html")

class TravelHandler(tornado.web.RequestHandler):
    """
    旅行
    """
    def get(self):
        return self.render("travel.html")


class FashionHandler(tornado.web.RequestHandler):
    """
    旅行
    """
    def get(self):
        return self.render("fashion.html")

class AboutHandler(tornado.web.RequestHandler):
    """
    关于我
    """
    def get(self):
        return self.render("about.html")

class ContactHandler(tornado.web.RequestHandler):
    """
    联系我
    """
    def get(self):
        return self.render("contact.html")

class SingleHandler(tornado.web.RequestHandler):
    """
    分享资源
    """
    def get(self):
        return self.render("single.html")