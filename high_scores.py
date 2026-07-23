"""
Module to manage a game player's High Score list.
"""
class HighScores:
    """Class to store a player's High Score and returns its highest score, last added score and the three highest scores when needed.

    Attributes:
        scores (list): The player's scores.
    """
    def __init__(self, scores):
        """Function to initialize the player's scores list."""
        self.scores = scores

    def latest(self):
        """Function returns the latest score that the player got.

        Returns:
            int: The last score that the player got.
        """
        return self.scores[-1]

    def personal_best(self):
        """Function returns the best score that the player got.

        Returns:
            int: The best score that the player got.
        """
        return max(self.scores)

    def personal_top_three(self):
        """Function returns the three best score that the player got.

        Returns:
            list: The three best score that the player got.
        """
        sorted_scores = sorted(self.scores, reverse=True)
        if len(self.scores) > 3:
            return sorted_scores[:3]
        return sorted_scores