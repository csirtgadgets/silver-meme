import pytest
from csirtg_indicator.format.bind import get_lines
from csirtg_indicator import Indicator
from pprint import pprint
import re

@pytest.fixture
def indicator():
    i = {
        'indicator': "example.com",
        'provider': "me.com",
        'tlp': "amber",
        'confidence': "85",
        'reported_at': '2015-01-01T00:00:00Z',
        'itype': 'fqdn'
    }
    return Indicator(**i)


def test_format_bind(indicator):
    data = [indicator]
    text = "\n".join(list(get_lines(data)))

    assert re.findall(r'^// generated by: csirtg-indicator at \S+', text)
    assert re.findall(r'\nzone "example.com" {type master; file "\S+";};', text)


if __name__ == '__main__':
    test_format_bind()