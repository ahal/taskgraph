# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import, print_function, unicode_literals

import attr

from ..parameters import Parameters
from ..config import GraphConfig


@attr.s(frozen=True)
class TransformConfig(object):
    """
    A container for configuration affecting transforms.  The `config` argument
    to transforms is an instance of this class.
    """

    # the name of the current kind
    kind = attr.ib()

    # the path to the kind configuration directory
    path = attr.ib(type=basestring)

    # the parsed contents of kind.yml
    config = attr.ib(type=dict)

    # the parameters for this task-graph generation run
    params = attr.ib(type=Parameters)

    # a list of all the tasks associated with the kind dependencies of the
    # current kind
    kind_dependencies_tasks = attr.ib()

    # Global configuration of the taskgraph
    graph_config = attr.ib(type=GraphConfig)


@attr.s()
class TransformSequence(object):
    """
    Container for a sequence of transforms.  Each transform is represented as a
    callable taking (config, items) and returning a generator which will yield
    transformed items.  The resulting sequence has the same interface.

    This is convenient to use in a file full of transforms, as it provides a
    decorator, @transforms.add, that will add the decorated function to the
    sequence.
    """

    _transforms = attr.ib(factory=list)

    def __call__(self, config, items):
        for xform in self._transforms:
            items = xform(config, items)
            if items is None:
                raise Exception("Transform {} is not a generator".format(xform))
        return items

    def add(self, func):
        self._transforms.append(func)
        return func
