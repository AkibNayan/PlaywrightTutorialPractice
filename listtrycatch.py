from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Selectable.html")
        # Store multiple elements in a list
        """elements = page.query_selector_all("b")
        print(len(elements))
        for element in elements:
            print(element.text_content())"""
        
        links = page.query_selector_all("a")
        print(len(links))
        for link in links:
            print(link.get_attribute('href'))
        
        # Wrong XPath
        page.query_selector('//h4/a').click()
        
        page.wait_for_timeout(2000)
        browser.close()
    except Exception as e:
        print(str(e))
    finally:
        print("Executed")