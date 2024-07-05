import pytest
import logging

from lesson_11.homework_11 import log_event

@pytest.fixture
def log_capture(caplog):
    caplog.set_level(logging.INFO)
    return caplog

user1 = "user1"
status1 = "success"
# @pytest.mark.positive
# @pytest.mark.skip
def test_log_event_success(caplog):
    log_event(user1, status1)
    assert caplog.messages[0] == f"Login event - Username: {user1}, Status: {status1}"


user2 = "user2"
status2 = "expired"


def test_log_event_expired(caplog):
    log_event(user2, status2)
    assert caplog.messages[0] == f"Login event - Username: {user2}, Status: {status2}"


user3 = "user3"
status3 = "failed"


def test_log_event_failed(caplog):
    log_event(user3, status3)
    assert caplog.messages[0] == f"Login event - Username: {user3}, Status: {status3}"
