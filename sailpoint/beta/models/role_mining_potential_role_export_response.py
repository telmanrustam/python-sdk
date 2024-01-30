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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.role_mining_potential_role_export_state import RoleMiningPotentialRoleExportState
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class RoleMiningPotentialRoleExportResponse(BaseModel):
    """
    RoleMiningPotentialRoleExportResponse
    """

  # noqa: E501
    min_entitlement_popularity: Optional[StrictInt] = Field(
        default=None,
        description=
        "The minimum popularity among identities in the role which an entitlement must have to be included in the report",
        alias="minEntitlementPopularity")
    include_common_access: Optional[StrictBool] = Field(
        default=None,
        description=
        "If false, do not include entitlements that are highly popular among the entire orginization",
        alias="includeCommonAccess")
    export_id: Optional[StrictStr] = Field(
        default=None,
        description="ID used to reference this export",
        alias="exportId")
    status: Optional[RoleMiningPotentialRoleExportState] = None
    __properties: ClassVar[List[str]] = [
        "minEntitlementPopularity", "includeCommonAccess", "exportId", "status"
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
        """Create an instance of RoleMiningPotentialRoleExportResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RoleMiningPotentialRoleExportResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minEntitlementPopularity":
            obj.get("minEntitlementPopularity"),
            "includeCommonAccess":
            obj.get("includeCommonAccess"),
            "exportId":
            obj.get("exportId"),
            "status":
            obj.get("status")
        })
        return _obj
