# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from beta.models.full_account import FullAccount
from beta.models.slim_account import SlimAccount
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

LISTACCOUNTS200RESPONSEINNER_ANY_OF_SCHEMAS = ["FullAccount", "SlimAccount"]


class ListAccounts200ResponseInner(BaseModel):
    """
    ListAccounts200ResponseInner
    """

    # data type: SlimAccount
    anyof_schema_1_validator: Optional[SlimAccount] = None
    # data type: FullAccount
    anyof_schema_2_validator: Optional[FullAccount] = None
    if TYPE_CHECKING:
        actual_instance: Union[FullAccount, SlimAccount]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(
        LISTACCOUNTS200RESPONSEINNER_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = ListAccounts200ResponseInner.construct()
        error_messages = []
        # validate data type: SlimAccount
        if not isinstance(v, SlimAccount):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `SlimAccount`")
        else:
            return v

        # validate data type: FullAccount
        if not isinstance(v, FullAccount):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `FullAccount`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError(
                "No match found when setting the actual_instance in ListAccounts200ResponseInner with anyOf schemas: FullAccount, SlimAccount. Details: "
                + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ListAccounts200ResponseInner:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ListAccounts200ResponseInner:
        """Returns the object represented by the json string"""
        instance = ListAccounts200ResponseInner.construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[SlimAccount] = None
        try:
            instance.actual_instance = SlimAccount.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[FullAccount] = None
        try:
            instance.actual_instance = FullAccount.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into ListAccounts200ResponseInner with anyOf schemas: FullAccount, SlimAccount. Details: "
                + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())
