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
from sailpoint.v3.models.campaign_all_of_role_composition_campaign_info_remediator_ref import CampaignAllOfRoleCompositionCampaignInfoRemediatorRef
from sailpoint.v3.models.campaign_all_of_search_campaign_info_reviewer import CampaignAllOfSearchCampaignInfoReviewer
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CampaignAllOfRoleCompositionCampaignInfo(BaseModel):
    """
    Optional configuration options for role composition campaigns.
    """ # noqa: E501
    reviewer: Optional[CampaignAllOfSearchCampaignInfoReviewer] = None
    role_ids: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "Optional list of roles to include in this campaign. Only one of `roleIds` and `query` may be set; if neither are set, all roles are included.",
        alias="roleIds")
    remediator_ref: CampaignAllOfRoleCompositionCampaignInfoRemediatorRef = Field(
        alias="remediatorRef")
    query: Optional[StrictStr] = Field(
        default=None,
        description=
        "Optional search query to scope this campaign to a set of roles. Only one of `roleIds` and `query` may be set; if neither are set, all roles are included."
    )
    description: Optional[StrictStr] = Field(
        default=None,
        description=
        "Describes this role composition campaign. Intended for storing the query used, and possibly the number of roles selected/available."
    )
    __properties: ClassVar[List[str]] = [
        "reviewer", "roleIds", "remediatorRef", "query", "description"
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
        """Create an instance of CampaignAllOfRoleCompositionCampaignInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reviewer
        if self.reviewer:
            _dict['reviewer'] = self.reviewer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remediator_ref
        if self.remediator_ref:
            _dict['remediatorRef'] = self.remediator_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CampaignAllOfRoleCompositionCampaignInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reviewer":
            CampaignAllOfSearchCampaignInfoReviewer.from_dict(
                obj.get("reviewer"))
            if obj.get("reviewer") is not None else None,
            "roleIds":
            obj.get("roleIds"),
            "remediatorRef":
            CampaignAllOfRoleCompositionCampaignInfoRemediatorRef.from_dict(
                obj.get("remediatorRef"))
            if obj.get("remediatorRef") is not None else None,
            "query":
            obj.get("query"),
            "description":
            obj.get("description")
        })
        return _obj
