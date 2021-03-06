# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_notification_getsupportednotificationtypes_output import TapiNotificationGetsupportednotificationtypesOutput  # noqa: F401,E501
from tapi_server import util


class TapiNotificationGetSupportedNotificationTypes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output=None):  # noqa: E501
        """TapiNotificationGetSupportedNotificationTypes - a model defined in OpenAPI

        :param output: The output of this TapiNotificationGetSupportedNotificationTypes.  # noqa: E501
        :type output: TapiNotificationGetsupportednotificationtypesOutput
        """
        self.openapi_types = {
            'output': TapiNotificationGetsupportednotificationtypesOutput
        }

        self.attribute_map = {
            'output': 'output'
        }

        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'TapiNotificationGetSupportedNotificationTypes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.notification.GetSupportedNotificationTypes of this TapiNotificationGetSupportedNotificationTypes.  # noqa: E501
        :rtype: TapiNotificationGetSupportedNotificationTypes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self):
        """Gets the output of this TapiNotificationGetSupportedNotificationTypes.


        :return: The output of this TapiNotificationGetSupportedNotificationTypes.
        :rtype: TapiNotificationGetsupportednotificationtypesOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TapiNotificationGetSupportedNotificationTypes.


        :param output: The output of this TapiNotificationGetSupportedNotificationTypes.
        :type output: TapiNotificationGetsupportednotificationtypesOutput
        """

        self._output = output
