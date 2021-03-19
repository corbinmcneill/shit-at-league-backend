import os
from typing import Callable, List

from .matchinfo import MatchInfo
from .riotclient import RiotClient


class PlayerSummary:
    def __init__(self, region: str, summoner_id: str, riot_client: RiotClient, max_games: int = None):
        self.region = region
        self.summonerId = summoner_id
        self.riotClient = riot_client
        self.maxGames = max_games
        print(max_games)
        if max_games is None:
            self.maxGames = int(os.environ.get("MAX_GAMES"))

        self.matchInfo = None
        """
        A list of MatchInfo objects.
        """

    async def generate(self, callback: Callable[[List[MatchInfo]], None]) -> None:
        match_ids = await self.retrieve_match_ids()

        self.matchInfo = []
        for matchId in match_ids:
            self.matchInfo.append(await self.retrieve_match_info_by_id(matchId))

        callback(self.matchInfo)

    async def retrieve_match_ids(self) -> list:
        encrypted_id = (await self.riotClient.get_summoner_by_name(self.summonerId))['accountId']
        match_history = await self.riotClient.get_matchlist_by_account(encrypted_id)
        number_of_games = min(len(match_history['matches']), self.maxGames)

        result = []
        for match in range(number_of_games):
            result.append(match_history['matches'][match]['gameId'])
        return result

    async def retrieve_match_info_by_id(self, match_id: int) -> MatchInfo:
        match_stats = await self.riotClient.get_match_by_match_id(match_id)
        match_timeline = await self.riotClient.get_timeline_by_match_id(match_id)

        return MatchInfo(match_id, match_stats, match_timeline)
