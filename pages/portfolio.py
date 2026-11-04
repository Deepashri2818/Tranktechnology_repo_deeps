class portfolioclass:
    def __init__(self, page):
        self.page = page      
        
        self.portfoliotab = page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]') 
        self.ics_hw = page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wing_pharma = page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arena_animation = page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home360 = page.locator('//a[@href="https://home360stores.com/"]')
        #self.club_meetings = page.locator("(//div[@class='cm-content'])[5]/a[text()='View More']")
        self.cords_cables = page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')
        
        self.portfolio_tabs_list = [ self.ics_hw, self.wing_pharma , self.arena_animation, self.home360,   self.cords_cables ]
    
    def new_windows_portfolio_tabs(self):
        self.portfoliotab.click()
        self.page.wait_for_load_state(state="load")
                   
        for portfoliolinks in self.portfolio_tabs_list:  
            with self.page.context.expect_page() as new_page_info:
                portfoliolinks.click()
                
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()  
                    #OR
                    # self.portfolio.click()
                    # i.click()
                    # self.page.wait_for_load_state("load")
                    # self.page.wait_for_timeout(5000)
                    # self.page.bring_to_front() # Switch  to main tab
                    # self.page.wait_for_timeout(5000)
                    #or
                    # with self.page.expect_popup() as popup:
                    #     self.portfolio.click()    
                    #     i.click()
                    #     new_tab = popup.value
                    #     new_tab.wait_for_load_state("domcontentloaded")
                    #     self.page.wait_for_timeout(2000)
                    #     new_tab.close()