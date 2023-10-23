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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from beta.models.role_mining_role_type import RoleMiningRoleType
from beta.models.role_mining_session_scope import RoleMiningSessionScope
from beta.models.role_mining_session_status import RoleMiningSessionStatus


class RoleMiningSessionResponse(BaseModel):
    """
    RoleMiningSessionResponse
    """
    scope: Optional[RoleMiningSessionScope] = None
    min_num_identities_in_potential_role: Optional[StrictInt] = Field(
        None,
        alias="minNumIdentitiesInPotentialRole",
        description="Minimum number of identities in a potential role")
    prescribed_prune_threshold: Optional[StrictInt] = Field(
        None,
        alias="prescribedPruneThreshold",
        description=
        "The computed (or prescribed) prune threshold for this session")
    prune_threshold: Optional[StrictInt] = Field(
        None,
        alias="pruneThreshold",
        description=
        "The prune threshold to be used for this role mining session")
    potential_role_count: Optional[StrictInt] = Field(
        None,
        alias="potentialRoleCount",
        description="The number of potential roles")
    potential_roles_ready_count: Optional[StrictInt] = Field(
        None,
        alias="potentialRolesReadyCount",
        description=
        "The number of potential roles which have completed processing")
    status: Optional[RoleMiningSessionStatus] = None
    id: Optional[StrictStr] = Field(
        None, description="Session Id for this role mining session")
    created_date: Optional[datetime] = Field(
        None,
        alias="createdDate",
        description="The date-time when this role mining session was created.")
    modified_date: Optional[datetime] = Field(
        None,
        alias="modifiedDate",
        description="The date-time when this role mining session was completed."
    )
    type: Optional[RoleMiningRoleType] = None
    __properties = [
        "scope", "minNumIdentitiesInPotentialRole", "prescribedPruneThreshold",
        "pruneThreshold", "potentialRoleCount", "potentialRolesReadyCount",
        "status", "id", "createdDate", "modifiedDate", "type"
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
    def from_json(cls, json_str: str) -> RoleMiningSessionResponse:
        """Create an instance of RoleMiningSessionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleMiningSessionResponse:
        """Create an instance of RoleMiningSessionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleMiningSessionResponse.parse_obj(obj)

        _obj = RoleMiningSessionResponse.parse_obj({
            "scope":
            RoleMiningSessionScope.from_dict(obj.get("scope"))
            if obj.get("scope") is not None else None,
            "min_num_identities_in_potential_role":
            obj.get("minNumIdentitiesInPotentialRole"),
            "prescribed_prune_threshold":
            obj.get("prescribedPruneThreshold"),
            "prune_threshold":
            obj.get("pruneThreshold"),
            "potential_role_count":
            obj.get("potentialRoleCount"),
            "potential_roles_ready_count":
            obj.get("potentialRolesReadyCount"),
            "status":
            RoleMiningSessionStatus.from_dict(obj.get("status"))
            if obj.get("status") is not None else None,
            "id":
            obj.get("id"),
            "created_date":
            obj.get("createdDate"),
            "modified_date":
            obj.get("modifiedDate"),
            "type":
            obj.get("type")
        })
        return _obj
