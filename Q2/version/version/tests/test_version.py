import pytest

try:
    from version.version import Version
except:
    Version = None


@pytest.mark.skipif(Version is None, reason= 'Version is not available')
def test_superior():
    assert Version('1.2.1') > Version('1.2.01')
    assert Version('1.2.01') > Version('1.1.01')
    assert Version('1.2.3') > Version('0')


@pytest.mark.skipif(Version is None, reason= 'Version is not available')
def test_inferior():
    assert Version('1.1.01') < Version('1.2.01')
    assert Version('1.1.01') < Version('2.1.01')
    assert Version('0') < Version('1.2.3')


@pytest.mark.skipif(Version is None, reason= 'Version is not available')
def test_equal():
    assert Version('1.2.00') == Version('1.2.0')
    assert Version('1.2') == Version('1.2')


@pytest.mark.skipif(Version is None, reason= 'Version is not available')
def test_inferior_or_equal():
    assert Version('1.2.00') <= Version('1.2.0')
    assert Version('1.1.00') <= Version('1.2.0')
    assert Version('1.1') <= Version('1.2.0')


@pytest.mark.skipif(Version is None, reason= 'Version is not available')
def test_superior_or_equal():
    assert Version('1.2.00') >= Version('1.2.0')
    assert Version('1.2.0') >= Version('1.1.00')
    assert Version('1.2.0') >= Version('1.1')