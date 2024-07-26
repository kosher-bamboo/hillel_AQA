import pytest
from lesson_16.hw_16_diamond_inheritance import TeamLead

teamlead = TeamLead(name="John", salary=3000, department="RND", programming_language="Python", team_size=10)

# Manager and Developer classes' attributes available for TeamLead class
attributes = ["name", "salary", "department", "programming_language"]
expected = [True, True, True, True]
params = list(zip(attributes, expected))


@pytest.mark.parametrize("attributes, expected", params, ids=attributes)
def test_class_teamlead(attributes, expected):
    assert hasattr(teamlead, attributes) is expected
