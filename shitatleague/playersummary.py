import os
from typing import Callable

from .riotclient import RiotClient


class PlayerSummary:
    def __init__(self, region: str, summoner_id: str, riot_client: RiotClient, callback: Callable[[], None],
                 max_games: int = None):
        self.region = region
        self.summonerId = summoner_id
        self.riotClient = riot_client
        self.callback = callback
        self.maxGames = max_games
        if self.maxGames is None:
            self.maxGames = int(os.environ.get("MAX_GAMES"))

        self.matches = None
        self.matchIds = None
        self.wasSuccessful = False
        self.finishedComputing = False

    def generate(self):
        self.matchIds = self.get_match_ids()
        try:
            for matchId in self.matchIds:
                self.matches[matchId] = self.get_match_by_id(matchId)
            self.wasSuccessful = True
        except RiotClient.APIException:
            print("Exception occurred")
            # TODO
        finally:
            self.finishedComputing = True
            self.callback()

    def is_resolved(self) -> bool:
        return self.finishedComputing

    def was_successful(self) -> bool:
        return self.wasSuccessful

    def get_match_ids(self) -> list:
        encrypted_id = self.riotClient.get_summoner_by_name(self.summonerId)['accountId']
        match_history = self.riotClient.get_matchlist_by_account(encrypted_id)
        number_of_games = min(len(match_history['matches']), self.maxGames)
        # TODO
        return []

    def get_match_by_id(self, match_id: int) -> dict:
        return {}
