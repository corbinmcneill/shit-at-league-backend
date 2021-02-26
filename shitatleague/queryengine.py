class QueryEngine:

    VALID_REGIONS = {'BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'RU', 'TR1'}

    class InvalidRegionException(Exception):
        pass

    def __init__(self, api_key: str):
        pass

    async def get_match_history(self, region: str, summoner_id: str) -> list:
        if region not in QueryEngine.VALID_REGIONS:
            raise QueryEngine.InvalidRegionException


    async def get_match_details(self, region: str, match_id: str) -> dict:
        if region not in QueryEngine.VALID_REGIONS:
            raise QueryEngine.InvalidRegionException
