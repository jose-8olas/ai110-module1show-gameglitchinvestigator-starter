def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guess bounds for a difficulty level.

    Args:
        difficulty: The selected difficulty name.

    Returns:
        A ``(low, high)`` tuple of inclusive integer bounds.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def parse_guess(raw: str, low: int = 1, high: int = 100):
    """Parse text as an integer guess and validate it against inclusive bounds.

    Args:
        raw: The input text to parse.
        low: The minimum permitted guess.
        high: The maximum permitted guess.

    Returns:
        A tuple of success status, parsed guess (or ``None``), and error
        message (or ``None``).
    """
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except (TypeError, ValueError):
        return False, None, "Enter a whole number."

    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """Compare a guess with the secret and return its outcome and hint.

    Args:
        guess: The player's guess.
        secret: The game's secret value.

    Returns:
        A tuple containing ``"Win"``, ``"Too High"``, or ``"Too Low"`` and
        the corresponding player-facing hint.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📈 Go Lower!"
        else:
            return "Too Low", "📉 Go Higher!"
    except TypeError:
        guess_text = str(guess)
        if guess_text == secret:
            return "Win", "🎉 Correct!"
        if guess_text > secret:
            return "Too High", "📈 Go Lower!"
        return "Too Low", "📉 Go Higher!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Calculate the updated score for a guess outcome.

    Args:
        current_score: The player's score before this outcome.
        outcome: The result label for the guess.
        attempt_number: The one-based number of the current attempt.

    Returns:
        The score after applying the outcome's scoring rule.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )
