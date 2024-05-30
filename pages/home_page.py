from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_search_page(self):
        self.page.locator("a[aria-label='Search']").click()