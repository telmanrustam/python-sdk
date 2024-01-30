# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.v3.models.error_message_dto import ErrorMessageDto
from sailpoint.v3.models.sod_policy_dto import SodPolicyDto
from sailpoint.v3.models.sod_violation_context import SodViolationContext
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SodViolationCheckResult(BaseModel):
    """
    The inner object representing the completed SOD Violation check
    """ # noqa: E501
    message: Optional[ErrorMessageDto] = None
    client_metadata: Optional[Dict[str, StrictStr]] = Field(
        default=None,
        description=
        "Arbitrary key-value pairs. They will never be processed by the IdentityNow system but will be returned on completion of the violation check.",
        alias="clientMetadata")
    violation_contexts: Optional[List[SodViolationContext]] = Field(
        default=None, alias="violationContexts")
    violated_policies: Optional[List[SodPolicyDto]] = Field(
        default=None,
        description="A list of the SOD policies that were violated.",
        alias="violatedPolicies")
    __properties: ClassVar[List[str]] = [
        "message", "clientMetadata", "violationContexts", "violatedPolicies"
    ]

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
        """Create an instance of SodViolationCheckResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in violation_contexts (list)
        _items = []
        if self.violation_contexts:
            for _item in self.violation_contexts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['violationContexts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in violated_policies (list)
        _items = []
        if self.violated_policies:
            for _item in self.violated_policies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['violatedPolicies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SodViolationCheckResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message":
            ErrorMessageDto.from_dict(obj.get("message"))
            if obj.get("message") is not None else None,
            "clientMetadata":
            obj.get("clientMetadata"),
            "violationContexts": [
                SodViolationContext.from_dict(_item)
                for _item in obj.get("violationContexts")
            ] if obj.get("violationContexts") is not None else None,
            "violatedPolicies": [
                SodPolicyDto.from_dict(_item)
                for _item in obj.get("violatedPolicies")
            ] if obj.get("violatedPolicies") is not None else None
        })
        return _obj
