import pytest
from selene import be, have
from selene.support.shared import browser


@pytest.fixture
def browser_window(scope='function'):
    browser.config.window_width = 1280
    browser.config.window_height = 720
    yield
    browser.close()


def test_find_true():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_find_false():
    type_text = 'dfbdsjfbdjbdsbdshfdshfbdhsfbhdf'
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(type_text).press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
