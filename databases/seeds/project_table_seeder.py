from orator.seeds import Seeder
from app.Project import Project
from config.factories import factory


class ProjectTableSeeder(Seeder):

    def run(self):
        factory(Project, 50).create()
