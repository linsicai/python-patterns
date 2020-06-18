"""
@author: Gordeev Andrey <gordeev.and.and@gmail.com>

*TL;DR
Provides a centralized entry point that controls and manages request handling.
"""

# 前端控制器
# 将特定请求分配到请求分配器上，分配器根据请求做不同操作


# 手机视图
class MobileView:
    def show_index_page(self):
        print('Displaying mobile index page')

# 表视图
class TabletView:
    def show_index_page(self):
        print('Displaying tablet index page')

# 分配器
class Dispatcher:
    def __init__(self):
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()

    def dispatch(self, request):
        if request.type == Request.mobile_type:
            self.mobile_view.show_index_page()
        elif request.type == Request.tablet_type:
            self.tablet_view.show_index_page()
        else:
            print('cant dispatch the request')

# 请求控制器
class RequestController:
    """ front controller """

    def __init__(self):
        self.dispatcher = Dispatcher()

    def dispatch_request(self, request):
        if isinstance(request, Request):
            self.dispatcher.dispatch(request)
        else:
            print('request must be a Request object')


class Request:
    """ request """

    mobile_type = 'mobile'
    tablet_type = 'tablet'

    def __init__(self, request):
        self.type = None
        request = request.lower()
        if request == self.mobile_type:
            self.type = self.mobile_type
        elif request == self.tablet_type:
            self.type = self.tablet_type


if __name__ == '__main__':
    front_controller = RequestController()
    front_controller.dispatch_request(Request('mobile'))
    front_controller.dispatch_request(Request('tablet'))

    front_controller.dispatch_request(Request('desktop'))
    front_controller.dispatch_request('mobile')


### OUTPUT ###
# Displaying mobile index page
# Displaying tablet index page
# cant dispatch the request
# request must be a Request object
