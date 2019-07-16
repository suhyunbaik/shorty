import os
import json
import pytest
from short.models import URLS


def read_input_set(fname):
    with open('{}/inputcase/{}.json'.format(os.path.dirname(os.path.realpath(__file__)), fname), 'r') as file:
        return json.load(file)


def read_output_set(fname):
    with open('{}/outputcase/{}.json'.format(os.path.dirname(os.path.realpath(__file__)), fname), 'r') as file:
        return json.load(file)


@pytest.fixture(scope='function')
def url_with_name(session):
    url = URLS(original_url='www.google.com', short_url='go')
    session.add(url)
    return url


@pytest.fixture(scope='function')
def url(session):
    urls = URLS(original_url='https://kr.linkedin.com/in/hyoungnae',
                short_url='cto')
    session.add(urls)
    session.commit()
    yield
    session.query(URLS).delete()
    session.commit()


def test_get_emtpy_url_list(client):
    response = client.get('/urls')
    assert response.status_code == 200
    assert response.json == {'urls': []}


def test_create_short_url_with_missing_required_parameter(client):
    response = client.post('/urls', json=dict(name='bar'))
    assert response.status_code == 422
    assert response.json == {'msg': 'url is missing'}


def test_create_short_url(client):
    input_set = read_input_set('short_url_with_no_name')
    response = client.post('/urls', json=dict(url=input_set['original_url']))
    assert response.status_code == 200
    output_set = read_output_set('short_url_with_no_name')
    assert response.json == output_set


def test_create_short_url_with_desired_name(client):
    input_set = read_input_set('short_url_with_name')
    response = client.post('/urls', json=dict(url=input_set['url'], name=input_set['name']))
    assert response.status_code == 200
    output_set = read_output_set('short_url_with_name')
    assert response.json == output_set


def test_get_url_list(client, url):
    response = client.get('/urls')
    assert response.status_code == 200

