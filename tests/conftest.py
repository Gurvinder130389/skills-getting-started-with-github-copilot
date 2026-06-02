import pytest
from copy import deepcopy
import src.app as app_module

original_activities = deepcopy(app_module.activities)

@pytest.fixture(autouse=True)
def reset_activities():
    yield
    app_module.activities = deepcopy(original_activities)
