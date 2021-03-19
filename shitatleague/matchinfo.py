class MatchInfo:
    """
    The information yielded by the Riot APIs about a particular match.
    """
    def __init__(self, match_id: int, match_statistics: dict, timeline: dict):
        self.matchId = match_id
        self.matchStats = match_statistics
        self.timeline = timeline
