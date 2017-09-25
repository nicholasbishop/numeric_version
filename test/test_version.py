#!/usr/bin/env python

# Copyright 2017 Neverware Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=missing-docstring

import unittest

from numeric_version import NumericVersion

class TestVersion(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(NumericVersion.parse('1.2.3'),
                         NumericVersion(1, 2, 3))

    def test_string(self):
        self.assertEqual(str(NumericVersion(1, 2, 3)), '1.2.3')

    def test_eq(self):
        self.assertEqual(NumericVersion(1, 2, 3),
                         NumericVersion(1, 2, 3))
        self.assertNotEqual(NumericVersion(1, 2, 3),
                            NumericVersion(1, 2, 4))

    def test_lt(self):
        self.assertLess(NumericVersion(1, 2, 3),
                        NumericVersion(1, 2, 4))
        self.assertLess(NumericVersion(1, 1, 3),
                        NumericVersion(1, 2, 2))
        self.assertLess(NumericVersion(0, 2, 3),
                        NumericVersion(1, 2, 2))

    def test_gt(self):
        self.assertGreater(NumericVersion(2, 1, 0),
                           NumericVersion(1, 2, 3))

    def test_len(self):
        self.assertEqual(len(NumericVersion(1, 1, 1)), 3)


if __name__ == '__main__':
    unittest.main()
