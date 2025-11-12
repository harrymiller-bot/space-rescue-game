class Globals:

    running = True
    FRAMES_PER_SECOND = 30

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800

    SCORE = 0

    # - Set the starting number of lives - #
    LIVES = 3

    

    money = 0

    # - Set the Window display name - #
    window_name = 'Dont take the bait!'

    # - Set the order of the rooms - #
    levels = ["WelcomeScreen", "GamePlay", "Mail", "End_game"]

    # - Set the starting level - #
    start_level = 0

    # - Set this number to the level you want to jump to when the game ends - #
    end_game_level = 4

    # - This variable keeps track of the room that will follow the current room - #
    # - Change this value to move through rooms in a non-sequential manner - #
    next_level = 0

    # - Change variable to True to exit the program - #
    exiting = False


# ############################################################# #
# ###### User Defined Global Variables below this line ######## #
# ############################################################# #

    response = None

    Email_decision = None

    total_count = 0
    destroyed_count = 0

    mail_messages_good = [
        "Great job keeping your data secure! G",
        "You successfully spotted a phishing attempt! G",
        "Your password strength is excellent!",
        "Thank you for enabling 2-factor authentication! G"
    ]

    mail_messages_bad = [
        "Click here to claim your free prize! B", 
        "Your account needs immediate verification B",
        "Urgent: Your bank account is locked B",
        "You've won a lottery you never entered! B"
    ]

    mail_messages_bad_R = [
        "Click here to claim your free prize! B", 
        "Your account needs immediate verification B",
        "Urgent: Your bank account is locked B",
        "You've won a lottery you never entered! B"
    ]

    mail_messages_good_R = [
        "Great job keeping your data secure! G",
        "You successfully spotted a phishing attempt! G",
        "Your password strength is excellent!",
        "Thank you for enabling 2-factor authentication! G"
    ]

    threshold = 99
