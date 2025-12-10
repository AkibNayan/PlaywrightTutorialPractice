from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.automationtesting.in/Selectable.html")
    # Mouse Actions
    # Action as Hover
    page.wait_for_selector('//a[contains(text(), "SwitchTo")]').hover()
    # Action as Click
    page.wait_for_selector('//a[contains(text(), "SwitchTo")]').click()
    # Action as Double Click
    page.wait_for_selector('//a[contains(text(), "SwitchTo")]').dblclick()
    # Action as right click
    page.wait_for_selector('//a[contains(text(), "SwitchTo")]').click(button="right")
    # Action as shift click
    page.wait_for_selector('//a[contains(text(), "SwitchTo")]').click(modifiers=["Shift"])
    
    # Keyboard Actions
    # Action as press
    page.wait_for_selector('//a[contains(text(), "SwitchTo")]').press("A")
    # A-z, 0-9, Special Char, ArrowRight, ArrowDown, PageUp, PageDown, Enter, Escape, Space, Tab, Shift, Ctrl, Alt, Meta
    page.wait_for_selector('//a[contains(text(), "SwitchTo")]').press("$")
    
    page.wait_for_timeout(2000)
    
    browser.close()