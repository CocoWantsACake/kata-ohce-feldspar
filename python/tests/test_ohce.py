import pytest
import ohce
from unittest.mock import Mock, call
from ohce.greeter import Greeter, SystemClock
from ohce.ui import UI, ConsoleInteractor


@pytest.fixture()
def mock_clock():
    return Mock(spec=SystemClock)


@pytest.fixture()
def greeter(mock_clock):
    greeter = Greeter()
    greeter.clock = mock_clock
    return greeter


def test_nightly_greeting(mock_clock, greeter):
    mock_clock.current_hour.return_value = 0
    assert greeter.greet() == "Good night"


def test_greeting_never_returns_none(mock_clock, greeter):
    for hour in range(24):
        mock_clock.current_hour.return_value = hour
        assert greeter.greet() is not None


def test_ohce_main_loop():
    ui = UI()
    mock_interactor = Mock(spec=ConsoleInteractor)
    mock_interactor.read_input.side_effect = ["hello", "oto", "quit"]
    ui.interactor = mock_interactor

    ui.main_loop()

    mock_interactor.print_message.assert_has_calls([
        call("olleh"),
        call("oto"),
        call("That was a palindrome!")
    ])
