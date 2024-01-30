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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from sailpoint.beta.models.attribute_definition import AttributeDefinition
from sailpoint.beta.models.source_feature import SourceFeature
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ModelSchema(BaseModel):
    """
    ModelSchema
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(default=None,
                                    description="The id of the Schema.")
    name: Optional[StrictStr] = Field(default=None,
                                      description="The name of the Schema.")
    native_object_type: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of the object type on the native system that the schema represents.",
        alias="nativeObjectType")
    identity_attribute: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of the attribute used to calculate the unique identifier for an object in the schema.",
        alias="identityAttribute")
    display_attribute: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of the attribute used to calculate the display value for an object in the schema.",
        alias="displayAttribute")
    hierarchy_attribute: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of the attribute whose values represent other objects in a hierarchy. Only relevant to group schemas.",
        alias="hierarchyAttribute")
    include_permissions: Optional[StrictBool] = Field(
        default=None,
        description=
        "Flag indicating whether or not the include permissions with the object data when aggregating the schema.",
        alias="includePermissions")
    features: Optional[List[SourceFeature]] = Field(
        default=None, description="The features that the schema supports.")
    configuration: Optional[Dict[str, Any]] = Field(
        default=None,
        description=
        "Holds any extra configuration data that the schema may require.")
    attributes: Optional[List[AttributeDefinition]] = Field(
        default=None,
        description="The attribute definitions which form the schema.")
    created: Optional[datetime] = Field(
        default=None, description="The date the Schema was created.")
    modified: Optional[datetime] = Field(
        default=None, description="The date the Schema was last modified.")
    __properties: ClassVar[List[str]] = [
        "id", "name", "nativeObjectType", "identityAttribute",
        "displayAttribute", "hierarchyAttribute", "includePermissions",
        "features", "configuration", "attributes", "created", "modified"
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
        """Create an instance of ModelSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ModelSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "nativeObjectType":
            obj.get("nativeObjectType"),
            "identityAttribute":
            obj.get("identityAttribute"),
            "displayAttribute":
            obj.get("displayAttribute"),
            "hierarchyAttribute":
            obj.get("hierarchyAttribute"),
            "includePermissions":
            obj.get("includePermissions"),
            "features":
            obj.get("features"),
            "configuration":
            obj.get("configuration"),
            "attributes": [
                AttributeDefinition.from_dict(_item)
                for _item in obj.get("attributes")
            ] if obj.get("attributes") is not None else None,
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified")
        })
        return _obj
