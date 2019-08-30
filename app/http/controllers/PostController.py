"""A PostController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Post import Post

class PostController(Controller):
    """PostController Controller Class."""

    def index(self, view: View):
        return view.render('blog.post.index', {
            'posts': Post.all()
        })

    def show(self, view: View, request: Request):
        post = Post.find(request.param('id'))

        return view.render('blog.post.show', {
            'post': post
        })

    def create(self, view: View):
        return view.render('blog.post.create')

    def store(self, request: Request):
        title = request.input('title')
        body = request.input('body')

        Post.create(title=title, body=body, author_id=1)

        return request.redirect('/blog')
