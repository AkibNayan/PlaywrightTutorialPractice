from playwright.sync_api import sync_playwright
text_alert = []

def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")
    
    page.wait_for_selector('//a[@href="#Textbox"]').click()
    page.wait_for_timeout(1000)
    
    #page.on('dialog', lambda dialog : dialog.accept())
    #page.on('dialog', lambda dialog : dialog.dismiss())
    #page.on('dialog', lambda dialog : dialog.message)
    page.on('dialog', handle_dialog)
    page.wait_for_selector('//div[@id="Textbox"]/button').click()
    page.wait_for_timeout(3000)
    
    print(text_alert)
    
    browser.close()