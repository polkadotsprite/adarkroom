from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Desktop
        page = browser.new_page()
        page.goto("http://localhost:8080")
        page.wait_for_selector("text=light fire")
        # Wait for fade-in animations to complete
        page.wait_for_timeout(2000)
        page.screenshot(path="verification/desktop_preview.png")

        # Mobile
        page_mobile = browser.new_page(viewport={"width": 375, "height": 667})
        page_mobile.goto("http://localhost:8080")
        page_mobile.wait_for_selector("text=light fire")
        # Wait for fade-in animations to complete
        page_mobile.wait_for_timeout(2000)
        page_mobile.screenshot(path="verification/mobile_preview.png")

        browser.close()

if __name__ == "__main__":
    run()
