from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
import time
from datetime import datetime


class LoggerMiddleware(MiddlewareMixin):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


    def process_request(self, request):
        """Set Request Start Time to measure time taken to service request."""
        if request.method in ['GET','POST', 'PUT', 'PATCH']:
            request.req_body = request.body
            request.start_time = datetime.now()
            with open('logs.log' ,"a") as f:
                f.write(f'{request} , {request.start_time}')


    def process_response(self, request, response):
        """Log data using logger."""
        response.start_time = datetime.now()
        with open('logs.log' ,"a") as f:
                f.write(f'{response} , {response.start_time}\n')
        return response



class BlackListMiddleware(MiddlewareMixin):
    IP_BLACK_LIST = [
        '127.0.0.8'
    ]
    def process_view(self,request,*args,**kwargs):
        ip = request.META['REMOTE_ADDR']
        print(ip)
        if ip in self.IP_BLACK_LIST:
            raise PermissionDenied

