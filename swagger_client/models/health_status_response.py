# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HealthStatusResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'str',
        'message': 'str',
        'components': 'list[Component]'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'components': 'components'
    }

    def __init__(self, status=None, message=None, components=None):  # noqa: E501
        """HealthStatusResponse - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._message = None
        self._components = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if components is not None:
            self.components = components

    @property
    def status(self):
        """Gets the status of this HealthStatusResponse.  # noqa: E501


        :return: The status of this HealthStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HealthStatusResponse.


        :param status: The status of this HealthStatusResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Healthy", "Sick", "Error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self):
        """Gets the message of this HealthStatusResponse.  # noqa: E501


        :return: The message of this HealthStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this HealthStatusResponse.


        :param message: The message of this HealthStatusResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def components(self):
        """Gets the components of this HealthStatusResponse.  # noqa: E501


        :return: The components of this HealthStatusResponse.  # noqa: E501
        :rtype: list[Component]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this HealthStatusResponse.


        :param components: The components of this HealthStatusResponse.  # noqa: E501
        :type: list[Component]
        """

        self._components = components

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(HealthStatusResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HealthStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
