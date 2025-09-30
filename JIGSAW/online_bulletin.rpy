### ONLINE BULLETIN SCREEN ###
label splashscreen:
    $ update_timer() ## THIS UPDATES THE JSON DATA FOR THE BOARD ##
    if persistent.cur_event_timer is not None:
        $ persistent.cur_time_left = get_event_time_left(persistent.cur_event_timer["event_timer_date"])
    return

label quit:
    if persistent.current_news != None:
        $ fetch_rpy(persistent.current_news["bullet_file"])
        $ delete_file()
    $ persistent.news = None
    $ persistent.current_news = None
    $ cleanup_temp_files()
