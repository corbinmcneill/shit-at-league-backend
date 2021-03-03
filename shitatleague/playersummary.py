from typing import Callable

from .riotclient import RiotClient


class PlayerSummary:
    def __init__(self, region: str, summoner_id: str, riot_client: RiotClient, callback: Callable[[], None]):
        self.region = region
        self.summonerId = summoner_id
        self.riotClient = riot_client
        self.callback = callback

        self.matches = None
        self.matchIds = None
        self.wasSuccessful = False
        self.finishedComputing = False

    def generate(self):
        # TODO missing stuff here
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

    async def get_match_ids(self) -> list[int]:
        # TODO
        return []

    async def get_match_by_id(self, match_id: int) -> dict:
        return {}
