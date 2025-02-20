from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils


class AvdFacts:
    def __init__(self, hostvars: dict, shared_utils: SharedUtils):
        self._hostvars = hostvars
        self.shared_utils = shared_utils

    @classmethod
    def __keys(cls):  # pylint: disable=bad-option-value, unused-private-member # CH Sep-22: Some pylint bug.
        """
        Get all class attributes including those of base Classes and Mixins.
        Using MRO, which is the same way Python resolves attributes.
        """
        keys = []
        for c in cls.mro():
            c_keys = [key for key in c.__dict__ if key not in keys]
            keys.extend(c_keys)

        return keys

    @classmethod
    def keys(cls):
        """
        Return the list of "keys"

        Actually the returned list are the names of attributes not starting with "_" and using cached_property class.
        The "_" check is added to allow support for "internal" cached_properties storing temporary values.
        """

        return [key for key in cls.__keys() if not key.startswith("_") and isinstance(getattr(cls, key), cached_property)]

    @classmethod
    def internal_keys(cls):
        """
        Return a list containing the names of attributes starting with "_" and using cached_property class.
        """

        return [key for key in cls.__keys() if key.startswith("_") and isinstance(getattr(cls, key), cached_property)]

    def get(self, key, default_value=None):
        """
        Emulate the builtin dict .get method
        """

        if key in self.keys():
            return getattr(self, key)
        return default_value

    def render(self):
        """
        Return a dictionary of all @cached_property values.

        If the value is cached, it will automatically get returned from cache
        If the value is not cached, it will be resolved by the attribute function first.
        Empty values are removed from the returned data.
        """
        return {key: getattr(self, key) for key in self.keys() if getattr(self, key) is not None}

    def clear_cache(self):
        for key in self.keys() + self.internal_keys():
            self.__dict__.pop(key, None)
