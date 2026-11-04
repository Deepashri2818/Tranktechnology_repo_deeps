import pytest
from pages.portfolio import portfolioclass

@pytest.mark.smoke
def test_portfolio_tabs_new_window(page):
    portfolio_obj = portfolioclass(page)  #classname from portfolio.py in page folder
    portfolio_obj.new_windows_portfolio_tabs() #function name from portfolio.py in page folder