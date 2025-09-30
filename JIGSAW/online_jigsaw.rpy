### ONLINE BULLETIN SCREEN ###
screen bulletin_board:
    imagebutton:
        idle "images/UI/jig_menu.png"
        hover Transform("images/UI/jig_menu.png",matrixcolor=BrightnessMatrix(0.25))
        xalign 0.95 yalign 0.25
        action [
            Hide("explore"),
            SetVariable("cur_puzzle",1),
            Show("jig_choice")
        ]

label splashscreen:
    $ update_news() ## THIS UPDATES THE JSON DATA FOR THE BOARD ##
    return

label quit:
    if persistent.current_news != None:
        $ fetch_rpy(persistent.current_news["jig_file"])
        $ delete_file()
    $ persistent.news = None
    $ persistent.current_news = None
    $ cleanup_temp_files()
