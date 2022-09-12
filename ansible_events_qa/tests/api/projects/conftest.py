import pytest

from ansible_events_qa.api import api_client


@pytest.fixture
def new_project(teardown_projects):
    """
    Fixture to create a new project with teardown
    """
    project = api_client.projects.create().data
    teardown_projects(project)
    return project


@pytest.fixture
def teardown_projects():
    """
    Deletes projects
    """
    projects = []
    yield projects.append
    for project in projects:
        api_client.projects.delete(project.id)
