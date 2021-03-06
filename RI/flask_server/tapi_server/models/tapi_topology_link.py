# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_admin_state_pac import TapiCommonAdminStatePac  # noqa: F401,E501
from tapi_server.models.tapi_common_administrative_state import TapiCommonAdministrativeState  # noqa: F401,E501
from tapi_server.models.tapi_common_capacity import TapiCommonCapacity  # noqa: F401,E501
from tapi_server.models.tapi_common_capacity_pac import TapiCommonCapacityPac  # noqa: F401,E501
from tapi_server.models.tapi_common_forwarding_direction import TapiCommonForwardingDirection  # noqa: F401,E501
from tapi_server.models.tapi_common_global_class import TapiCommonGlobalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_layer_protocol_name import TapiCommonLayerProtocolName  # noqa: F401,E501
from tapi_server.models.tapi_common_lifecycle_state import TapiCommonLifecycleState  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server.models.tapi_common_operational_state import TapiCommonOperationalState  # noqa: F401,E501
from tapi_server.models.tapi_topology_cost_characteristic import TapiTopologyCostCharacteristic  # noqa: F401,E501
from tapi_server.models.tapi_topology_latency_characteristic import TapiTopologyLatencyCharacteristic  # noqa: F401,E501
from tapi_server.models.tapi_topology_layer_protocol_transition_pac import TapiTopologyLayerProtocolTransitionPac  # noqa: F401,E501
from tapi_server.models.tapi_topology_node_edge_point_ref import TapiTopologyNodeEdgePointRef  # noqa: F401,E501
from tapi_server.models.tapi_topology_resilience_type import TapiTopologyResilienceType  # noqa: F401,E501
from tapi_server.models.tapi_topology_risk_characteristic import TapiTopologyRiskCharacteristic  # noqa: F401,E501
from tapi_server.models.tapi_topology_risk_parameter_pac import TapiTopologyRiskParameterPac  # noqa: F401,E501
from tapi_server.models.tapi_topology_transfer_cost_pac import TapiTopologyTransferCostPac  # noqa: F401,E501
from tapi_server.models.tapi_topology_transfer_integrity_pac import TapiTopologyTransferIntegrityPac  # noqa: F401,E501
from tapi_server.models.tapi_topology_transfer_timing_pac import TapiTopologyTransferTimingPac  # noqa: F401,E501
from tapi_server.models.tapi_topology_validation_mechanism import TapiTopologyValidationMechanism  # noqa: F401,E501
from tapi_server.models.tapi_topology_validation_pac import TapiTopologyValidationPac  # noqa: F401,E501
from tapi_server import util


class TapiTopologyLink(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, operational_state=None, lifecycle_state=None, administrative_state=None, available_capacity=None, total_potential_capacity=None, name=None, uuid=None, transitioned_layer_protocol_name=None, risk_characteristic=None, cost_characteristic=None, error_characteristic=None, unavailable_time_characteristic=None, server_integrity_process_characteristic=None, delivery_order_characteristic=None, repeat_delivery_characteristic=None, loss_characteristic=None, latency_characteristic=None, validation_mechanism=None, layer_protocol_name=None, resilience_type=None, node_edge_point=None, direction=None):  # noqa: E501
        """TapiTopologyLink - a model defined in OpenAPI

        :param operational_state: The operational_state of this TapiTopologyLink.  # noqa: E501
        :type operational_state: TapiCommonOperationalState
        :param lifecycle_state: The lifecycle_state of this TapiTopologyLink.  # noqa: E501
        :type lifecycle_state: TapiCommonLifecycleState
        :param administrative_state: The administrative_state of this TapiTopologyLink.  # noqa: E501
        :type administrative_state: TapiCommonAdministrativeState
        :param available_capacity: The available_capacity of this TapiTopologyLink.  # noqa: E501
        :type available_capacity: TapiCommonCapacity
        :param total_potential_capacity: The total_potential_capacity of this TapiTopologyLink.  # noqa: E501
        :type total_potential_capacity: TapiCommonCapacity
        :param name: The name of this TapiTopologyLink.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param uuid: The uuid of this TapiTopologyLink.  # noqa: E501
        :type uuid: str
        :param transitioned_layer_protocol_name: The transitioned_layer_protocol_name of this TapiTopologyLink.  # noqa: E501
        :type transitioned_layer_protocol_name: List[str]
        :param risk_characteristic: The risk_characteristic of this TapiTopologyLink.  # noqa: E501
        :type risk_characteristic: List[TapiTopologyRiskCharacteristic]
        :param cost_characteristic: The cost_characteristic of this TapiTopologyLink.  # noqa: E501
        :type cost_characteristic: List[TapiTopologyCostCharacteristic]
        :param error_characteristic: The error_characteristic of this TapiTopologyLink.  # noqa: E501
        :type error_characteristic: str
        :param unavailable_time_characteristic: The unavailable_time_characteristic of this TapiTopologyLink.  # noqa: E501
        :type unavailable_time_characteristic: str
        :param server_integrity_process_characteristic: The server_integrity_process_characteristic of this TapiTopologyLink.  # noqa: E501
        :type server_integrity_process_characteristic: str
        :param delivery_order_characteristic: The delivery_order_characteristic of this TapiTopologyLink.  # noqa: E501
        :type delivery_order_characteristic: str
        :param repeat_delivery_characteristic: The repeat_delivery_characteristic of this TapiTopologyLink.  # noqa: E501
        :type repeat_delivery_characteristic: str
        :param loss_characteristic: The loss_characteristic of this TapiTopologyLink.  # noqa: E501
        :type loss_characteristic: str
        :param latency_characteristic: The latency_characteristic of this TapiTopologyLink.  # noqa: E501
        :type latency_characteristic: List[TapiTopologyLatencyCharacteristic]
        :param validation_mechanism: The validation_mechanism of this TapiTopologyLink.  # noqa: E501
        :type validation_mechanism: List[TapiTopologyValidationMechanism]
        :param layer_protocol_name: The layer_protocol_name of this TapiTopologyLink.  # noqa: E501
        :type layer_protocol_name: List[TapiCommonLayerProtocolName]
        :param resilience_type: The resilience_type of this TapiTopologyLink.  # noqa: E501
        :type resilience_type: TapiTopologyResilienceType
        :param node_edge_point: The node_edge_point of this TapiTopologyLink.  # noqa: E501
        :type node_edge_point: List[TapiTopologyNodeEdgePointRef]
        :param direction: The direction of this TapiTopologyLink.  # noqa: E501
        :type direction: TapiCommonForwardingDirection
        """
        self.openapi_types = {
            'operational_state': TapiCommonOperationalState,
            'lifecycle_state': TapiCommonLifecycleState,
            'administrative_state': TapiCommonAdministrativeState,
            'available_capacity': TapiCommonCapacity,
            'total_potential_capacity': TapiCommonCapacity,
            'name': List[TapiCommonNameAndValue],
            'uuid': str,
            'transitioned_layer_protocol_name': List[str],
            'risk_characteristic': List[TapiTopologyRiskCharacteristic],
            'cost_characteristic': List[TapiTopologyCostCharacteristic],
            'error_characteristic': str,
            'unavailable_time_characteristic': str,
            'server_integrity_process_characteristic': str,
            'delivery_order_characteristic': str,
            'repeat_delivery_characteristic': str,
            'loss_characteristic': str,
            'latency_characteristic': List[TapiTopologyLatencyCharacteristic],
            'validation_mechanism': List[TapiTopologyValidationMechanism],
            'layer_protocol_name': List[TapiCommonLayerProtocolName],
            'resilience_type': TapiTopologyResilienceType,
            'node_edge_point': List[TapiTopologyNodeEdgePointRef],
            'direction': TapiCommonForwardingDirection
        }

        self.attribute_map = {
            'operational_state': 'operational-state',
            'lifecycle_state': 'lifecycle-state',
            'administrative_state': 'administrative-state',
            'available_capacity': 'available-capacity',
            'total_potential_capacity': 'total-potential-capacity',
            'name': 'name',
            'uuid': 'uuid',
            'transitioned_layer_protocol_name': 'transitioned-layer-protocol-name',
            'risk_characteristic': 'risk-characteristic',
            'cost_characteristic': 'cost-characteristic',
            'error_characteristic': 'error-characteristic',
            'unavailable_time_characteristic': 'unavailable-time-characteristic',
            'server_integrity_process_characteristic': 'server-integrity-process-characteristic',
            'delivery_order_characteristic': 'delivery-order-characteristic',
            'repeat_delivery_characteristic': 'repeat-delivery-characteristic',
            'loss_characteristic': 'loss-characteristic',
            'latency_characteristic': 'latency-characteristic',
            'validation_mechanism': 'validation-mechanism',
            'layer_protocol_name': 'layer-protocol-name',
            'resilience_type': 'resilience-type',
            'node_edge_point': 'node-edge-point',
            'direction': 'direction'
        }

        self._operational_state = operational_state
        self._lifecycle_state = lifecycle_state
        self._administrative_state = administrative_state
        self._available_capacity = available_capacity
        self._total_potential_capacity = total_potential_capacity
        self._name = name
        self._uuid = uuid
        self._transitioned_layer_protocol_name = transitioned_layer_protocol_name
        self._risk_characteristic = risk_characteristic
        self._cost_characteristic = cost_characteristic
        self._error_characteristic = error_characteristic
        self._unavailable_time_characteristic = unavailable_time_characteristic
        self._server_integrity_process_characteristic = server_integrity_process_characteristic
        self._delivery_order_characteristic = delivery_order_characteristic
        self._repeat_delivery_characteristic = repeat_delivery_characteristic
        self._loss_characteristic = loss_characteristic
        self._latency_characteristic = latency_characteristic
        self._validation_mechanism = validation_mechanism
        self._layer_protocol_name = layer_protocol_name
        self._resilience_type = resilience_type
        self._node_edge_point = node_edge_point
        self._direction = direction

    @classmethod
    def from_dict(cls, dikt) -> 'TapiTopologyLink':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.topology.Link of this TapiTopologyLink.  # noqa: E501
        :rtype: TapiTopologyLink
        """
        return util.deserialize_model(dikt, cls)

    @property
    def operational_state(self):
        """Gets the operational_state of this TapiTopologyLink.


        :return: The operational_state of this TapiTopologyLink.
        :rtype: TapiCommonOperationalState
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state):
        """Sets the operational_state of this TapiTopologyLink.


        :param operational_state: The operational_state of this TapiTopologyLink.
        :type operational_state: TapiCommonOperationalState
        """

        self._operational_state = operational_state

    @property
    def lifecycle_state(self):
        """Gets the lifecycle_state of this TapiTopologyLink.


        :return: The lifecycle_state of this TapiTopologyLink.
        :rtype: TapiCommonLifecycleState
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """Sets the lifecycle_state of this TapiTopologyLink.


        :param lifecycle_state: The lifecycle_state of this TapiTopologyLink.
        :type lifecycle_state: TapiCommonLifecycleState
        """

        self._lifecycle_state = lifecycle_state

    @property
    def administrative_state(self):
        """Gets the administrative_state of this TapiTopologyLink.


        :return: The administrative_state of this TapiTopologyLink.
        :rtype: TapiCommonAdministrativeState
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state):
        """Sets the administrative_state of this TapiTopologyLink.


        :param administrative_state: The administrative_state of this TapiTopologyLink.
        :type administrative_state: TapiCommonAdministrativeState
        """

        self._administrative_state = administrative_state

    @property
    def available_capacity(self):
        """Gets the available_capacity of this TapiTopologyLink.


        :return: The available_capacity of this TapiTopologyLink.
        :rtype: TapiCommonCapacity
        """
        return self._available_capacity

    @available_capacity.setter
    def available_capacity(self, available_capacity):
        """Sets the available_capacity of this TapiTopologyLink.


        :param available_capacity: The available_capacity of this TapiTopologyLink.
        :type available_capacity: TapiCommonCapacity
        """

        self._available_capacity = available_capacity

    @property
    def total_potential_capacity(self):
        """Gets the total_potential_capacity of this TapiTopologyLink.


        :return: The total_potential_capacity of this TapiTopologyLink.
        :rtype: TapiCommonCapacity
        """
        return self._total_potential_capacity

    @total_potential_capacity.setter
    def total_potential_capacity(self, total_potential_capacity):
        """Sets the total_potential_capacity of this TapiTopologyLink.


        :param total_potential_capacity: The total_potential_capacity of this TapiTopologyLink.
        :type total_potential_capacity: TapiCommonCapacity
        """

        self._total_potential_capacity = total_potential_capacity

    @property
    def name(self):
        """Gets the name of this TapiTopologyLink.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiTopologyLink.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiTopologyLink.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiTopologyLink.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this TapiTopologyLink.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this TapiTopologyLink.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TapiTopologyLink.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this TapiTopologyLink.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def transitioned_layer_protocol_name(self):
        """Gets the transitioned_layer_protocol_name of this TapiTopologyLink.

        Provides the ordered structure of layer protocol transitions encapsulated in the TopologicalEntity. The ordering relates to the LinkPort role.  # noqa: E501

        :return: The transitioned_layer_protocol_name of this TapiTopologyLink.
        :rtype: List[str]
        """
        return self._transitioned_layer_protocol_name

    @transitioned_layer_protocol_name.setter
    def transitioned_layer_protocol_name(self, transitioned_layer_protocol_name):
        """Sets the transitioned_layer_protocol_name of this TapiTopologyLink.

        Provides the ordered structure of layer protocol transitions encapsulated in the TopologicalEntity. The ordering relates to the LinkPort role.  # noqa: E501

        :param transitioned_layer_protocol_name: The transitioned_layer_protocol_name of this TapiTopologyLink.
        :type transitioned_layer_protocol_name: List[str]
        """

        self._transitioned_layer_protocol_name = transitioned_layer_protocol_name

    @property
    def risk_characteristic(self):
        """Gets the risk_characteristic of this TapiTopologyLink.

        A list of risk characteristics for consideration in an analysis of shared risk. Each element of the list represents a specific risk consideration.  # noqa: E501

        :return: The risk_characteristic of this TapiTopologyLink.
        :rtype: List[TapiTopologyRiskCharacteristic]
        """
        return self._risk_characteristic

    @risk_characteristic.setter
    def risk_characteristic(self, risk_characteristic):
        """Sets the risk_characteristic of this TapiTopologyLink.

        A list of risk characteristics for consideration in an analysis of shared risk. Each element of the list represents a specific risk consideration.  # noqa: E501

        :param risk_characteristic: The risk_characteristic of this TapiTopologyLink.
        :type risk_characteristic: List[TapiTopologyRiskCharacteristic]
        """

        self._risk_characteristic = risk_characteristic

    @property
    def cost_characteristic(self):
        """Gets the cost_characteristic of this TapiTopologyLink.

        The list of costs where each cost relates to some aspect of the TopologicalEntity.  # noqa: E501

        :return: The cost_characteristic of this TapiTopologyLink.
        :rtype: List[TapiTopologyCostCharacteristic]
        """
        return self._cost_characteristic

    @cost_characteristic.setter
    def cost_characteristic(self, cost_characteristic):
        """Sets the cost_characteristic of this TapiTopologyLink.

        The list of costs where each cost relates to some aspect of the TopologicalEntity.  # noqa: E501

        :param cost_characteristic: The cost_characteristic of this TapiTopologyLink.
        :type cost_characteristic: List[TapiTopologyCostCharacteristic]
        """

        self._cost_characteristic = cost_characteristic

    @property
    def error_characteristic(self):
        """Gets the error_characteristic of this TapiTopologyLink.

        Describes the degree to which the signal propagated can be errored.                       Applies to TDM systems as the errored signal will be propagated and not packet as errored packets will be discarded.  # noqa: E501

        :return: The error_characteristic of this TapiTopologyLink.
        :rtype: str
        """
        return self._error_characteristic

    @error_characteristic.setter
    def error_characteristic(self, error_characteristic):
        """Sets the error_characteristic of this TapiTopologyLink.

        Describes the degree to which the signal propagated can be errored.                       Applies to TDM systems as the errored signal will be propagated and not packet as errored packets will be discarded.  # noqa: E501

        :param error_characteristic: The error_characteristic of this TapiTopologyLink.
        :type error_characteristic: str
        """

        self._error_characteristic = error_characteristic

    @property
    def unavailable_time_characteristic(self):
        """Gets the unavailable_time_characteristic of this TapiTopologyLink.

        Describes the duration for which there may be no valid signal propagated.  # noqa: E501

        :return: The unavailable_time_characteristic of this TapiTopologyLink.
        :rtype: str
        """
        return self._unavailable_time_characteristic

    @unavailable_time_characteristic.setter
    def unavailable_time_characteristic(self, unavailable_time_characteristic):
        """Sets the unavailable_time_characteristic of this TapiTopologyLink.

        Describes the duration for which there may be no valid signal propagated.  # noqa: E501

        :param unavailable_time_characteristic: The unavailable_time_characteristic of this TapiTopologyLink.
        :type unavailable_time_characteristic: str
        """

        self._unavailable_time_characteristic = unavailable_time_characteristic

    @property
    def server_integrity_process_characteristic(self):
        """Gets the server_integrity_process_characteristic of this TapiTopologyLink.

        Describes the effect of any server integrity enhancement process on the characteristics of the TopologicalEntity.  # noqa: E501

        :return: The server_integrity_process_characteristic of this TapiTopologyLink.
        :rtype: str
        """
        return self._server_integrity_process_characteristic

    @server_integrity_process_characteristic.setter
    def server_integrity_process_characteristic(self, server_integrity_process_characteristic):
        """Sets the server_integrity_process_characteristic of this TapiTopologyLink.

        Describes the effect of any server integrity enhancement process on the characteristics of the TopologicalEntity.  # noqa: E501

        :param server_integrity_process_characteristic: The server_integrity_process_characteristic of this TapiTopologyLink.
        :type server_integrity_process_characteristic: str
        """

        self._server_integrity_process_characteristic = server_integrity_process_characteristic

    @property
    def delivery_order_characteristic(self):
        """Gets the delivery_order_characteristic of this TapiTopologyLink.

        Describes the degree to which packets will be delivered out of sequence.                      Does not apply to TDM as the TDM protocols maintain strict order.  # noqa: E501

        :return: The delivery_order_characteristic of this TapiTopologyLink.
        :rtype: str
        """
        return self._delivery_order_characteristic

    @delivery_order_characteristic.setter
    def delivery_order_characteristic(self, delivery_order_characteristic):
        """Sets the delivery_order_characteristic of this TapiTopologyLink.

        Describes the degree to which packets will be delivered out of sequence.                      Does not apply to TDM as the TDM protocols maintain strict order.  # noqa: E501

        :param delivery_order_characteristic: The delivery_order_characteristic of this TapiTopologyLink.
        :type delivery_order_characteristic: str
        """

        self._delivery_order_characteristic = delivery_order_characteristic

    @property
    def repeat_delivery_characteristic(self):
        """Gets the repeat_delivery_characteristic of this TapiTopologyLink.

        Primarily applies to packet systems where a packet may be delivered more than once (in fault recovery for example).                       It can also apply to TDM where several frames may be received twice due to switching in a system with a large differential propagation delay.  # noqa: E501

        :return: The repeat_delivery_characteristic of this TapiTopologyLink.
        :rtype: str
        """
        return self._repeat_delivery_characteristic

    @repeat_delivery_characteristic.setter
    def repeat_delivery_characteristic(self, repeat_delivery_characteristic):
        """Sets the repeat_delivery_characteristic of this TapiTopologyLink.

        Primarily applies to packet systems where a packet may be delivered more than once (in fault recovery for example).                       It can also apply to TDM where several frames may be received twice due to switching in a system with a large differential propagation delay.  # noqa: E501

        :param repeat_delivery_characteristic: The repeat_delivery_characteristic of this TapiTopologyLink.
        :type repeat_delivery_characteristic: str
        """

        self._repeat_delivery_characteristic = repeat_delivery_characteristic

    @property
    def loss_characteristic(self):
        """Gets the loss_characteristic of this TapiTopologyLink.

        Describes the acceptable characteristic of lost packets where loss may result from discard due to errors or overflow.                      Applies to packet systems and not TDM (as for TDM errored signals are propagated unless grossly errored and overflow/underflow turns into timing slips).  # noqa: E501

        :return: The loss_characteristic of this TapiTopologyLink.
        :rtype: str
        """
        return self._loss_characteristic

    @loss_characteristic.setter
    def loss_characteristic(self, loss_characteristic):
        """Sets the loss_characteristic of this TapiTopologyLink.

        Describes the acceptable characteristic of lost packets where loss may result from discard due to errors or overflow.                      Applies to packet systems and not TDM (as for TDM errored signals are propagated unless grossly errored and overflow/underflow turns into timing slips).  # noqa: E501

        :param loss_characteristic: The loss_characteristic of this TapiTopologyLink.
        :type loss_characteristic: str
        """

        self._loss_characteristic = loss_characteristic

    @property
    def latency_characteristic(self):
        """Gets the latency_characteristic of this TapiTopologyLink.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :return: The latency_characteristic of this TapiTopologyLink.
        :rtype: List[TapiTopologyLatencyCharacteristic]
        """
        return self._latency_characteristic

    @latency_characteristic.setter
    def latency_characteristic(self, latency_characteristic):
        """Sets the latency_characteristic of this TapiTopologyLink.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :param latency_characteristic: The latency_characteristic of this TapiTopologyLink.
        :type latency_characteristic: List[TapiTopologyLatencyCharacteristic]
        """

        self._latency_characteristic = latency_characteristic

    @property
    def validation_mechanism(self):
        """Gets the validation_mechanism of this TapiTopologyLink.

        Provides details of the specific validation mechanism(s) used to confirm the presence of an intended topologicalEntity.  # noqa: E501

        :return: The validation_mechanism of this TapiTopologyLink.
        :rtype: List[TapiTopologyValidationMechanism]
        """
        return self._validation_mechanism

    @validation_mechanism.setter
    def validation_mechanism(self, validation_mechanism):
        """Sets the validation_mechanism of this TapiTopologyLink.

        Provides details of the specific validation mechanism(s) used to confirm the presence of an intended topologicalEntity.  # noqa: E501

        :param validation_mechanism: The validation_mechanism of this TapiTopologyLink.
        :type validation_mechanism: List[TapiTopologyValidationMechanism]
        """

        self._validation_mechanism = validation_mechanism

    @property
    def layer_protocol_name(self):
        """Gets the layer_protocol_name of this TapiTopologyLink.

        none  # noqa: E501

        :return: The layer_protocol_name of this TapiTopologyLink.
        :rtype: List[TapiCommonLayerProtocolName]
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name):
        """Sets the layer_protocol_name of this TapiTopologyLink.

        none  # noqa: E501

        :param layer_protocol_name: The layer_protocol_name of this TapiTopologyLink.
        :type layer_protocol_name: List[TapiCommonLayerProtocolName]
        """

        self._layer_protocol_name = layer_protocol_name

    @property
    def resilience_type(self):
        """Gets the resilience_type of this TapiTopologyLink.


        :return: The resilience_type of this TapiTopologyLink.
        :rtype: TapiTopologyResilienceType
        """
        return self._resilience_type

    @resilience_type.setter
    def resilience_type(self, resilience_type):
        """Sets the resilience_type of this TapiTopologyLink.


        :param resilience_type: The resilience_type of this TapiTopologyLink.
        :type resilience_type: TapiTopologyResilienceType
        """

        self._resilience_type = resilience_type

    @property
    def node_edge_point(self):
        """Gets the node_edge_point of this TapiTopologyLink.

        none  # noqa: E501

        :return: The node_edge_point of this TapiTopologyLink.
        :rtype: List[TapiTopologyNodeEdgePointRef]
        """
        return self._node_edge_point

    @node_edge_point.setter
    def node_edge_point(self, node_edge_point):
        """Sets the node_edge_point of this TapiTopologyLink.

        none  # noqa: E501

        :param node_edge_point: The node_edge_point of this TapiTopologyLink.
        :type node_edge_point: List[TapiTopologyNodeEdgePointRef]
        """

        self._node_edge_point = node_edge_point

    @property
    def direction(self):
        """Gets the direction of this TapiTopologyLink.


        :return: The direction of this TapiTopologyLink.
        :rtype: TapiCommonForwardingDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TapiTopologyLink.


        :param direction: The direction of this TapiTopologyLink.
        :type direction: TapiCommonForwardingDirection
        """

        self._direction = direction
