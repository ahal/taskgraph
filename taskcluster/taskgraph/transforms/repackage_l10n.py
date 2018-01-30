# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Transform the repackage task into an actual task description.
"""

from __future__ import absolute_import, print_function, unicode_literals

import copy

from taskgraph.transforms.base import TransformSequence

transforms = TransformSequence()


@transforms.add
def split_locales(config, jobs):
    for job in jobs:
        dep_job = job['dependent-task']
        for locale in dep_job.attributes.get('chunk_locales', []):
            locale_job = copy.deepcopy(job)  # don't overwrite dict values here
            treeherder = locale_job.setdefault('treeherder', {})
            treeherder['symbol'] = 'L10n-Rpk({})'.format(locale)
            locale_job['locale'] = locale
            yield locale_job
