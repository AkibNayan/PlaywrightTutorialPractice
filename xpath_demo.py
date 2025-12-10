from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Relative Xpath -> //tagname[@attribute='value']
    
    """username = page.wait_for_selector('//input[@name="username"]')
    username.type("Admin")
    password = page.wait_for_selector('//input[@placeholder="Password"]')
    password.type("admin123")
    login_btn = page.wait_for_selector('//button[@type="submit"]')
    login_btn.click()"""
    
    # text() -> //tagname[text()='text]
    """page.wait_for_selector('//p[text()="Forgot your password? "]').click()"""
    
    # Dynamic Xpath
    # contains -> //tagname[contains(@attribute,'value')]
    
    """username = page.wait_for_selector('//input[contains(@placeholder,"User")]')"""
    
    # akib123, akib323, akib352
    """starts-with -> //tagname[starts-with(@attribute,'value')]"""
    # 213user, 343user, 456user
    """ends-with -> //tagname[ends-with(@attribute, 'value')]"""
    
    # family
    """parent -> //tagname[@attribute='value']/parent::tagname"""
    """child -> //tagname[@attribute='value']/child::tagname"""
    """ancestor"""
    """sibling -> //td[text(), 'Microsoft']/following-sibling::td[2]"""
    
    page.wait_for_timeout(4000)
    browser.close()