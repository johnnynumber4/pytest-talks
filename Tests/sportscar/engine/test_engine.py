from pytest import mark


@mark.smoke
@mark.engine
@mark.skip(reason="This is a stupid test")
def test_engine_functions_as_expected(browser):
    browser.get('www.google.com')
    assert False