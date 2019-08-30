"""A ProjectController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Project import Project
from masonite.request import Request

class ProjectController(Controller):
    """ProjectController Controller Class."""

    def __init__(self, request: Request):
        """ProjectController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: View):
        projects = Project.all()

        return view.render('projects', {
            'name': 'Joe',
            'projects': projects,
        })
    
    def show(self, view: View, request: Request):
        project = Project.find(request.param('id'))

        return view.render('projects', {
            'name': 'Joe',
            'project': project,
        })
