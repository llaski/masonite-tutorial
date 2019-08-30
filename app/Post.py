"""Post Model."""

from config.database import Model
from orator.orm import belongs_to

class Post(Model):
    """Model Definition (generated with love by Masonite) 

    id: integer default: None
    title: string(255) default: None
    body: text(65535) default: None
    author_id: integer default: None
    created_at: datetime(6) default: CURRENT_TIMESTAMP(6)
    updated_at: datetime(6) default: CURRENT_TIMESTAMP(6)
    """

    __fillable__ = ['title', 'body', 'author_id']

    @belongs_to('author_id', 'id')
    def author(self):
        from app.User import User
        return User

