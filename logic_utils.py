
def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guess bounds for a difficulty level."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int = 1, high: int = 100):
    """Parse and validate a whole-number guess."""
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except (TypeError, ValueError):
        return False, None, "Enter a whole number."

    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess: int, secret: int):
    """Compare a guess with the secret number."""
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go Lower!"
    return "Too Low", "📉 Go Higher!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the score using the game's existing scoring rules."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score