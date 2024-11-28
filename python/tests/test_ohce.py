import pytest
import ohce
from unittest.mock import Mock, call
from ohce.greeter import Greeter, SystemClock
from ohce.ui import UI, ConsoleInteractor


def test_nightly_greeting():
    """
    Assert that greeter says "Good night" at midnight
    (when current hour is 0)
    """
    greeter = Greeter()
    mock_clock = Mock(spec=SystemClock)
    mock_clock.current_hour.return_value = 0
    greeter.clock = mock_clock

    assert greeter.greet() == "Good night"


def test_greeting_never_returns_none():
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """
    greeter = Greeter()
    mock_clock = Mock(spec=SystemClock)
    
    for hour in range(24):
        mock_clock.current_hour.return_value = hour
        greeter.clock = mock_clock
        assert greeter.greet() is not None


def test_ohce_main_loop():
    """
    Given the following inputs:
    - hello
    - oto
    - quit

    Check that the following messages are printed:
    - olleh
    - oto
    - That was a palindrome!
    """
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
