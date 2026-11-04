import pytest
from pages.contactus import contactusclass

@pytest.mark.smoke
def test_contactus_form(page):
    contactus_obj = contactusclass(page)  #classname from contactus.py in page folder
    contactus_obj.contactus_form_fill() #function name from contactus.py in page folder

@pytest.mark.smoke
def test_contactus_service_links(page):
    contactus_obj = contactusclass(page)  #classname from contactus.py in page folder
    contactus_obj.contactus_service_links() #function name from contactus.py in page folder
        
        
@pytest.mark.smoke
def test_contactus_social_media_new_window(page):
    contactus_obj = contactusclass(page)  #classname from contactus.py in page folder
    contactus_obj.new_windows_contactus_social_media() #function name from contactus.py in page folder        
    

@pytest.mark.smoke
def test_contactus_service_links_special_new_window(page):
    contactus_obj = contactusclass(page)  #classname from contactus.py in page folder
    contactus_obj.new_windows_contactus_service_links_special() #function name from contactus.py in page folder    
    