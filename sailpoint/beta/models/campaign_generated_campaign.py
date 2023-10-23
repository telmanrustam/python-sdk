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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator
from beta.models.campaign_generated_campaign_campaign_owner import CampaignGeneratedCampaignCampaignOwner


class CampaignGeneratedCampaign(BaseModel):
    """
    Details about the campaign that was generated.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The unique ID of the campaign.")
    name: StrictStr = Field(...,
                            description="Human friendly name of the campaign.")
    description: StrictStr = Field(
        ..., description="Extended description of the campaign.")
    created: datetime = Field(
        ..., description="The date and time the campaign was created.")
    modified: Optional[StrictStr] = Field(
        None, description="The date and time the campaign was last modified.")
    deadline: Optional[StrictStr] = Field(
        None,
        description="The date and time when the campaign must be finished by.")
    type: Dict[str, Any] = Field(
        ..., description="The type of campaign that was generated.")
    campaign_owner: CampaignGeneratedCampaignCampaignOwner = Field(
        ..., alias="campaignOwner")
    status: Dict[str, Any] = Field(
        ..., description="The current status of the campaign.")
    __properties = [
        "id", "name", "description", "created", "modified", "deadline", "type",
        "campaignOwner", "status"
    ]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('MANAGER', 'SOURCE_OWNER', 'SEARCH',
                         'ROLE_COMPOSITION'):
            raise ValueError(
                "must be one of enum values ('MANAGER', 'SOURCE_OWNER', 'SEARCH', 'ROLE_COMPOSITION')"
            )
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('STAGED', 'ACTIVATING', 'ACTIVE'):
            raise ValueError(
                "must be one of enum values ('STAGED', 'ACTIVATING', 'ACTIVE')"
            )
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CampaignGeneratedCampaign:
        """Create an instance of CampaignGeneratedCampaign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of campaign_owner
        if self.campaign_owner:
            _dict['campaignOwner'] = self.campaign_owner.to_dict()
        # set to None if modified (nullable) is None
        # and __fields_set__ contains the field
        if self.modified is None and "modified" in self.__fields_set__:
            _dict['modified'] = None

        # set to None if deadline (nullable) is None
        # and __fields_set__ contains the field
        if self.deadline is None and "deadline" in self.__fields_set__:
            _dict['deadline'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignGeneratedCampaign:
        """Create an instance of CampaignGeneratedCampaign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignGeneratedCampaign.parse_obj(obj)

        _obj = CampaignGeneratedCampaign.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "deadline":
            obj.get("deadline"),
            "type":
            obj.get("type"),
            "campaign_owner":
            CampaignGeneratedCampaignCampaignOwner.from_dict(
                obj.get("campaignOwner"))
            if obj.get("campaignOwner") is not None else None,
            "status":
            obj.get("status")
        })
        return _obj
