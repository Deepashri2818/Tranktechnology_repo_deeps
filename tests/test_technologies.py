import pytest
from pages.technologies import technologiestab

@pytest.mark.smoke
def test_ecommerce_technologies_menu_options(page):
    technology_obj = technologiestab(page)  #classname from technologies.py in page folder
    technology_obj.ecommerce_technologies_menu_options() #function name from technologies.py in page folder
    
@pytest.mark.smoke
def test_mobile_app_menu_options(page):
    technology_obj = technologiestab(page)  #classname from technologies.py in page folder
    technology_obj.mobile_app_menu_options() #function name from technologies.py in page folder    
    
@pytest.mark.smoke
def test_ai_menu_options(page):
    technology_obj = technologiestab(page)  #classname from technologies.py in page folder
    technology_obj.ai_menu_options() #function name from technologies.py in page folder 