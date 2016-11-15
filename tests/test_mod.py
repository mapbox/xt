import xt
import pytest

def test_format_hash():
    x = 10
    y = 100
    z = 1000
    delimiter = 'poo'

    assert xt.format_hash(x, y, z, delimiter) == '1000poo10poo100'


def test_parsetile_slash():
    instring = 'junk/junk/junk/junk/13/255/300.junk'

    assert xt.parsetile(instring) == '[255, 300, 13]'


def test_parsetile_dash():
    instring = 'junk-junk-junk-junk-13-255-300.junk'

    assert xt.parsetile(instring) == '[255, 300, 13]'


def test_parsetile_mix():
    instring = 'junk/junk-junk/junk/13-255-300.junk'

    assert xt.parsetile(instring) == '[255, 300, 13]'


def test_parsetile_parse_last_dash():
    instring = 'junk 100-100-100 13-255-300.junk'

    assert xt.parsetile(instring) == '[255, 300, 13]'


def test_parsetile_parse_last_slash():
    instring = 'junk 100-100-100 13/255/300.junk'

    assert xt.parsetile(instring) == '[255, 300, 13]'


def test_parsetile_mercantileish():
    instring = '[255, 300, 13]'
    assert xt.parsetile(instring) == '13/255/300'


def test_parsetile_mercantileish_dash():
    instring = '[255, 300, 13]'
    assert xt.parsetile(instring, '-') == '13-255-300'


def test_parsetile_mercantileish_roundtrip():
    instring = '[255, 300, 13]'
    assert xt.parsetile(xt.parsetile(instring)) == instring


def test_parsetile_nomatch():
    instring = 'fail-obvi-100-100.junk'

    with pytest.raises(ValueError):
        xt.parsetile(instring)
