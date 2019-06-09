import pytest
from mock import patch

from src.mid_piano import main

@patch('src.mid_piano')
def test_setup_test(mid_piano):
    mid_piano.main()
    assert mid_piano.main.called 
