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

from typing import Optional
from pydantic import BaseModel, Field
from v3.models.aggregations import Aggregations
from v3.models.bucket_aggregation import BucketAggregation
from v3.models.filter_aggregation import FilterAggregation
from v3.models.metric_aggregation import MetricAggregation
from v3.models.nested_aggregation import NestedAggregation


class SubSearchAggregationSpecification(BaseModel):
    """
    SubSearchAggregationSpecification
    """
    nested: Optional[NestedAggregation] = None
    metric: Optional[MetricAggregation] = None
    filter: Optional[FilterAggregation] = None
    bucket: Optional[BucketAggregation] = None
    sub_aggregation: Optional[Aggregations] = Field(None,
                                                    alias="subAggregation")
    __properties = ["nested", "metric", "filter", "bucket", "subAggregation"]

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
    def from_json(cls, json_str: str) -> SubSearchAggregationSpecification:
        """Create an instance of SubSearchAggregationSpecification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of nested
        if self.nested:
            _dict['nested'] = self.nested.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric
        if self.metric:
            _dict['metric'] = self.metric.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bucket
        if self.bucket:
            _dict['bucket'] = self.bucket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_aggregation
        if self.sub_aggregation:
            _dict['subAggregation'] = self.sub_aggregation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubSearchAggregationSpecification:
        """Create an instance of SubSearchAggregationSpecification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubSearchAggregationSpecification.parse_obj(obj)

        _obj = SubSearchAggregationSpecification.parse_obj({
            "nested":
            NestedAggregation.from_dict(obj.get("nested"))
            if obj.get("nested") is not None else None,
            "metric":
            MetricAggregation.from_dict(obj.get("metric"))
            if obj.get("metric") is not None else None,
            "filter":
            FilterAggregation.from_dict(obj.get("filter"))
            if obj.get("filter") is not None else None,
            "bucket":
            BucketAggregation.from_dict(obj.get("bucket"))
            if obj.get("bucket") is not None else None,
            "sub_aggregation":
            Aggregations.from_dict(obj.get("subAggregation"))
            if obj.get("subAggregation") is not None else None
        })
        return _obj
