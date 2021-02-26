import os

import pytest
from dotenv import load_dotenv

from shitatleague.riotclient import RiotClient

INVALID_SUMMONER_NAME = "This is an invalid summoner name asdfhqwetbasdfasd"

def test_get_summoner_by_name():
    client = RiotClient(os.environ.get("API_KEY"), "NA1")
    result = client.get_summoner_by_name("TheRealMcNeill")
    assert('accountId' in result)

def test_bad_get_summoner_by_name():
    client = RiotClient(os.environ.get("API_KEY"), "NA1")
    with pytest.raises(RiotClient.APIException):
        result = client.get_summoner_by_name(INVALID_SUMMONER_NAME)
