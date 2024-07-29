import pytest
from lesson_16.hw_16_diamond_inheritance import TeamLead

teamlead = TeamLead(name="John", salary=3000, department="RND", programming_language="Python", team_size=10)


@pytest.mark.parametrize("attributes", ["name", "salary", "department", "programming_language"])
def test_class_teamlead(attributes):
    assert hasattr(teamlead, attributes)
