from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.select_change_currency(currency='EUR')
    bot.select_place_to_go(place='United States')
    bot.select_date(timein='2022-10-30',timeout='2022-11-05')
    bot.select_acr()
    bot.select_num_adults(count=8)
    bot.select_num_childern(count=4,age=3)
    bot.select_num_rooms(count=4)
    bot.select_find()
    bot.apply_filteration()
    bot.refresh()
    bot.report_result()