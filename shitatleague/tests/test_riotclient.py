import os

import pytest

from shitatleague.riotclient import RiotClient


REGION = "NA1"

VALID_SUMMONER_NAME = "TheRealMcNeill"
INVALID_SUMMONER_NAME = "This is an invalid summoner name asdfhqwetbasdfasd"

VALID_ENCRYPTED_SUMMONER_ID = "BWAdvevdyjtvBowVkHdw6OsK86jrKHjRiDH7cUToZFIwHoM"
INVALID_ENCRYPTED_SUMMONER_ID = "BWAdvevdyjtvBowVkHdw6O-------------------"

VALID_MATCH_ID = 3802359829
INVALID_MATCH_ID = 99999999999999999


@pytest.mark.asyncio
async def test_get_summoner_by_name():
    client = RiotClient(os.environ.get("API_KEY"), REGION)
    result = await client.get_summoner_by_name(VALID_SUMMONER_NAME)
    assert 'accountId' in result


@pytest.mark.asyncio
async def test_bad_get_summoner_by_name():
    client = RiotClient(os.environ.get("API_KEY"), REGION)
    with pytest.raises(RiotClient.APIException):
        await client.get_summoner_by_name(INVALID_SUMMONER_NAME)


@pytest.mark.asyncio
async def test_get_matchlist_by_account():
    client = RiotClient(os.environ.get("API_KEY"), REGION)
    result = await client.get_matchlist_by_account(VALID_ENCRYPTED_SUMMONER_ID)
    assert 'matches' in result


@pytest.mark.asyncio
async def test_bad_get_matchlist_by_account():
    client = RiotClient(os.environ.get("API_KEY"), REGION)
    with pytest.raises(RiotClient.APIException):
        await client.get_matchlist_by_account(INVALID_ENCRYPTED_SUMMONER_ID)


@pytest.mark.asyncio
async def test_get_match_by_match_id():
    client = RiotClient(os.environ.get("API_KEY"), REGION)
    result = await client.get_match_by_match_id(VALID_MATCH_ID)
    assert 'teams' in result


@pytest.mark.asyncio
async def test_bad_match_by_match_id():
    client = RiotClient(os.environ.get("API_KEY"), REGION)
    with pytest.raises(RiotClient.APIException):
        await client.get_match_by_match_id(INVALID_MATCH_ID)


@pytest.mark.asyncio
async def test_get_timeline_by_match_id():
    client = RiotClient(os.environ.get("API_KEY"), REGION)
    result = await client.get_timeline_by_match_id(VALID_MATCH_ID)
    assert 'frames' in result


@pytest.mark.asyncio
async def test_bad_get_timeline_by_match_id():
    client = RiotClient(os.environ.get("API_KEY"), REGION)
    with pytest.raises(RiotClient.APIException):
        await client.get_timeline_by_match_id(INVALID_MATCH_ID)
