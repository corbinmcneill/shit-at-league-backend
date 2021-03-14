import os

import pytest

from shitatleague.playersummary import PlayerSummary
from shitatleague.riotclient import RiotClient


@pytest.mark.asyncio
async def test_player_process():
    client = RiotClient(os.environ.get("API_KEY"), "NA1")
    ps = PlayerSummary("NA1", "TheRealMcNeill", client, lambda: None)
    await ps.generate()
    print(ps)

