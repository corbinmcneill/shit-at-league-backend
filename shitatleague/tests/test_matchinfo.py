import os

import pytest

from shitatleague.matchinfo import MatchInfo
from shitatleague.playersummary import PlayerSummary
from shitatleague.riotclient import RiotClient


@pytest.mark.asyncio
async def test_player_process():
    max_games = 5

    client = RiotClient(os.environ.get("API_KEY"), "NA1")
    ps = PlayerSummary("NA1", "TheRealMcNeill", client, max_games)
    await ps.generate(lambda x: None)

    match_info_item = ps.matchInfo[0]

    assert isinstance(match_info_item, MatchInfo)
    assert isinstance(match_info_item.matchId, int)
    assert isinstance(match_info_item.summonerName, str)
    assert isinstance(match_info_item.matchStats, dict)
    assert isinstance(match_info_item.timeline, dict)

    assert isinstance(match_info_item.participantId, int)
    assert 0 <= match_info_item.participantId <= 9
