import json
from agents import function_tool

USER_PROFILE_FILE = "user_profile.json"

@function_tool
def read_user_profile() -> dict:
    """Reads the user's profile from a JSON file."""
    try:
        with open(USER_PROFILE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@function_tool
def update_user_profile(key: str, value: str) -> str:
    """Updates a specific key in the user's profile and saves it to a JSON file."""
    try:
        with open(USER_PROFILE_FILE, "r") as f:
            profile = json.load(f)
    except FileNotFoundError:
        profile = {}
    
    profile[key] = value
    
    with open(USER_PROFILE_FILE, "w") as f:
        json.dump(profile, f)
        
    return f"Updated profile with {key}: {value}"

@function_tool
def summarize_text(text: str) -> str:
    """
    Summarizes the given text.
    This function represents a tool that would interact with an LLM to generate a summary.
    For now, it returns a mock summary.
    """
    # In a real scenario, this would call an LLM to summarize the text
    print(f"Summarizing text (first 200 chars): {text[:200]}...")
    return f"This is a mock summary of the provided text. The original text had {len(text)} characters."

@function_tool
def generate_quiz(text: str) -> str:
    """
    Generates a quiz (MCQs or mixed-style) from the given text.
    This function represents a tool that would interact with an LLM to generate a quiz.
    For now, it returns a mock quiz.
    """
    # In a real scenario, this would call an LLM to generate a quiz
    print(f"Generating quiz from text (first 200 chars): {text[:200]}...")
    mock_quiz = """
    Question 1: What is the main topic of the text?
    a) Option A
    b) Option B
    c) Option C
    d) Option D
    Correct Answer: a) Option A

    Question 2: According to the text, what is a key detail?
    a) Detail X
    b) Detail Y
    c) Detail Z
    d) Detail W
    Correct Answer: b) Detail Y
    """
    return f"This is a mock quiz generated from the provided text. The original text had {len(text)} characters.\n{mock_quiz}"