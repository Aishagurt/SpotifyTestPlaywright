import pytest
from playwright.sync_api import sync_playwright, Page
from pages.home_page import HomePage
from pages.search_page import SearchPage
from resources.constants.ui_constants import UrlConstant
from resources.constants.common_constants import SingerName, Song


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


class TestSongAvailability:
    home_page = HomePage
    search_page = SearchPage

    @pytest.mark.parametrize("singer_name, song_name", [
        pytest.param(SingerName.DRAKE.value, Song.ONE_DANCE.value),
        # pytest.param(SingerName.THE_BEATLES.value, Song.HERE_COMES_THE_SUN.value)
    ])
    def test_check_song(self, page: Page, singer_name, song_name):
        page.goto(UrlConstant.SPOTIFY_HOME_PAGE)

        home_page = HomePage(page)
        assert home_page.is_displayed()

        home_page.go_to_search_page()

        search_page = SearchPage(page)
        assert search_page.is_displayed()

        song_text = search_page.get_song_text_by_name(search_text=singer_name, song_name=song_name)

        assert song_text.lower() == song_name.lower(), f"Wrong name for the song {song_name}"
