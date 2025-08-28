from twttr import shorten
import pytest

def test_shorten():
    #testing >>> tstng
    assert shorten("testing") == "tstng"
    #this is my tweet! >>>>ths s my twt!
    assert shorten("this is my tweet!") == "ths s my twt!"
    #UPPERCASE
    assert shorten("UPPERCASE") == "PPRCS"
    #s0mth1ng
    assert shorten("s0mth1ng") == "s0mth1ng"
