from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.redbus.in/")
    my_cookies = page.context.cookies()
    print(my_cookies)
    
    # Clear the cookies
    page.context.clear_cookies()
    
    #Add a new cookie
    """new_cookies = {
        "name": "akib",
        "uid": "23lksdj322432"
    }
    page.context.add_cookies([new_cookies])"""
    print(page.context.cookies())
    
    page.screenshot(path="redbus.png", full_page=True)