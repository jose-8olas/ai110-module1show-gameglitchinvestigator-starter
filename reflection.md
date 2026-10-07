# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Two bugs I saw is that whenver changing difficulty, the range of numbers coressponding to the diffuclty will not update on the center of the page. Also, another bug is that whenever a user guessed a number that was higher than the secret number, the app will say that the number was too low meaning we will need to go higher.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                            | Expected Behavior                                                     | Actual Behavior                                                                                                 | Console Output / Error |
| ------------------------------------------------ | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------- |
| When I entered 60 with secret lower than 60      | Show TOO HIGH and tell player to go lower                             | It returned GO Higher                                                                                           | None                   |
| Check the attempts display before making a guess | The number of attempts allowed and attempts should be the same        | The sidebar shows the full attempt limit, while the center display one less.                                    | None                   |
| Change difficulty from Normal to Hard            | The game should update the secret number and use the appropiate range | The sidebar changes to 1–50, but the existing secret number is not reset and may still be outside the new range | None observed          |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used the built-in Copilot AI as well as Claude Code for this project.

An example, when AI was correct was when I was asking it why my current application was not chnaging the ranges when we chnaged difficulty. It told me that the low and high variables where not being used and that we had to make several chnages throughout the code. It also fixed resetting secert when we chnage difficulty since each difficulty has a different range of numbers

Suggestions from AI:

    st.sidebar.caption(f"Range: {low} to {high}")

    if "secret_difficulty" not in st.session_state:
      st.session_state.secret = random.randint(low, high)
      st.session_state.secret_difficulty = difficulty
    elif st.session_state.secret_difficulty != difficulty:
      st.session_state.secret = random.randint(low, high)
      st.session_state.secret_difficulty = difficulty
      st.session_state.attempts = 0
      st.session_state.score = 0
      st.session_state.status = "playing"
      st.session_state.history = []

Now, one time where I prevented AI from chnaging my code was when I was asking it why my current application was telling the using to guess higher when they were supposed to guess lower. I asked AI to tell me why and it expalined to me that the outputs messages where reversed. It rewrote my code into something a little bit more diffrent and changed the strcuture of the code.
Here is an example:
def check_guess(guess, secret):
try:
difference = int(guess) - int(secret)
except (TypeError, ValueError):
return "Invalid", "⚠️ That guess couldn't be checked."

    if difference == 0:
        return "Win", "🎉 Correct!"
    elif difference > 0:
        return "Too High", "📈 Go Lower!"
    else:
        return "Too Low", "📉 Go Higher!"

The code was not doing anything wrong but the messages where in the wrong places. So i adjusted the code accordingly. So i followed advice of Claude but not copy pasted their code. The fix was very simple.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

For debugging, I used pytest and also tested the changes myself to actually verify if the changes are accuarte and good. For example for the check_guess function, I collaborated with AI to change the issue of displaying GO HIGHER when in reality the number we inputted we should be guessing lower. I created a test_game_logic.py to test 3 different scenarios. All tests were passed, but I wanted to see for myself if in the actual application those changes were visbile and working.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns the python when there is some interaction. Streamlit helps the application remember information between these runs. Take the example of this guessing game, we have attempts, secert number, and score. These are stored in st.session state. This lets the user guess a number everytime without forgetting the progress they have done.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I will implement in future labs is using pytests to test my chnages in my code to see if these actually are fixed. I will also manually check these chnages to make sure. I feel AI is very helpful in many aspects since it can point out things that need fixes in my code relativey quickly, however, these changes need to be verified first. It can really help save time and energy.
