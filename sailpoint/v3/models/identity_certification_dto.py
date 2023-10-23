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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from v3.models.campaign_reference import CampaignReference
from v3.models.certification_phase import CertificationPhase
from v3.models.reassignment import Reassignment
from v3.models.reviewer import Reviewer


class IdentityCertificationDto(BaseModel):
    """
    IdentityCertificationDto
    """
    id: Optional[StrictStr] = Field(None,
                                    description="id of the certification")
    name: Optional[StrictStr] = Field(None,
                                      description="name of the certification")
    campaign: Optional[CampaignReference] = None
    completed: Optional[StrictBool] = Field(
        None, description="Have all decisions been made?")
    identities_completed: Optional[StrictInt] = Field(
        None,
        alias="identitiesCompleted",
        description=
        "The number of identities for whom all decisions have been made and are complete."
    )
    identities_total: Optional[StrictInt] = Field(
        None,
        alias="identitiesTotal",
        description=
        "The total number of identities in the Certification, both complete and incomplete."
    )
    created: Optional[datetime] = Field(None, description="created date")
    modified: Optional[datetime] = Field(None, description="modified date")
    decisions_made: Optional[StrictInt] = Field(
        None,
        alias="decisionsMade",
        description=
        "The number of approve/revoke/acknowledge decisions that have been made."
    )
    decisions_total: Optional[StrictInt] = Field(
        None,
        alias="decisionsTotal",
        description="The total number of approve/revoke/acknowledge decisions."
    )
    due: Optional[datetime] = Field(
        None, description="The due date of the certification.")
    signed: Optional[datetime] = Field(
        None,
        description="The date the reviewer signed off on the Certification.")
    reviewer: Optional[Reviewer] = None
    reassignment: Optional[Reassignment] = None
    has_errors: Optional[StrictBool] = Field(
        None,
        alias="hasErrors",
        description="Identifies if the certification has an error")
    error_message: Optional[StrictStr] = Field(
        None,
        alias="errorMessage",
        description="Description of the certification error")
    phase: Optional[CertificationPhase] = None
    __properties = [
        "id", "name", "campaign", "completed", "identitiesCompleted",
        "identitiesTotal", "created", "modified", "decisionsMade",
        "decisionsTotal", "due", "signed", "reviewer", "reassignment",
        "hasErrors", "errorMessage", "phase"
    ]

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
    def from_json(cls, json_str: str) -> IdentityCertificationDto:
        """Create an instance of IdentityCertificationDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reviewer
        if self.reviewer:
            _dict['reviewer'] = self.reviewer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reassignment
        if self.reassignment:
            _dict['reassignment'] = self.reassignment.to_dict()
        # set to None if signed (nullable) is None
        # and __fields_set__ contains the field
        if self.signed is None and "signed" in self.__fields_set__:
            _dict['signed'] = None

        # set to None if reassignment (nullable) is None
        # and __fields_set__ contains the field
        if self.reassignment is None and "reassignment" in self.__fields_set__:
            _dict['reassignment'] = None

        # set to None if error_message (nullable) is None
        # and __fields_set__ contains the field
        if self.error_message is None and "error_message" in self.__fields_set__:
            _dict['errorMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityCertificationDto:
        """Create an instance of IdentityCertificationDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityCertificationDto.parse_obj(obj)

        _obj = IdentityCertificationDto.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "campaign":
            CampaignReference.from_dict(obj.get("campaign"))
            if obj.get("campaign") is not None else None,
            "completed":
            obj.get("completed"),
            "identities_completed":
            obj.get("identitiesCompleted"),
            "identities_total":
            obj.get("identitiesTotal"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "decisions_made":
            obj.get("decisionsMade"),
            "decisions_total":
            obj.get("decisionsTotal"),
            "due":
            obj.get("due"),
            "signed":
            obj.get("signed"),
            "reviewer":
            Reviewer.from_dict(obj.get("reviewer"))
            if obj.get("reviewer") is not None else None,
            "reassignment":
            Reassignment.from_dict(obj.get("reassignment"))
            if obj.get("reassignment") is not None else None,
            "has_errors":
            obj.get("hasErrors"),
            "error_message":
            obj.get("errorMessage"),
            "phase":
            obj.get("phase")
        })
        return _obj
