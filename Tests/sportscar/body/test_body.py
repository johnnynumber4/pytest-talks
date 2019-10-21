from pytest import mark


@mark.body
@mark.ui
class BodyTests:
    @mark.smoke
    def test_can_navigate_to_a_body_page(self, session_browser):
        session_browser.get('http://www.google.com/')
        assert True
