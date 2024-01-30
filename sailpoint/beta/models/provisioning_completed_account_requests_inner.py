# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from sailpoint.beta.models.provisioning_completed_account_requests_inner_attribute_requests_inner import ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner
from sailpoint.beta.models.provisioning_completed_account_requests_inner_source import ProvisioningCompletedAccountRequestsInnerSource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ProvisioningCompletedAccountRequestsInner(BaseModel):
    """
    ProvisioningCompletedAccountRequestsInner
    """

  # noqa: E501
    source: ProvisioningCompletedAccountRequestsInnerSource
    account_id: Optional[StrictStr] = Field(
        default=None,
        description="The unique idenfier of the account being provisioned.",
        alias="accountId")
    account_operation: StrictStr = Field(
        description=
        "The provisioning operation; typically Create, Modify, Enable, Disable, Unlock, or Delete.",
        alias="accountOperation")
    provisioning_result: Dict[str, Any] = Field(
        description=
        "The overall result of the provisioning transaction; this could be success, pending, failed, etc.",
        alias="provisioningResult")
    provisioning_target: StrictStr = Field(
        description=
        "The name of the provisioning channel selected; this could be the same as the source, or could be a Service Desk Integration Module (SDIM).",
        alias="provisioningTarget")
    ticket_id: Optional[StrictStr] = Field(
        default=None,
        description=
        "A reference to a tracking number, if this is sent to a Service Desk Integration Module (SDIM).",
        alias="ticketId")
    attribute_requests: Optional[List[
        ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner]] = Field(
            default=None,
            description=
            "A list of attributes as part of the provisioning transaction.",
            alias="attributeRequests")
    __properties: ClassVar[List[str]] = [
        "source", "accountId", "accountOperation", "provisioningResult",
        "provisioningTarget", "ticketId", "attributeRequests"
    ]

    @field_validator('provisioning_result')
    def provisioning_result_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SUCCESS', 'PENDING', 'FAILED'):
            raise ValueError(
                "must be one of enum values ('SUCCESS', 'PENDING', 'FAILED')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProvisioningCompletedAccountRequestsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_requests (list)
        _items = []
        if self.attribute_requests:
            for _item in self.attribute_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributeRequests'] = _items
        # set to None if ticket_id (nullable) is None
        # and model_fields_set contains the field
        if self.ticket_id is None and "ticket_id" in self.model_fields_set:
            _dict['ticketId'] = None

        # set to None if attribute_requests (nullable) is None
        # and model_fields_set contains the field
        if self.attribute_requests is None and "attribute_requests" in self.model_fields_set:
            _dict['attributeRequests'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProvisioningCompletedAccountRequestsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "source":
            ProvisioningCompletedAccountRequestsInnerSource.from_dict(
                obj.get("source")) if obj.get("source") is not None else None,
            "accountId":
            obj.get("accountId"),
            "accountOperation":
            obj.get("accountOperation"),
            "provisioningResult":
            obj.get("provisioningResult"),
            "provisioningTarget":
            obj.get("provisioningTarget"),
            "ticketId":
            obj.get("ticketId"),
            "attributeRequests": [
                ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner
                .from_dict(_item) for _item in obj.get("attributeRequests")
            ] if obj.get("attributeRequests") is not None else None
        })
        return _obj
