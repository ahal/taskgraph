# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
This file contains a whitelist of gecko.v2 index route job names.  The intent
of this whitelist is to raise an alarm when new jobs are added.  If those jobs
already run in Buildbot, then it's important that the generated index routes
match (and that only one of Buildbot and TaskCluster be tier-1 at any time).
If the jobs are new and never ran in Buildbot, then their job name can be added
here without any further fuss.

Once all jobs have been ported from Buildbot, this file can be removed.
"""

from __future__ import absolute_import, print_function, unicode_literals

# please keep me in lexical order
JOB_NAME_WHITELIST = set([
    'android-aarch64-opt',
    'android-api-16-debug',
    'android-api-16-gradle-opt',
    'android-api-16-old-id-opt',
    'android-api-16-opt',
    'android-checkstyle',
    'android-dependencies',
    'android-findbugs',
    'android-lint',
    'android-test',
    'android-x86-old-id-opt',
    'android-x86-opt',
    'browser-haz-debug',
    'linux-debug',
    'linux-devedition',
    'linux-devedition-nightly-repackage',
    'linux-devedition-nightly-repackage-signing',
    'linux-nightly-repackage',
    'linux-nightly-repackage-signing',
    'linux-opt',
    'linux-pgo',
    'linux-rusttests-opt',
    'linux-rusttests-debug',
    'linux64-add-on-devel',
    'linux64-artifact-opt',
    'linux64-asan-debug',
    'linux64-asan-opt',
    'linux64-asan-reporter-opt',
    'linux64-base-toolchains-debug',
    'linux64-base-toolchains-opt',
    'linux64-fuzzing-asan-opt',
    'linux64-fuzzing-debug',
    'linux64-ccov-opt',
    'linux64-clang-tidy',
    'linux64-debug',
    'linux64-devedition',
    'linux64-devedition-nightly-repackage',
    'linux64-devedition-nightly-repackage-signing',
    'linux64-jsdcov-opt',
    'linux64-nightly-repackage',
    'linux64-nightly-repackage-signing',
    'linux64-noopt-debug',
    'linux64-opt',
    'linux64-pgo',
    'linux64-rusttests-opt',
    'linux64-rusttests-debug',
    'linux64-searchfox-debug',
    'linux64-st-an-debug',
    'linux64-st-an-opt',
    'linux64-valgrind-opt',
    'linux64-dmd-opt',
    'macosx64-add-on-devel',
    'macosx64-clang-tidy',
    'macosx64-debug',
    'macosx64-nightly-repackage',
    'macosx64-nightly-repackage-signing',
    'macosx64-noopt-debug',
    'macosx64-opt',
    'macosx64-devedition-nightly-repackage',
    'macosx64-devedition-nightly-repackage-signing',
    'macosx64-st-an-debug',
    'macosx64-st-an-opt',
    'macosx64-searchfox-debug',
    'macosx64-dmd-opt',
    'shell-haz-debug',
    'sm-arm-sim-linux32-debug',
    'sm-arm64-sim-linux64-debug',
    'sm-asan-linux64-opt',
    'sm-compacting-linux64-debug',
    'sm-compacting-win32-debug',
    'sm-fuzzing-linux64',
    'sm-mozjs-sys-linux64-debug',
    'sm-msan-linux64-opt',
    'sm-nonunified-linux64-debug',
    'sm-package-linux64-opt',
    'sm-plain-linux64-opt',
    'sm-plain-win32-opt',
    'sm-plain-linux64-debug',
    'sm-plain-win32-debug',
    'sm-rootanalysis-linux64-debug',
    'sm-rust-bindings-linux64-debug',
    'sm-tsan-linux64-opt',
    'source-bugzilla-info',
    'win32-add-on-devel',
    'win32-clang-tidy',
    'win32-debug',
    'win32-devedition-nightly-repackage',
    'win32-devedition-nightly-repackage-signing',
    'win32-devedition-opt',
    'win32-nightly-repackage',
    'win32-nightly-repackage-signing',
    'win32-noopt-debug',
    'win32-opt',
    'win32-pgo',
    'win32-rusttests-opt',
    'win32-searchfox-debug',
    'win32-st-an-debug',
    'win32-st-an-opt',
    'win32-dmd-opt',
    'win64-ccov-debug',
    'win64-add-on-devel',
    'win64-clang-tidy',
    'win64-debug',
    'win64-devedition-opt',
    'win64-devedition-nightly-repackage',
    'win64-devedition-nightly-repackage-signing',
    'win64-nightly-repackage',
    'win64-nightly-repackage-signing',
    'win64-noopt-debug',
    'win64-opt',
    'win64-pgo',
    'win64-rusttests-opt',
    'win64-st-an-debug',
    'win64-st-an-opt',
    'win64-asan-debug',
    'win64-asan-opt',
    'win64-dmd-opt',
    'win32-mingw32-debug',
])

JOB_NAME_WHITELIST_ERROR = """\
The gecko-v2 job name {} is not in the whitelist in gecko_v2_whitelist.py.
If this job runs on Buildbot, please ensure that the job names match between
Buildbot and TaskCluster, then add the job name to the whitelist.  If this is a
new job, there is nothing to check -- just add the job to the whitelist.
"""
