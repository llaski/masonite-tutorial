from config.database import Model
from orator.orm import belongs_to

class Project(Model):
    """Model Definition (generated with love by Masonite) 

    id: integer default: None
    name: string(255) default: None
    description: text(65535) default: None
    manager_id: integer default: None
    created_at: datetime(6) default: CURRENT_TIMESTAMP(6)
    updated_at: datetime(6) default: CURRENT_TIMESTAMP(6)
    """

    __fillable__ = ['name', 'description', 'manager_id']

    @belongs_to('manager_id', 'id')
    def manager(self):
        from app.User import User
        return User
