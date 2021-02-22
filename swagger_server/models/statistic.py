# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Statistic(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, primary: str=None, secondary: str=None):  # noqa: E501
        """Statistic - a model defined in Swagger

        :param primary: The primary of this Statistic.  # noqa: E501
        :type primary: str
        :param secondary: The secondary of this Statistic.  # noqa: E501
        :type secondary: str
        """
        self.swagger_types = {
            'primary': str,
            'secondary': str
        }

        self.attribute_map = {
            'primary': 'primary',
            'secondary': 'secondary'
        }
        self._primary = primary
        self._secondary = secondary

    @classmethod
    def from_dict(cls, dikt) -> 'Statistic':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Statistic of this Statistic.  # noqa: E501
        :rtype: Statistic
        """
        return util.deserialize_model(dikt, cls)

    @property
    def primary(self) -> str:
        """Gets the primary of this Statistic.


        :return: The primary of this Statistic.
        :rtype: str
        """
        return self._primary

    @primary.setter
    def primary(self, primary: str):
        """Sets the primary of this Statistic.


        :param primary: The primary of this Statistic.
        :type primary: str
        """
        if primary is None:
            raise ValueError("Invalid value for `primary`, must not be `None`")  # noqa: E501

        self._primary = primary

    @property
    def secondary(self) -> str:
        """Gets the secondary of this Statistic.


        :return: The secondary of this Statistic.
        :rtype: str
        """
        return self._secondary

    @secondary.setter
    def secondary(self, secondary: str):
        """Sets the secondary of this Statistic.


        :param secondary: The secondary of this Statistic.
        :type secondary: str
        """

        self._secondary = secondary
