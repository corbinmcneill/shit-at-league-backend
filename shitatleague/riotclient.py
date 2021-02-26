import requests

class RiotClient:
    """
    This is a client application for riot's developer API capable of making all queries necessary for this library.
    It takes input parameters as either constructor arguments or method parameters and returns the parsed JSON
    response.
    """

    VALID_REGIONS = {'BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'RU', 'TR1'}

    class InvalidRegionException(Exception):
        pass

    class APIException(Exception):
        pass

    def __init__(self, api_key: str, region: str):
        self.apiKey = api_key

        if region not in RiotClient.VALID_REGIONS:
            raise RiotClient.InvalidRegionException
        self.region = region

    def get_summoner_by_name(self, summoner_name: str) -> dict:
        """
        Make a GET call to the /lol/summoner/v4/summoners/by-name/{summonerName} endpoint.
        """
        endpoint_url = "https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(
            self.region,
            summoner_name,
            self.apiKey
        )
        response = requests.get(endpoint_url)
        if response.status_code != 200:
            raise RiotClient.APIException()  # TODO

        return response.json()

    def get_matchlist_by_account(self, encrypted_summoner_id: str) -> dict:
        """
        Make a GET call to the /lol/match/v4/matchlists/by-account/{encryptedAccountId} endpoint.
        """
        endpoint_url = 'https://{}.api.riotgames.com/lol/match/v4/matchlists/by-account/{}}?api_key={}}'.format(
            self.region,
            encrypted_summoner_id,
            self.apiKey
        )
        response = requests.get(endpoint_url)
        if response.status_code != 200:
            raise RiotClient.APIException()  # TODO

        return response.json()

    def get_match_by_match_id(self, match_id: str) -> dict:
        """
        Make a GET call to the /lol/match/v4/matches/{matchId} endpoint.
        """
        pass
