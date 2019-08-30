"""HelloWorld Middleware."""

from masonite.request import Request


class HelloWorldMiddleware:
    """HelloWorld Middleware."""

    def __init__(self, request: Request):
        """Inject Any Dependencies From The Service Container.

        Arguments:
            Request {masonite.request.Request} -- The Masonite request object
        """
        self.request = request

    def before(self):
        print('Hello World')

    def after(self):
        print('Goodbye World')
