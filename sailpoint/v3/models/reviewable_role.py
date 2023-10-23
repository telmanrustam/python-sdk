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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from v3.models.identity_reference_with_name_and_email import IdentityReferenceWithNameAndEmail
from v3.models.reviewable_access_profile import ReviewableAccessProfile


class ReviewableRole(BaseModel):
    """
    ReviewableRole
    """
    id: Optional[StrictStr] = Field(None, description="The id for the Role")
    name: Optional[StrictStr] = Field(None, description="The name of the Role")
    description: Optional[StrictStr] = Field(
        None, description="Information about the Role")
    privileged: Optional[StrictBool] = Field(
        None,
        description="Indicates if the entitlement is a privileged entitlement")
    owner: Optional[IdentityReferenceWithNameAndEmail] = None
    revocable: Optional[StrictBool] = Field(
        None,
        description="Indicates whether the Role can be revoked or requested")
    end_date: Optional[datetime] = Field(
        None,
        alias="endDate",
        description="The date when a user's access expires.")
    access_profiles: Optional[conlist(ReviewableAccessProfile)] = Field(
        None,
        alias="accessProfiles",
        description="The list of Access Profiles associated with this Role")
    __properties = [
        "id", "name", "description", "privileged", "owner", "revocable",
        "endDate", "accessProfiles"
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
    def from_json(cls, json_str: str) -> ReviewableRole:
        """Create an instance of ReviewableRole from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in access_profiles (list)
        _items = []
        if self.access_profiles:
            for _item in self.access_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accessProfiles'] = _items
        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReviewableRole:
        """Create an instance of ReviewableRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReviewableRole.parse_obj(obj)

        _obj = ReviewableRole.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "privileged":
            obj.get("privileged"),
            "owner":
            IdentityReferenceWithNameAndEmail.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "revocable":
            obj.get("revocable"),
            "end_date":
            obj.get("endDate"),
            "access_profiles": [
                ReviewableAccessProfile.from_dict(_item)
                for _item in obj.get("accessProfiles")
            ] if obj.get("accessProfiles") is not None else None
        })
        return _obj
