from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    """page.goto("https://demo.automationtesting.in/Index.html")"""
    # CSS Selector 3-way-> id-#, class-., attribute-tagname[attribute='value']
    # Id using
    """email_txt_box = page.wait_for_selector("#email")
    email_txt_box.type("test@gmail.com")
    login_btn = page.wait_for_selector("#enterimg")
    login_btn.click()"""
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # attribute->tagname[attribute='value']
    username = page.wait_for_selector("input[name='username']")
    username.type("Admin")
    password = page.wait_for_selector("input[type='password']")
    password.type("admin123")
    
    login_btn = page.wait_for_selector("button[type='submit']")
    login_btn.click()
    page.wait_for_timeout(4000)