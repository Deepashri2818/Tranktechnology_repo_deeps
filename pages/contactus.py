class contactusclass:
    def __init__(self, page):
        self.page = page      
        
        self.contact_us_link = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')#.click()  # Contact Us page
        self.contact_name_input = page.locator('(//input[@placeholder="Your Name"])[2]')#.fill('Deepashri')  # Name field
        self.contact_email_input = page.locator('(//input[@placeholder="Your Mail"])[2]')
        #.fill('deepashri.g.joshi@gmail.com')  # Email field
       # self.send_otp_button = page.locator('//button[@class="send-otp-btn"]')#.click()  # Send OTP button
        self.otp_input = page.locator('(//input[@placeholder="Enter OTP"])[2]')#.fill('3434')  # OTP field
        self.company_input = page.locator('(//input[@placeholder="Your Company"])[2]')#.fill('ABC')  # Company field
        self.service_dropdown = page.locator('(//select[@name="service"])[2]')#.select_option('Business Listing')  # Service dropdown
        self.phone_input = page.locator('(//input[@placeholder="Your Phone"])[2]')#.fill('1234567890')  # Phone field
        self.message_textarea = page.locator('(//textarea[@name="message"])[2]')#.fill('Hello there')  # Message field
        
        ###############################################################################################################
        
        # ========== Service links ==========
        
        #***********************************************************
        ##Web Development
        self.cms_website_development = page.locator(
            '//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]'
        )
        self.ecommerce_web_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]'
        )
        #Drop-Down1
        self.web_development_dropdown_special = page.locator(
            '(//i[@class="fa fa-chevron-down text-red-2"])[1]'
        )  
        #Drop-Down option1
        self.website_development_special = page.locator(
            '//a[@href="https://www.tranktechnologies.com/website-development-company"]'
        )
        self.custom_web_portal_development = page.locator(
            '//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]'
        )

        #***********************************************************
        # App Development 
        self.ios_app_development = page.locator(
            '//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]'
        )
        self.android_app_development = page.locator(
            '//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]'
        )
        #Drop-Down
        self.app_development_dropdown_special = page.locator(
            '(//i[@class="fa fa-chevron-down text-red-2"])[2]'
        )  # Second submenu expand icon
         #Drop-Down option1
        self.android_app_development_dropdown_special = page.locator(
            '//a[@href="https://www.tranktechnologies.com/android-app-development-company"]'
        )
        #Drop-Down option2
        self.app_development_dropdown_link_special = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]'
        )
        self.hybrid_mobile_app_development = page.locator(
            '//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]'
        )
        self.cross_platform_mobile_app_development = page.locator(
            '//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]'
        )
        self.progressive_web_app_development = page.locator(
            '//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]'
        )
        
        #***********************************************************
        #UI UX Design
        self.mobile_app_design = page.locator(
            '//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]'
        )
        self.responsive_web_design = page.locator(
            '//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]'
        )
        self.brand_identity_design = page.locator(
            '//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]'
        )        
        self.web_development_option_list = [ self.cms_website_development, self.ecommerce_web_development ]
        
        #***********************************************************
        #Graphic Design
        self.logo_design = page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.banner_design = page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packaging_design = page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.business_cards_design = page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
        
        
        #LIST
        self.all_contactus_service_links_option_list = [
            # Web Development
            self.cms_website_development,
            self.ecommerce_web_development,
           # self.web_development_dropdown_special, 
           # self.website_development_special,
            self.custom_web_portal_development,

            # App Development
            self.ios_app_development,
            self.android_app_development, 
            #self.app_development_dropdown_special,
            #self.android_app_development_dropdown_special,
            #self.app_development_dropdown_link_special,
            self.hybrid_mobile_app_development,
            self.cross_platform_mobile_app_development,
            self.progressive_web_app_development,

            # UI/UX Design
            self.mobile_app_design,
            self.responsive_web_design,
            self.brand_identity_design,

            # Graphic Design
            self.logo_design,
            self.banner_design,
            self.packaging_design,
            self.business_cards_design
        ]
        
        self.all_contactus_service_links_option_list_special = [
                    # Web Development

               # self.web_development_dropdown_special, 
                self.website_development_special,                  
                # App Development
               # self.app_development_dropdown_special,
                self.android_app_development_dropdown_special,
                self.app_development_dropdown_link_special
            ]
        #***********************************************************
        
        #Follow US
        # Follow Us — social media locators
        self.facebook = page.locator('//a[@href="https://www.facebook.com/TrankTechnologies"]')
        self.linkedin = page.locator('//a[@href="https://in.linkedin.com/company/trank-technologies-official"]')
        self.instagram = page.locator('//a[@href="https://www.instagram.com/tranktechnologies/"]')
        self.pinterest = page.locator('//a[@href="https://in.pinterest.com/tranktechnologies12/"]')
        self.twitter = page.locator('//a[@href="https://twitter.com/tranktechno"]')
        self.youtube = page.locator('//a[@href="https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg"]')
        self.quora = page.locator('//a[@href="https://www.quora.com/profile/Trank-Technologies-1"]')

        self.social_media_list = [
            self.facebook,
            self.linkedin,
            self.instagram,
            self.pinterest,
            self.twitter,
            self.youtube,
            self.quora
        ]

    def contactus_form_fill(self):
        
        self.contact_us_link.click()
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(2000)
        self.contact_name_input.fill('Deepashri')
        self.contact_email_input .fill('deepashri.g.joshi@gmail.com') 
        #self.send_otp_button.click() 
        self.otp_input.fill('3434')
        self.company_input.fill("ABC")
        self.service_dropdown.select_option('Business Listing') 
        self.phone_input.fill("1234567890")
        self.message_textarea.fill("Hello there")
        self.page.wait_for_timeout(5000)

    def contactus_service_links(self):

        for link in self.all_contactus_service_links_option_list:

            self.contact_us_link.click()
            self.page.wait_for_load_state("load")
            link.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
    
    def new_windows_contactus_service_links_special(self):
        self.contact_us_link.click()  
        self.web_development_dropdown_special.click()      
        self.page.wait_for_timeout(5000)
        self.app_development_dropdown_special.click()
        self.page.wait_for_timeout(5000)
        for servicelinks in self.all_contactus_service_links_option_list_special:
            with self.page.context.expect_page() as new_page_info:
                servicelinks.click()
                
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                self.page.wait_for_timeout(2000)
                new_tab.close()
        #OR
        #  for i in self.all_contactus_service_links_option_list_special:
        #     with self.page.expect_popup() as popup:
        #         self.contact_us_link.click()  
        #         self.web_development_dropdown_special.click()      
        #         self.page.wait_for_timeout(5000)
        #         self.app_development_dropdown_special.click()
        #         self.page.wait_for_timeout(5000)
        #         i.click()
        #         new_tab = popup.value
        #         new_tab.wait_for_load_state("domcontentloaded")
        #         self.page.wait_for_timeout(2000)
        #         new_tab.close()
    
    def new_windows_contactus_social_media(self):
         for social_link in self.social_media_list:        
            with self.page.context.expect_page() as new_page_info:
                social_link.click()
                
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                self.page.wait_for_timeout(2000)
                new_tab.close()
                #OR
        # for social_link in self.social_media_list:
        #     with self.page.expect_popup() as popup:
        #         social_link.click()
                
        #         new_tab = popup.value
        #         new_tab.wait_for_load_state("domcontentloaded")
        #         self.page.wait_for_timeout(2000)
        #         new_tab.close()
                    