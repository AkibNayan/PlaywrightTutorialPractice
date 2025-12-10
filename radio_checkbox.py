from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    
    # Radio Button
    radio_btn = page.wait_for_selector('//input[@value="FeMale"]')
    radio_btn.click()
    #radio_btn.check()
    
    if radio_btn.is_checked():
        print("Passed")
    else:
        print("Failed")
    
    # Checkbox
    checkbox = page.query_selector('//input[@value="Cricket"]')
    #checkbox2 = page.query_selector('//input[@value="Movies"]')
    
    checkbox.check()
    #checkbox2.check()
    
    if checkbox.is_checked():
        print("Checked Cricket")
    else:
        print("Failed Cricket")
    
    page.wait_for_timeout(4000)
    browser.close()