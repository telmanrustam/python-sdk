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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.beta.models.field_details_dto import FieldDetailsDto
from sailpoint.beta.models.usage_type import UsageType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ProvisioningPolicyDto(BaseModel):
    """
    ProvisioningPolicyDto
    """

  # noqa: E501
    name: StrictStr = Field(description="the provisioning policy name")
    description: Optional[StrictStr] = Field(
        default=None, description="the description of the provisioning policy")
    usage_type: Optional[UsageType] = Field(default=None, alias="usageType")
    fields: Optional[List[FieldDetailsDto]] = None
    __properties: ClassVar[List[str]] = [
        "name", "description", "usageType", "fields"
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
        """Create an instance of ProvisioningPolicyDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProvisioningPolicyDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "usageType":
            obj.get("usageType"),
            "fields":
            [FieldDetailsDto.from_dict(_item) for _item in obj.get("fields")]
            if obj.get("fields") is not None else None
        })
        return _obj
