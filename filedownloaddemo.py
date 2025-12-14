from playwright.sync_api import sync_playwright

def download_handle(download):
    location_file = "sample_file.zip"
    download.save_as(location_file)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/FileDownload.html')
    page.on("download", download_handle)
    page.wait_for_selector('//a[@type="button"]').click()
    
    
    page.wait_for_timeout(3000)
    browser.close()