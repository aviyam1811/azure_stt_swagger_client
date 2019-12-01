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


class IReadOnlyDictionary2(object):
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
        '_none': 'list[str]',
        'language': 'list[str]',
        'acoustic': 'list[str]',
        'pronunciation': 'list[str]',
        'custom_voice': 'list[str]',
        'audio_files': 'list[str]',
        'keyword': 'list[str]'
    }

    attribute_map = {
        '_none': 'None',
        'language': 'Language',
        'acoustic': 'Acoustic',
        'pronunciation': 'Pronunciation',
        'custom_voice': 'CustomVoice',
        'audio_files': 'AudioFiles',
        'keyword': 'Keyword'
    }

    def __init__(self, _none=None, language=None, acoustic=None, pronunciation=None, custom_voice=None, audio_files=None, keyword=None):  # noqa: E501
        """IReadOnlyDictionary2 - a model defined in Swagger"""  # noqa: E501

        self.__none = None
        self._language = None
        self._acoustic = None
        self._pronunciation = None
        self._custom_voice = None
        self._audio_files = None
        self._keyword = None
        self.discriminator = None

        if _none is not None:
            self._none = _none
        if language is not None:
            self.language = language
        if acoustic is not None:
            self.acoustic = acoustic
        if pronunciation is not None:
            self.pronunciation = pronunciation
        if custom_voice is not None:
            self.custom_voice = custom_voice
        if audio_files is not None:
            self.audio_files = audio_files
        if keyword is not None:
            self.keyword = keyword

    @property
    def _none(self):
        """Gets the _none of this IReadOnlyDictionary2.  # noqa: E501


        :return: The _none of this IReadOnlyDictionary2.  # noqa: E501
        :rtype: list[str]
        """
        return self.__none

    @_none.setter
    def _none(self, _none):
        """Sets the _none of this IReadOnlyDictionary2.


        :param _none: The _none of this IReadOnlyDictionary2.  # noqa: E501
        :type: list[str]
        """

        self.__none = _none

    @property
    def language(self):
        """Gets the language of this IReadOnlyDictionary2.  # noqa: E501


        :return: The language of this IReadOnlyDictionary2.  # noqa: E501
        :rtype: list[str]
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this IReadOnlyDictionary2.


        :param language: The language of this IReadOnlyDictionary2.  # noqa: E501
        :type: list[str]
        """

        self._language = language

    @property
    def acoustic(self):
        """Gets the acoustic of this IReadOnlyDictionary2.  # noqa: E501


        :return: The acoustic of this IReadOnlyDictionary2.  # noqa: E501
        :rtype: list[str]
        """
        return self._acoustic

    @acoustic.setter
    def acoustic(self, acoustic):
        """Sets the acoustic of this IReadOnlyDictionary2.


        :param acoustic: The acoustic of this IReadOnlyDictionary2.  # noqa: E501
        :type: list[str]
        """

        self._acoustic = acoustic

    @property
    def pronunciation(self):
        """Gets the pronunciation of this IReadOnlyDictionary2.  # noqa: E501


        :return: The pronunciation of this IReadOnlyDictionary2.  # noqa: E501
        :rtype: list[str]
        """
        return self._pronunciation

    @pronunciation.setter
    def pronunciation(self, pronunciation):
        """Sets the pronunciation of this IReadOnlyDictionary2.


        :param pronunciation: The pronunciation of this IReadOnlyDictionary2.  # noqa: E501
        :type: list[str]
        """

        self._pronunciation = pronunciation

    @property
    def custom_voice(self):
        """Gets the custom_voice of this IReadOnlyDictionary2.  # noqa: E501


        :return: The custom_voice of this IReadOnlyDictionary2.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_voice

    @custom_voice.setter
    def custom_voice(self, custom_voice):
        """Sets the custom_voice of this IReadOnlyDictionary2.


        :param custom_voice: The custom_voice of this IReadOnlyDictionary2.  # noqa: E501
        :type: list[str]
        """

        self._custom_voice = custom_voice

    @property
    def audio_files(self):
        """Gets the audio_files of this IReadOnlyDictionary2.  # noqa: E501


        :return: The audio_files of this IReadOnlyDictionary2.  # noqa: E501
        :rtype: list[str]
        """
        return self._audio_files

    @audio_files.setter
    def audio_files(self, audio_files):
        """Sets the audio_files of this IReadOnlyDictionary2.


        :param audio_files: The audio_files of this IReadOnlyDictionary2.  # noqa: E501
        :type: list[str]
        """

        self._audio_files = audio_files

    @property
    def keyword(self):
        """Gets the keyword of this IReadOnlyDictionary2.  # noqa: E501


        :return: The keyword of this IReadOnlyDictionary2.  # noqa: E501
        :rtype: list[str]
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this IReadOnlyDictionary2.


        :param keyword: The keyword of this IReadOnlyDictionary2.  # noqa: E501
        :type: list[str]
        """

        self._keyword = keyword

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
        if issubclass(IReadOnlyDictionary2, dict):
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
        if not isinstance(other, IReadOnlyDictionary2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
