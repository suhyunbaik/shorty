from config import config_by_name


def test_test_config(app):
    test_config = config_by_name['test']
    app.config.from_object(test_config)
    assert app.config['DEBUG']
    assert app.config['TESTING']


def test_ping(app):
    client = app.test_client()
    res = client.get('/ping')
    assert res.status_code == 200
    assert res.json == {'ok': 'ok'}


