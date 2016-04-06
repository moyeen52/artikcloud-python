# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class RuleCreationInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RuleCreationInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'enabled': 'bool',
            'name': 'str',
            'rule': 'dict(str, object)'
        }

        self.attribute_map = {
            'description': 'description',
            'enabled': 'enabled',
            'name': 'name',
            'rule': 'rule'
        }

        self._description = None
        self._enabled = None
        self._name = None
        self._rule = None

    @property
    def description(self):
        """
        Gets the description of this RuleCreationInfo.
        Description

        :return: The description of this RuleCreationInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RuleCreationInfo.
        Description

        :param description: The description of this RuleCreationInfo.
        :type: str
        """
        self._description = description

    @property
    def enabled(self):
        """
        Gets the enabled of this RuleCreationInfo.
        Is Enabled

        :return: The enabled of this RuleCreationInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this RuleCreationInfo.
        Is Enabled

        :param enabled: The enabled of this RuleCreationInfo.
        :type: bool
        """
        self._enabled = enabled

    @property
    def name(self):
        """
        Gets the name of this RuleCreationInfo.
        Name

        :return: The name of this RuleCreationInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RuleCreationInfo.
        Name

        :param name: The name of this RuleCreationInfo.
        :type: str
        """
        self._name = name

    @property
    def rule(self):
        """
        Gets the rule of this RuleCreationInfo.
        Rule

        :return: The rule of this RuleCreationInfo.
        :rtype: dict(str, object)
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """
        Sets the rule of this RuleCreationInfo.
        Rule

        :param rule: The rule of this RuleCreationInfo.
        :type: dict(str, object)
        """
        self._rule = rule

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

