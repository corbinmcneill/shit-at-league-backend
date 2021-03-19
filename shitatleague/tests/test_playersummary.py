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

    assert isinstance(ps.matchInfo, list)
    assert len(ps.matchInfo) <= max_games

    for item in ps.matchInfo:
        assert isinstance(item, MatchInfo)
