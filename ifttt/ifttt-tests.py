# -*- coding: utf-8 -*-
"""
  Wikipedia channel for IFTTT
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Copyright 2015 Ori Livneh <ori@wikimedia.org>
                 Stephen LaPorte <stephen.laporte@gmail.com>
                 Alangi Derick <alangiderick@gmail.com>

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

"""

from triggers import *

import requests, unittest

class AotdTestCase(unittest.TestCase):
  """Test class for Article of the Day trigger"""

  def test_aotd_trigger_with_get(self):
    """Test suite for Article of the Day trigger which checks for 
    proper respone code after the GET request"""

    # response = requests.get('http://localhost:5000/v1/triggers/article_of_the_day?lang=en')
    # self.assertEquals(response.status_code, 200)
    pass