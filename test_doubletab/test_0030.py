import pytest

from sf_setup_helper.base_pytest import Base
from sf_setup_helper.base_helper import BaseHelper


@pytest.mark.webtest
class TestID0030(Base, BaseHelper):
    """
        @TestCase: 0030 (1)
        @Author: Iryna Vaskiv
        Description:
            1. Check if new tab open when user click with "open in new tab".
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click shafa.ua site
            2. Select block items inside main page
            3. Click "open"
        Expected result:
            1. New tab should print correct information.
    """

    # def test_if_possible_open_new_tab(self):
        

