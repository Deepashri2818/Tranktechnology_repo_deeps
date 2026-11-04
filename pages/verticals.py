class vertical:
    def __init__(self, page):
        self.page = page
        #verticals locaters
        #  ========== Header: Verticals tab menu ==========
        self.verticals_tab = page.locator('//li[@class="drop_down"][1]')  # Main “Verticals” dropdown
        
        #Trading Menu in Verticals tab
        self.vertical_trading_menu = page.locator('//li[@data-id="trading"]')  # Trading submenu
        
        # Trading submenu link         
        self.stock_trading =  page.locator('(//li/a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.algo_trading  = page.locator('(//li/a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.paper_trading = page.locator('(//li/a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.cust_trading  = page.locator('(//li/a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.cfd_trading  = page.locator('(//li/a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.webportal_trading  = page.locator('(//li/a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.mass_trading  = page.locator('(//li/a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        
        self.trading_option_list = [self.stock_trading, self.algo_trading, self.paper_trading,  self.cust_trading, self.cfd_trading, self.webportal_trading, self.mass_trading]
        
        ################################################################################################################################
        
        #Retail and Ecommerce Menu in Verticals tab
        self.verticals_retail_ecommerce_menu = page.locator('//li[@data-id="retailEcommerce"]')  # Retail & eCommerce submenu

        # Retail & eCommerce submenu links
        self.ecommerce_app_development = page.locator('(//li/a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.ecommerce_web_development_vertical = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        
        self.retail_ecommerce_menu_option_list = [self.ecommerce_app_development, self.ecommerce_web_development_vertical  ]
        
        ################################################################################################################################
         #Fintect Menu in Verticals tab
         
        self.verticals_fintech_menu = page.locator('//li[@data-id="fintech"]')  # Fintech submenu
        
        # Fintech submenu links
        self.pos_software_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]'
        )
        self.cryptocurrency_mobile_app_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]'
        )
        
        self.Fintech_menu_option_list = [self.pos_software_development, self.cryptocurrency_mobile_app_development]
        
        ################################################################################################################################
         #Healthcare Menu in Verticals tab
         
        self.verticals_healthcare_menu = page.locator('//li[@data-id="healthcare"]')  # Healthcare submenu
        
        # Healthcare submenu links
        self.diet_and_nutrition_app = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]'
        )
        self.health_tracking_app = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]'
        )
        
        self.healthcare_menu_option_list = [self.diet_and_nutrition_app,  self.health_tracking_app ]
        
        ################################################################################################################################
        
        #CustomAPP Menu in Verticals tab
        
        self.verticals_custom_app_menu = page.locator('//li[@data-id="customApp"]')  # Custom App submenu
        
        # Custom App submenu links
        self.desktop_application_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]'
        )
        self.custom_crm_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]'
        )
        self.hrm_application_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]'
        )
        self.erp_app_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]'
        )
        self.travel_mobile_app_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]'
        )
        self.elearning_mobile_app_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]'
        )
        self.dating_app_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]'
        )
        self.real_estate_mobile_app_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]'
        )
        self.usa_custom_crm_development = page.locator(
            '(//li/a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]'
        )
        
        self.custom_app_menu_option_list = [self.desktop_application_development, self.custom_crm_development , self.custom_crm_development, self.erp_app_development,
                                            self.travel_mobile_app_development, self.elearning_mobile_app_development, 
                                            self.dating_app_development, self.real_estate_mobile_app_development, self.usa_custom_crm_development  ]



    def trading_menu_options(self):        
        for i in self.trading_option_list:
            self.verticals_tab.hover()
            self.vertical_trading_menu.hover()
            i.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    
    def retail_ecommerce_menu_option(self):        
        for i in self.retail_ecommerce_menu_option_list:
            self.verticals_tab.hover()
            self.verticals_retail_ecommerce_menu.hover()
            i.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()       
            
    
    def fintech_menu_options(self):
        for i in self.Fintech_menu_option_list:
            self.verticals_tab.hover()
            self.verticals_fintech_menu.hover()
            i.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()    
    
    def healthcare_menu_option(self):        
                for i in self.healthcare_menu_option_list:
                    self.verticals_tab.hover()
                    self.verticals_healthcare_menu.hover()
                    i.hover()
                    i.click()
                    self.page.wait_for_load_state("load")
                    self.page.go_back()           
                    
    def custom_app_menu_option(self):        
                for i in self.custom_app_menu_option_list:
                    self.verticals_tab.hover()
                    self.verticals_custom_app_menu.hover()
                    i.hover()
                    i.click()
                    self.page.wait_for_load_state("load")     
                    self.page.wait_for_timeout(2000)              
                    self.page.go_back()           
                
