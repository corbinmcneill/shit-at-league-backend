from typing import Optional


class Fact:
    """
    A fact is an interesting observation about a game, usually related to a performance of a particular player in that
    game. Score measures the relevancy of this fact for down stream curating purposes, while first_line and
    second_line are the contents of the message.
    """
    def __init__(self, score: float, first_line: str, second_line: Optional[str] = None):
        self.score = score
        """
        A score to measure the relevance of this particular fact between -1 and 1, where 1 is most relevant and -1 is
        least relevant.
        """

        self.firstLine = first_line
        self.secondLine = second_line
