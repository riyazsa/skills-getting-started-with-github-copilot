from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


_initial_activities = deepcopy(activities)


@pytest.fixture()
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def reset_activities():
    # Keep each test isolated from changes made by earlier tests.
    activities.clear()
    activities.update(deepcopy(_initial_activities))
    yield
    activities.clear()
    activities.update(deepcopy(_initial_activities))