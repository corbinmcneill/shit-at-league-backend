from .queryengine import QueryEngine


class PlayerStats:
    def __init__(self, region: str, summoner_id: str, query_engine: QueryEngine):
        self.region = region
        self.summonerId = summoner_id
        self.query_engine = query_engine
        self.finishedComputing = False
        self.successful = False

        self.matchIds = self.get_match_ids();
        # TODO

    def is_resolved(self) -> bool:
        return self.finishedComputing

    def was_successful(self) -> bool:
        return self.successful

    async def get_match_ids(self) -> list[int]:
        return []

    async def get_match_by_id(self, match_id: int) -> dict:
        return {}
