import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.player import Player  # noqa: E501
from swagger_server import util


def get_player(summoner_name, region):  # noqa: E501
    """Get the shit summary for a particular player

     # noqa: E501

    :param summoner_name: ID of the user
    :type summoner_name: str
    :param region: Region of the player
    :type region: str

    :rtype: Player
    """
    return 'do some magic!'


def root():  # noqa: E501
    """Simple endpoint ping

     # noqa: E501


    :rtype: str
    """
    return 'do some magic!'
