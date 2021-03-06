# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_odu_odu_common_pac import TapiOduOduCommonPac  # noqa: F401,E501
from tapi_server.models.tapi_odu_odu_ctp_pac import TapiOduOduCtpPac  # noqa: F401,E501
from tapi_server.models.tapi_odu_odu_protection_pac import TapiOduOduProtectionPac  # noqa: F401,E501
from tapi_server.models.tapi_odu_odu_termination_and_client_adaptation_pac import TapiOduOduTerminationAndClientAdaptationPac  # noqa: F401,E501
from tapi_server import util


class TapiOduOduConnectionEndPointSpec(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, odu_term_and_adapter=None, odu_common=None, odu_ctp=None, odu_protection=None):  # noqa: E501
        """TapiOduOduConnectionEndPointSpec - a model defined in OpenAPI

        :param odu_term_and_adapter: The odu_term_and_adapter of this TapiOduOduConnectionEndPointSpec.  # noqa: E501
        :type odu_term_and_adapter: TapiOduOduTerminationAndClientAdaptationPac
        :param odu_common: The odu_common of this TapiOduOduConnectionEndPointSpec.  # noqa: E501
        :type odu_common: TapiOduOduCommonPac
        :param odu_ctp: The odu_ctp of this TapiOduOduConnectionEndPointSpec.  # noqa: E501
        :type odu_ctp: TapiOduOduCtpPac
        :param odu_protection: The odu_protection of this TapiOduOduConnectionEndPointSpec.  # noqa: E501
        :type odu_protection: TapiOduOduProtectionPac
        """
        self.openapi_types = {
            'odu_term_and_adapter': TapiOduOduTerminationAndClientAdaptationPac,
            'odu_common': TapiOduOduCommonPac,
            'odu_ctp': TapiOduOduCtpPac,
            'odu_protection': TapiOduOduProtectionPac
        }

        self.attribute_map = {
            'odu_term_and_adapter': 'odu-term-and-adapter',
            'odu_common': 'odu-common',
            'odu_ctp': 'odu-ctp',
            'odu_protection': 'odu-protection'
        }

        self._odu_term_and_adapter = odu_term_and_adapter
        self._odu_common = odu_common
        self._odu_ctp = odu_ctp
        self._odu_protection = odu_protection

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduOduConnectionEndPointSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.OduConnectionEndPointSpec of this TapiOduOduConnectionEndPointSpec.  # noqa: E501
        :rtype: TapiOduOduConnectionEndPointSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def odu_term_and_adapter(self):
        """Gets the odu_term_and_adapter of this TapiOduOduConnectionEndPointSpec.


        :return: The odu_term_and_adapter of this TapiOduOduConnectionEndPointSpec.
        :rtype: TapiOduOduTerminationAndClientAdaptationPac
        """
        return self._odu_term_and_adapter

    @odu_term_and_adapter.setter
    def odu_term_and_adapter(self, odu_term_and_adapter):
        """Sets the odu_term_and_adapter of this TapiOduOduConnectionEndPointSpec.


        :param odu_term_and_adapter: The odu_term_and_adapter of this TapiOduOduConnectionEndPointSpec.
        :type odu_term_and_adapter: TapiOduOduTerminationAndClientAdaptationPac
        """

        self._odu_term_and_adapter = odu_term_and_adapter

    @property
    def odu_common(self):
        """Gets the odu_common of this TapiOduOduConnectionEndPointSpec.


        :return: The odu_common of this TapiOduOduConnectionEndPointSpec.
        :rtype: TapiOduOduCommonPac
        """
        return self._odu_common

    @odu_common.setter
    def odu_common(self, odu_common):
        """Sets the odu_common of this TapiOduOduConnectionEndPointSpec.


        :param odu_common: The odu_common of this TapiOduOduConnectionEndPointSpec.
        :type odu_common: TapiOduOduCommonPac
        """

        self._odu_common = odu_common

    @property
    def odu_ctp(self):
        """Gets the odu_ctp of this TapiOduOduConnectionEndPointSpec.


        :return: The odu_ctp of this TapiOduOduConnectionEndPointSpec.
        :rtype: TapiOduOduCtpPac
        """
        return self._odu_ctp

    @odu_ctp.setter
    def odu_ctp(self, odu_ctp):
        """Sets the odu_ctp of this TapiOduOduConnectionEndPointSpec.


        :param odu_ctp: The odu_ctp of this TapiOduOduConnectionEndPointSpec.
        :type odu_ctp: TapiOduOduCtpPac
        """

        self._odu_ctp = odu_ctp

    @property
    def odu_protection(self):
        """Gets the odu_protection of this TapiOduOduConnectionEndPointSpec.


        :return: The odu_protection of this TapiOduOduConnectionEndPointSpec.
        :rtype: TapiOduOduProtectionPac
        """
        return self._odu_protection

    @odu_protection.setter
    def odu_protection(self, odu_protection):
        """Sets the odu_protection of this TapiOduOduConnectionEndPointSpec.


        :param odu_protection: The odu_protection of this TapiOduOduConnectionEndPointSpec.
        :type odu_protection: TapiOduOduProtectionPac
        """

        self._odu_protection = odu_protection
