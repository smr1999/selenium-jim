from cgi import print_form
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time
from datetime import datetime
from . import constants
from .filteration import BookFilteration


class Booking(webdriver.Firefox):
    def __init__(self, driver_path=":./driver", teardown=False, *args, **kwargs):
        self.teardown = teardown
        os.environ['PATH'] += driver_path
        super(Booking, self).__init__(*args, **kwargs)
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(constants.BASE_URL)

    def select_change_currency(self, currency='USD'):
        change_currency_btn = 'button[data-tooltip-text="Choose your currency"]'
        self.find_element(
            By.CSS_SELECTOR,
            change_currency_btn
        ).click()

        currency_elm = f'a[data-modal-header-async-url-param$="selected_currency={currency}"]'
        self.find_element(By.CSS_SELECTOR, currency_elm).click()

    def select_place_to_go(self, place):
        place_elm = 'input[placeholder="Where are you going?"]'
        place_loc = self.find_element(By.CSS_SELECTOR, place_elm)
        place_loc.clear()
        place_loc.send_keys(place)

        try:
            self.find_element(By.CSS_SELECTOR,'li[data-i="0"]').click()
        except Exception:
            self.select_place_to_go(place)

    def select_date(self, timein, timeout):
        now_date = datetime.now()
        in_date = datetime.strptime(timein, '%Y-%m-%d')
        out_date = datetime.strptime(timeout, '%Y-%m-%d')

        if (in_date - now_date).days < 0 or (out_date - now_date).days < 0:
            print('Can not reserve before now !')
            return
        elif (out_date-in_date).days < 0:
            print('in date must greater than out date')
            return
        elif out_date.month - in_date.month > 1:
            print('Your travel can not longer than a month !')
            return

        month_diff = in_date.month - now_date.month

        next_month_elm_class = 'bui-calendar__control--next'
        next_month_loc = self.find_element(By.CLASS_NAME, next_month_elm_class)

        for i in range(month_diff):
            next_month_loc.click()

        in_elm = f'td[data-date="{timein}"]'
        self.find_element(By.CSS_SELECTOR, in_elm).click()

        out_elm = f'td[data-date="{timeout}"]'
        self.find_element(By.CSS_SELECTOR, out_elm).click()

    def select_acr(self):
        acr_elm_class = 'xp__guests__count'
        self.find_element(By.CLASS_NAME, acr_elm_class).click()

    def select_num_adults(self, count=1):
        adult_dec_elm = 'button[aria-label="Decrease number of Adults"]'
        adult_dec_loc = self.find_element(By.CSS_SELECTOR, adult_dec_elm)

        adult_inc_elm = 'button[aria-label="Increase number of Adults"]'
        adult_inc_loc = self.find_element(By.CSS_SELECTOR, adult_inc_elm)

        while True:
            adult_dec_loc.click()
            adult_count_elm_id = 'group_adults'
            if int(self.find_element(By.ID, adult_count_elm_id).get_attribute('value')) == 1:
                break

        for i in range(count-1):
            adult_inc_loc.click()

    def select_num_childern(self, age, count=0):
        children_inc_elm = 'button[aria-label="Increase number of Children"]'
        children_inc_loc = self.find_element(By.CSS_SELECTOR, children_inc_elm)

        for i in range(count):
            children_inc_loc.click()
            age_elm = f'select[data-group-child-age="{str(i)}"]'
            select_age = Select(self.find_element(By.CSS_SELECTOR, age_elm))
            select_age.select_by_value(str(age))

    def select_num_rooms(self, count=1):
        rooms_inc_elm = 'button[aria-label="Increase number of Rooms"]'
        rooms_inc_loc = self.find_element(By.CSS_SELECTOR, rooms_inc_elm)

        for i in range(count-1):
            rooms_inc_loc.click()

    def select_find(self):
        find_elm_class = 'sb-searchbox__button'
        self.find_element(By.CLASS_NAME, find_elm_class).click()

    def apply_filteration(self):
        filteration = BookFilteration(self)
        
        filteration.filter_stars(4, 5)
        filteration.sort_lowest_price()

    def report_result(self):
        box_elms = 'div[data-testid="property-card"]'
        boxes = self.find_elements(By.CSS_SELECTOR,box_elms)
        
        for box in boxes:
            print(box.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').get_attribute('innerHTML').strip())

        next_page_elm = 'button[aria-label="Next page"]'
        next_page_loc = self.find_element(By.CSS_SELECTOR,next_page_elm)
        if next_page_loc.is_enabled():
            next_page_loc.click()
            time.sleep(5)
            self.report_result()

    def __exit__(self, *args, **kwargs):
        if self.teardown:
            print('Exiting')
            time.sleep(10)
            self.quit()
