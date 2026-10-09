
"""Tests for the number guessing game's logic utilities."""

from logic_utils import (
    check_guess,
    parse_guess,
    get_range_for_difficulty,
    update_score,
)
# fix code by adding proper docstrings

def test_winning_guess():
    """Test that a correct guess returns a win message."""

    # If the secret is 50 and guess is 50, it should be a win

    result = check_guess(50, 50)

    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high():
    """Test that a guess above the secret returns the Too High hint."""

    # If secret is 50 and guess is 60, hint should be "Too High"

    result = check_guess(60, 50)

    assert result == ("Too High", "📈 Go Lower!")


def test_guess_too_low():
    """Test that a guess below the secret returns the Too Low hint."""

    # If secret is 50 and guess is 40, hint should be "Too Low"

    result = check_guess(40, 50)

    assert result == ("Too Low", "📉 Go Higher!")


def test_negative_guess_is_rejected():
    """Test that a negative guess outside the range is rejected."""

    result = parse_guess("-1", 1, 100)

    assert result == (False, None, "Guess must be between 1 and 100.")


def test_decimal_guess_is_rejected_instead_of_truncated():
    """Test that a decimal guess is rejected instead of truncated."""

    result = parse_guess("50.9", 1, 100)

    assert result == (False, None, "Enter a whole number.")


def test_extremely_large_guess_is_rejected_without_crashing():
    """Test that an extremely large guess is rejected without crashing."""

    result = parse_guess("9" * 5000, 1, 100)

    assert result[0] is False

    assert result[1] is None

    assert result[2] == "Enter a whole number."


def test_easy_difficulty_range():
    """Test that Easy difficulty uses the range 1 to 20."""

    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_difficulty_range():
    """Test that Normal difficulty uses the range 1 to 100."""

    assert get_range_for_difficulty("Normal") == (1, 100)


def test_hard_difficulty_range():
    """Test that Hard difficulty uses the range 1 to 50."""

    assert get_range_for_difficulty("Hard") == (1, 50)


def test_winning_guess_updates_score():
    """Test that a winning guess increases the score."""

    assert update_score(0, "Win", 1) == 80


def test_too_high_guess_updates_score_on_even_attempt():
    """Test that a Too High guess adds 5 points on an even attempt."""

    assert update_score(10, "Too High", 2) == 15


def test_too_high_guess_updates_score_on_odd_attempt():
    """Test that a Too High guess subtracts 5 points on an odd attempt."""

    assert update_score(10, "Too High", 1) == 5


def test_too_low_guess_updates_score():
    """Test that a Too Low guess subtracts 5 points."""

    assert update_score(10, "Too Low", 2) == 5