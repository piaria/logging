# Custom middleware
import logging
import socket
import threading
import uuid
from django.http import HttpRequest, HttpResponse

local = threading.local()


class RequestLogFilter(logging.Filter):
    """
    Log filter , The current request thread's request Information saved to the log record Context
    record with formater Information needed .
    """

    def filter(self, record):
        record.hostname = getattr(local, "hostname", "")  # Host name
        record.dest_ip = getattr(local, "dest_ip", "")  # The server IP
        record.username = getattr(local, "username", "")  # user
        record.source_ip = getattr(local, "source_ip", "")  # client IP
        record.uow = getattr(local, "uow", "")  # Unit of Work ID
        record.request_id = getattr(local, "request_id", "")  # Request ID
        return True


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        self.__process_request(request)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        self.__process_response(request, response)

        return response

    def __process_request(self, request: HttpRequest):
        local.hostname = socket.gethostname()
        local.dest_ip = socket.gethostbyname(local.hostname)
        local.username = request.user.id or "Anonymous"
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR", "")
        if x_forwarded_for:
            source_ip = x_forwarded_for.split(",")[0]  # So this is real ip
        else:
            source_ip = request.META.get("REMOTE_ADDR")  # Get an agent here ip
        local.source_ip = source_ip

        local.uow = request.headers.get("X-UOW", ":(")
        local.request_id = str(uuid.uuid4())

    def __process_response(self, request: HttpRequest, response: HttpResponse):
        return response
