class MatchInfo:

    class ParticipantNotFoundException(Exception):
        pass

    """
    The information yielded by the Riot APIs about a particular match.
    """
    def __init__(self, summoner_name: str, match_id: int, match_statistics: dict, timeline: dict):
        self.summonerName = summoner_name
        self.matchId = match_id
        self.matchStats = match_statistics
        self.timeline = timeline

        # calculate the participantId based on summonerName to assist with contextualizing the matchStats and timeline
        self.participantId = None
        participant_id_set = False

        for participantIdentity in self.matchStats['participantIdentities']:
            if participantIdentity['player']['summonerName'] == self.summonerName:
                self.participantId = participantIdentity['participantId']
                participant_id_set = True

        if not participant_id_set:
            raise MatchInfo.ParticipantNotFoundException()
