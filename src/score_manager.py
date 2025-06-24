import json
import os
from datetime import datetime

SCORES_FILE = "scores.json"

def load_scores():
    """
    Load and return the list of top scores from the JSON file.

    Returns:
        list of dict: List of score entries sorted by score descending.
                      Each entry contains 'score' (int) and 'date' (str).
                      Returns empty list if file does not exist or is invalid.
    """
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        try:
            scores = json.load(f)
            scores.sort(key=lambda x: x["score"], reverse=True)
            return scores
        except json.JSONDecodeError:
            return []

def add_score(score):
    """
    Add a new score entry to the score list and save top 10 scores to the file.

    Args:
        score (int): The score to add.
    """
    scores = load_scores()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    scores.append({"score": score, "date": now})
    scores.sort(key=lambda x: x["score"], reverse=True)
    scores = scores[:10]  # Keep only top 10 scores
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=4)
