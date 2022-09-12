import nanoid
import pytest

from ansible_events_api.model.project_create import ProjectCreate
from ansible_events_qa.api import api_client
from ansible_events_qa.config import config


@pytest.mark.qa
@pytest.mark.api
def test_list_projects(new_project: ProjectCreate):
    """
    Test the correct listing of projects
    """
    response = api_client.projects.list()

    assert response.status_code == 200

    # TODO: update it when the endpoint supports pagination
    assert len([project for project in response.data if project.id == new_project.id]) == 1


@pytest.mark.qa
@pytest.mark.api
def test_create_project():
    """
    Test the correct creation of a project
    """
    payload = {
        "name": f"QE-test-{nanoid.generate()}",
        "description": "Test project created by QE",
    }
    response = api_client.projects.create(**payload)

    assert response.status_code == 201
    assert response.data.name == payload["name"]
    assert response.data.description == payload["description"]
    assert response.data.url == config.default_project_url


@pytest.mark.qa
@pytest.mark.api
def test_init_created_project(new_project: ProjectCreate):
    """
    Test that a created project was properly initializated
    """
    project = api_client.projects.show(new_project.id).data
    expected_playbooks = [
        "run_simple_app_test.yml",
        "run_pytest.yml",
        "continuous_integration.yml",
        "continuous_deployment.yml",
    ]
    expected_rulesets = [
        "local-test-rules.yml",
        "github-ci-cd-rules.yml",
        "git-hook-test-rules.yml",
        "git-hook-deploy-rules.yml",
        "ci-cd-rules.yml",
    ]
    assert len(project.inventories) == 1
    assert project.inventories[0].id
    assert project.inventories[0].name == "inventory.yml"

    assert len(project.vars) == 1
    assert project.vars[0].id
    assert project.vars[0].name == "local-vars.yml"

    assert len(project.playbooks) == 4
    assert len([p for p in project.playbooks if p.id]) == 4
    for playbook in expected_playbooks:
        assert any(p for p in project.playbooks if p.name == playbook)

    assert len(project.rulesets) == 5
    assert len([r for r in project.rulesets if r.id]) == 5
    for ruleset in expected_rulesets:
        assert any(r for r in project.rulesets if r.name == ruleset)


@pytest.mark.qa
@pytest.mark.api
def test_show_project(new_project: ProjectCreate):
    """
    Test the correct fetch of a project
    """
    response = api_client.projects.show(new_project.id)

    assert response.status_code == 200
    assert response.data.id == new_project.id
    assert response.data.name == new_project.name
    assert response.data.description == new_project.description
    assert response.data.url == new_project.url


@pytest.mark.qa
@pytest.mark.api
def test_delete_project():
    """
    Test the correct deletion of a project
    """
    project = api_client.projects.create().data
    response = api_client.projects.delete(project.id)
    assert response.status_code == 204

    response = api_client.projects.show(project.id)
    assert response.status_code == 404

    # TODO: https://issues.redhat.com/browse/AAP-5703


@pytest.mark.qa
@pytest.mark.api
def test_update_project(new_project: ProjectCreate):
    """
    Test the correct update of a project
    """
    # TODO: add description when it's implemented
    name = new_project.name + "-updated"

    response = api_client.projects.update(new_project.id, name)

    assert response.status_code == 200
    assert response.data.id == new_project.id
    assert response.data.name == name

    project = api_client.projects.show(new_project.id).data
    assert project.name == name
