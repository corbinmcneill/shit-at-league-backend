from typing import Callable

from .riotclient import RiotClient


class PlayerStats:
    def __init__(self, region: str, summoner_id: str, riot_client: RiotClient, callback: Callable[[], None]):
        self.region = region
        self.summonerId = summoner_id
        self.riotClient = riot_client
        self.wasSuccessful = False
        self.finishedComputing = False

        try:
            self.matchIds = self.get_match_ids();
            self.matches = {}
            for matchId in self.matchIds:
                self.matches[matchId] = self.get_match_by_id(matchId)
            self.wasSuccessful = True
        except Exception:
            print("Exception occurred")
            # TODO
        finally:
            self.finishedComputing = True
            callback()

    def is_resolved(self) -> bool:
        return self.finishedComputing

    def was_successful(self) -> bool:
        return self.wasSuccessful

    async def get_match_ids(self) -> list[int]:
        return self.riotClient.get_match_history(self.region, self.summonerId)

    async def get_match_by_id(self, match_id: int) -> dict:
        return {}
