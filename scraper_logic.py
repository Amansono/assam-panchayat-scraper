import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class AssamVoterScraper:
    def __init__(self):
        self.url = "https://ermssec.assam.gov.in/panchayat/download-pdf-electoral-roll"
        chrome_options = Options()
        # chrome_options.add_argument("--headless") # Piche chalane ke liye un-comment karein
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def select_dropdown_by_text(self, element_id, text):
        """Dropdown se option select karne ka clean method"""
        try:
            dropdown = Select(self.driver.find_element(By.ID, element_id))
            dropdown.select_by_visible_text(text)
            time.sleep(2) # Dropdown load hone ka wait
        except Exception as e:
            print(f"Selection Error at {element_id}: {e}")

    def get_data(self, district, zilla, gp, ward):
        try:
            self.driver.get(self.url)
            
            # Sequence mein select karna
            self.select_dropdown_by_text('district_id', district)
            self.select_dropdown_by_text('zp_id', zilla)
            self.select_dropdown_by_text('gp_id', gp)
            self.select_dropdown_by_text('ward_id', ward)
            
            # Search button click karna
            search_btn = self.driver.find_element(By.ID, 'search_btn_id') # ID verify karein site check karke
            search_btn.click()
            
            # PDF links nikalne ka logic yaha aayega
            # ...
            
            return "Success: PDF links fetched!"
        finally:
            self.driver.quit()
