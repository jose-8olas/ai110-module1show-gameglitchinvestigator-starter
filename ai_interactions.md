# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked AI to create me a guess history feature to keep track of guesses made before and some documenattion chnages as well. Also, for this challenge, AI identified three potential "edge case" inputs. I used codepath examples.

**What did the agent do?**

The agent inspected the guessing game application and planned the guess history feature. It modified the app.py to add the features adding and modifying the code so that it appears on the sidebar as I intended. It also added some edge test cases and

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

I manually tested the new features and fixes presented by AI. Checked if the guess history correctly displays on teh sidebar as intended. I adjusted minor UI changes.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case                  | Prompt Used                                                                                                                                                                                  | AI-Suggested Test                                                                                                                                                                                                                                     | Did It Pass? | Your Reasoning                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| Edge case Negative num     | For this challenge, identify three potential "edge case" inputs (e.g., negative numbers, decimals, or extremely large values) that might still break the game. can you mkae these edge cases | Genearted three fucntions to handle the 3 cases test_negative_guess_is_rejected(), test_decimal_guess_is_rejected_instead_of_truncated(), and test_extremely_large_guess_is_rejected_without_crashing(). I tested them on test.py and verified myslef | Yes          | Neagtive numbers, decimals, and larger values shouldn't be acccounted for since we have specific ranges |
| edge case for decimals     | For this challenge, identify three potential "edge case" inputs (e.g., negative numbers, decimals, or extremely large values) that might still break the game. can you mkae these edge cases | Genearted three fucntions to handle the 3 cases test_negative_guess_is_rejected(), test_decimal_guess_is_rejected_instead_of_truncated(), and test_extremely_large_guess_is_rejected_without_crashing(). I tested them on test.py and verified myslef | Yes          | Neagtive numbers, decimals, and larger values shouldn't be acccounted for since we have specific ranges |
| Edge case for large values | For this challenge, identify three potential "edge case" inputs (e.g., negative numbers, decimals, or extremely large values) that might still break the game. can you mkae these edge cases | Genearted three fucntions to handle the 3 cases test_negative_guess_is_rejected(), test_decimal_guess_is_rejected_instead_of_truncated(), and test_extremely_large_guess_is_rejected_without_crashing(). I tested them on test.py and verified myslef | Yes          | Neagtive numbers, decimals, and larger values shouldn't be acccounted for since we have specific ranges |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Add professional-grade docstrings to every function in logic_utils.py. Keep the existing functionality unchanged. Make the docstrings clear and concise.

Review logic_utils.py for PEP 8 style compliance. Identify any formatting or naming issues and fix them. Do not change the functionality of the code. After making the changes, explain what you changed.
```

**Linting output before:**

```
$ python -m pycodestyle logic_utils.py
logic_utils.py:40:1: E302 expected 2 blank lines, found 1
(.venv)
```

**Changes applied:**
There was a formatting issue invlvoing only 1 blank line as indicated by the linting output and it expected 2. I asked the AI and it fixed this issue for me quickly without any input from me. This was a simple fix.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

I asked the model to fix the check guessed function that was wrong at the start of proejct

|                          | Model A             | Model B             |
| ------------------------ | ------------------- | ------------------- |
| **Model name**           | gpt 4               | cluade opus         |
| **Response summary**     | good                | good                |
| **More Pythonic?**       | Yes                 | No                  |
| **Clearer explanation?** | Both about the same | Both about the same |

**Which did you prefer and why?**

I think overall I preferroed Chatgpt since it gave me a simple fix. Claude restrutcured the code differently and changed some things.
