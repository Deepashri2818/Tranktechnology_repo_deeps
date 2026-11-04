import pytest
from pages.verticals import vertical

@pytest.mark.smoke
def test_trading_menu_options(page):
    trading_obj = vertical(page)  #classname from verticals.py in page folder
    trading_obj.trading_menu_options() #function name from verticals.py in page folder
    
@pytest.mark.smoke
def test_retail_ecommerce_menu_option(page):
    trading_obj = vertical(page)  #classname from verticals.py in page folder
    trading_obj.retail_ecommerce_menu_option() #function name from verticals.py in page folder    
    
@pytest.mark.smoke
def test_fintect_menu_option(page):
    trading_obj = vertical(page)  #classname from verticals.py in page folder
    trading_obj.fintech_menu_options() #function name from verticals.py in page folder        
    
@pytest.mark.smoke
def test_healthcare_menu_option(page):
    trading_obj = vertical(page)  #classname from verticals.py in page folder
    trading_obj.healthcare_menu_option() #function name from verticals.py in page folder        

@pytest.mark.smoke
def test_custom_app_menu_option(page):
    trading_obj = vertical(page)  #classname from verticals.py in page folder
    trading_obj.custom_app_menu_option() #function name from verticals.py in page folder            
        