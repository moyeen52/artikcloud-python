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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'email': 'str',
            'full_name': 'str',
            'sa_identity': 'str',
            'created_on': 'int',
            'modified_on': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'email': 'email',
            'full_name': 'fullName',
            'sa_identity': 'saIdentity',
            'created_on': 'createdOn',
            'modified_on': 'modifiedOn'
        }

        self._id = None
        self._name = None
        self._email = None
        self._full_name = None
        self._sa_identity = None
        self._created_on = None
        self._modified_on = None

    @property
    def id(self):
        """
        Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.


        :param id: The id of this User.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.


        :param name: The name of this User.
        :type: str
        """
        self._name = name

    @property
    def email(self):
        """
        Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.


        :param email: The email of this User.
        :type: str
        """
        self._email = email

    @property
    def full_name(self):
        """
        Gets the full_name of this User.


        :return: The full_name of this User.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this User.


        :param full_name: The full_name of this User.
        :type: str
        """
        self._full_name = full_name

    @property
    def sa_identity(self):
        """
        Gets the sa_identity of this User.


        :return: The sa_identity of this User.
        :rtype: str
        """
        return self._sa_identity

    @sa_identity.setter
    def sa_identity(self, sa_identity):
        """
        Sets the sa_identity of this User.


        :param sa_identity: The sa_identity of this User.
        :type: str
        """
        self._sa_identity = sa_identity

    @property
    def created_on(self):
        """
        Gets the created_on of this User.


        :return: The created_on of this User.
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this User.


        :param created_on: The created_on of this User.
        :type: int
        """
        self._created_on = created_on

    @property
    def modified_on(self):
        """
        Gets the modified_on of this User.


        :return: The modified_on of this User.
        :rtype: int
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """
        Sets the modified_on of this User.


        :param modified_on: The modified_on of this User.
        :type: int
        """
        self._modified_on = modified_on

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

