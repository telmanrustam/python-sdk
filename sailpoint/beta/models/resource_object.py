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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ResourceObject(BaseModel):
    """
    Representation of the object which is returned from source connectors.
    """ # noqa: E501
    instance: Optional[StrictStr] = Field(
        default=None,
        description=
        "Identifier of the specific instance where this object resides.")
    identity: Optional[StrictStr] = Field(
        default=None,
        description="Native identity of the object in the Source.")
    uuid: Optional[StrictStr] = Field(
        default=None,
        description="Universal unique identifier of the object in the Source.")
    previous_identity: Optional[StrictStr] = Field(
        default=None,
        description="Native identity that the object has previously.",
        alias="previousIdentity")
    name: Optional[StrictStr] = Field(
        default=None, description="Display name for this object.")
    object_type: Optional[StrictStr] = Field(default=None,
                                             description="Type of object.",
                                             alias="objectType")
    incomplete: Optional[StrictBool] = Field(
        default=None,
        description=
        "A flag indicating that this is an incomplete object. Used in special cases where the connector has to return account information in several phases and the objects might not have a complete set of all account attributes. The attributes in this object will replace the corresponding attributes in the Link, but no other Link attributes will be changed."
    )
    incremental: Optional[StrictBool] = Field(
        default=None,
        description=
        "A flag indicating that this is an incremental change object. This is similar to incomplete but it also means that the values of any multi-valued attributes in this object should be merged with the existing values in the Link rather than replacing the existing Link value."
    )
    delete: Optional[StrictBool] = Field(
        default=None,
        description=
        "A flag indicating that this object has been deleted. This is set only when doing delta aggregation and the connector supports detection of native deletes."
    )
    remove: Optional[StrictBool] = Field(
        default=None,
        description=
        "A flag set indicating that the values in the attributes represent things to remove rather than things to add. Setting this implies incremental. The values which are always for multi-valued attributes are removed from the current values."
    )
    missing: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "A list of attribute names that are not included in this object. This is only used with SMConnector and will only contain \"groups\"."
    )
    attributes: Optional[Dict[str, Any]] = Field(
        default=None, description="Attributes of this ResourceObject.")
    final_update: Optional[StrictBool] = Field(
        default=None,
        description=
        "In Aggregation, for sparse object the count for total accounts scanned identities updated is not incremented.",
        alias="finalUpdate")
    __properties: ClassVar[List[str]] = [
        "instance", "identity", "uuid", "previousIdentity", "name",
        "objectType", "incomplete", "incremental", "delete", "remove",
        "missing", "attributes", "finalUpdate"
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
        """Create an instance of ResourceObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "instance",
                "identity",
                "uuid",
                "previous_identity",
                "name",
                "object_type",
                "incomplete",
                "incremental",
                "delete",
                "remove",
                "missing",
                "attributes",
                "final_update",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ResourceObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "instance":
            obj.get("instance"),
            "identity":
            obj.get("identity"),
            "uuid":
            obj.get("uuid"),
            "previousIdentity":
            obj.get("previousIdentity"),
            "name":
            obj.get("name"),
            "objectType":
            obj.get("objectType"),
            "incomplete":
            obj.get("incomplete"),
            "incremental":
            obj.get("incremental"),
            "delete":
            obj.get("delete"),
            "remove":
            obj.get("remove"),
            "missing":
            obj.get("missing"),
            "attributes":
            obj.get("attributes"),
            "finalUpdate":
            obj.get("finalUpdate")
        })
        return _obj
