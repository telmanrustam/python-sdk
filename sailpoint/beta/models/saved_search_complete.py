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

from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.beta.models.saved_search_complete_search_results import SavedSearchCompleteSearchResults
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SavedSearchComplete(BaseModel):
    """
    SavedSearchComplete
    """

  # noqa: E501
    file_name: StrictStr = Field(description="A name for the report file.",
                                 alias="fileName")
    owner_email: StrictStr = Field(
        description=
        "The email address of the identity that owns the saved search.",
        alias="ownerEmail")
    owner_name: StrictStr = Field(
        description="The name of the identity that owns the saved search.",
        alias="ownerName")
    query: StrictStr = Field(
        description="The search query that was used to generate the report.")
    search_name: StrictStr = Field(description="The name of the saved search.",
                                   alias="searchName")
    search_results: SavedSearchCompleteSearchResults = Field(
        alias="searchResults")
    signed_s3_url: StrictStr = Field(
        description="The Amazon S3 URL to download the report from.",
        alias="signedS3Url")
    __properties: ClassVar[List[str]] = [
        "fileName", "ownerEmail", "ownerName", "query", "searchName",
        "searchResults", "signedS3Url"
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
        """Create an instance of SavedSearchComplete from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of search_results
        if self.search_results:
            _dict['searchResults'] = self.search_results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SavedSearchComplete from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fileName":
            obj.get("fileName"),
            "ownerEmail":
            obj.get("ownerEmail"),
            "ownerName":
            obj.get("ownerName"),
            "query":
            obj.get("query"),
            "searchName":
            obj.get("searchName"),
            "searchResults":
            SavedSearchCompleteSearchResults.from_dict(
                obj.get("searchResults"))
            if obj.get("searchResults") is not None else None,
            "signedS3Url":
            obj.get("signedS3Url")
        })
        return _obj
