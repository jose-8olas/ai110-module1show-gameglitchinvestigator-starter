from logic_utils import check_guess, parse_guess
#fix code by adding proper docstrings
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📈 Go Lower!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📉 Go Higher!")

def test_negative_guess_is_rejected():
    result = parse_guess("-1", 1, 100)
    assert result == (False, None, "Guess must be between 1 and 100.")

def test_decimal_guess_is_rejected_instead_of_truncated():
    result = parse_guess("50.9", 1, 100)
    assert result == (False, None, "Enter a whole number.")

def test_extremely_large_guess_is_rejected_without_crashing():
    result = parse_guess("9" * 5000, 1, 100)
    assert result[0] is False
    assert result[1] is None
    assert result[2]
