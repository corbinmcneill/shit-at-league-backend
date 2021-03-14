import asyncio
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

    async def generate(self) -> None:
        try:
            self.matchIds = await self.retrieve_match_ids()
            self.matches = await self.retrieve_matches_by_ids(self.matchIds)
            self.wasSuccessful = True
        except RiotClient.APIException:
            print("Exception occurred")
            # TODO
        finally:
            self.finishedComputing = True
            self.callback()

    async def retrieve_match_ids(self) -> list:
        encrypted_id = (await self.riotClient.get_summoner_by_name(self.summonerId))['accountId']
        match_history = await self.riotClient.get_matchlist_by_account(encrypted_id)
        number_of_games = min(len(match_history['matches']), self.maxGames)

        result = []
        for match in range(number_of_games):
            result.append(match_history['matches'][match]['gameId'])
        return result

    async def retrieve_matches_by_ids(self, match_ids: list) -> list:
        aws = []
        for match_id in match_ids:
            aws.append(self.riotClient.get_match_by_match_id(match_id))
        done, _ = await asyncio.wait(aws)

        result = {}
        for item in done:
            item_result = item.result()
            result[item_result['gameId']] = item_result

        return result
