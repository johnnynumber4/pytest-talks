def test_config_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://my-qaenv.com'
    assert port == 8080

def test_config_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://my-devenv.com'
    assert port == 80

