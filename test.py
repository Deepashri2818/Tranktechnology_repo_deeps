from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #browser = p.chromium.launch(headless=False)
    #page = browser.new_page()
    # 1. Launch with the maximize argument
    browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        
    # 2. Force the context to bypass the default 1280x720 viewport
    context = browser.new_context(no_viewport=True)
        
    # 3. Create your page and navigate
    page = context.new_page()
    
    
    page.goto("https://www.tranktechnologies.com")