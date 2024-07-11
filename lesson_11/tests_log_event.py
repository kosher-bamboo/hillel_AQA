import pytest

from lesson_11.homework_11 import log_event


@pytest.mark.positive
class TestLogEventPositive:

    users = ("user1", "user2", "user3", "", 13)
    statuses = ("success", "expired", "failed", "", 13)
    input_values = list(zip(users, statuses))

    @pytest.mark.parametrize("users, statuses", input_values, ids=statuses)
    def test_log_event_positive(self, caplog, users, statuses):
        log_event(users, statuses)
        assert len(caplog.records) == 1
        assert caplog.messages[0] == f"Login event - Username: {users}, Status: {statuses}"
