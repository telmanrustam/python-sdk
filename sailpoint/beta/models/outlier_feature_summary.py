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

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from beta.models.outlier_feature_summary_outlier_feature_display_values_inner import OutlierFeatureSummaryOutlierFeatureDisplayValuesInner


class OutlierFeatureSummary(BaseModel):
    """
    OutlierFeatureSummary
    """
    contributing_feature_name: Optional[StrictStr] = Field(
        None,
        alias="contributingFeatureName",
        description="Contributing feature name")
    identity_outlier_display_name: Optional[StrictStr] = Field(
        None,
        alias="identityOutlierDisplayName",
        description="Identity display name")
    outlier_feature_display_values: Optional[conlist(
        OutlierFeatureSummaryOutlierFeatureDisplayValuesInner)] = Field(
            None, alias="outlierFeatureDisplayValues")
    feature_definition: Optional[StrictStr] = Field(
        None,
        alias="featureDefinition",
        description="Definition of the feature")
    feature_explanation: Optional[StrictStr] = Field(
        None,
        alias="featureExplanation",
        description="Detailed explanation of the feature")
    peer_display_name: Optional[StrictStr] = Field(
        None,
        alias="peerDisplayName",
        description="outlier's peer identity display name")
    peer_identity_id: Optional[StrictStr] = Field(
        None, alias="peerIdentityId", description="outlier's peer identity id")
    access_item_reference: Optional[Dict[str, Any]] = Field(
        None, alias="accessItemReference", description="Access Item reference")
    __properties = [
        "contributingFeatureName", "identityOutlierDisplayName",
        "outlierFeatureDisplayValues", "featureDefinition",
        "featureExplanation", "peerDisplayName", "peerIdentityId",
        "accessItemReference"
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
    def from_json(cls, json_str: str) -> OutlierFeatureSummary:
        """Create an instance of OutlierFeatureSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in outlier_feature_display_values (list)
        _items = []
        if self.outlier_feature_display_values:
            for _item in self.outlier_feature_display_values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['outlierFeatureDisplayValues'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OutlierFeatureSummary:
        """Create an instance of OutlierFeatureSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OutlierFeatureSummary.parse_obj(obj)

        _obj = OutlierFeatureSummary.parse_obj({
            "contributing_feature_name":
            obj.get("contributingFeatureName"),
            "identity_outlier_display_name":
            obj.get("identityOutlierDisplayName"),
            "outlier_feature_display_values": [
                OutlierFeatureSummaryOutlierFeatureDisplayValuesInner.
                from_dict(_item)
                for _item in obj.get("outlierFeatureDisplayValues")
            ] if obj.get("outlierFeatureDisplayValues") is not None else None,
            "feature_definition":
            obj.get("featureDefinition"),
            "feature_explanation":
            obj.get("featureExplanation"),
            "peer_display_name":
            obj.get("peerDisplayName"),
            "peer_identity_id":
            obj.get("peerIdentityId"),
            "access_item_reference":
            obj.get("accessItemReference")
        })
        return _obj
