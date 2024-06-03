import urllib.parse

from playwright.async_api import Page


class SearchPage:
    TRACK_NAME_LABEL_LOCATOR_FORMAT = "//*[contains(@href, '/track/') and .//*[contains(text(), '%s')]]"
    SEARCH_TRACKS_BUTTON_LOCATOR_FORMAT = "a[href='/search/%s/tracks']"

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("form[role='search'] input")

    def get_song_text_by_name(self, search_text: str, song_name: str):
        self.search_input.fill(search_text)
        self.search_input.press("Enter")

        search_track_button = self._get_search_track_button(search_text)
        search_track_button.click()

        track_name_label = self._get_track_name_label(song_name)
        return track_name_label.text_content()

    def _get_search_track_button(self, search_text: str):
        search_track_button_locator = self.SEARCH_TRACKS_BUTTON_LOCATOR_FORMAT % urllib.parse.quote(search_text)
        return self.page.locator(search_track_button_locator)

    def _get_track_name_label(self, song_name: str):
        track_name_label_locator = self.TRACK_NAME_LABEL_LOCATOR_FORMAT % song_name
        return self.page.locator(track_name_label_locator)
