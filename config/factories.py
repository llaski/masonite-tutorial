from orator.orm import Factory
from app.User import User
from app.Project import Project
import random

factory = Factory()


def users_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': '$2b$12$WMgb5Re1NqUr.uSRfQmPQeeGWudk/8/aNbVMpD1dR.Et83vfL8WAu',  # == 'secret'
    }


def project_factory(faker):
    return {
        'name': faker.company(),
        'description': faker.paragraph(),
        'manager_id': random.randint(1, 50)
    }


factory.register(User, users_factory)
factory.register(Project, project_factory)
