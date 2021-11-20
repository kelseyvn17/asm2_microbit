max_sound = 0
min_sound = 0
mean_sound = 0

image = Image("11111:"
              "11111:"
              "11111:"
              "11111:"
              "11111")

def dangerous_level(sound):
    """
    This function tracks for sound level input larger than 80 and output a blinking dangerous sign
    :param sound: the desired sound level (int)
    :return: none
    """
    loud_sound = 80
    if sound > loud_sound:
        exclamation_mark = Image("00900:"
                                 "00900"
                                 "09990"
                                 "90909"
                                 "99999")
        for i in range (2):
            display.show(exclamation_mark, delay = 100)  # blink the image 3 times every 100ms


def button_pressed(max):
    """
    This function depicts sound level on the led lights depending on users' input
    :param max: current maximum sound level to check the threshold level (int)
    :return: none
    """
    if button_a.is_pressed():
        dangerous_level(max)
        display.show(image*max_sound)
    if button_b.is_pressed():
        display.show(image*mean_sound)
    if button_a.is_pressed and button_b.is_pressed:
        display.show(image*sound_pitch)
        # if quite than display a straight line code


# Main program starts here
def sound_record():
    """
    This function runs a while loop to track sound level and update max and mean sound level
    :return: none
    """
    global min_sound, max_sound, number_sound
    sound_pitch = microphone.sound_level()
    display.show(image*sound_pitch)
    while True:
        if sound_pitch < min_sound:
            min_sound = sound_pitch
        if sound_pitch > max_sound:
            max_sound = sound_pitch
        # Input sound_pitch to list and calculate mean sound
        list_sound.append(sound_pitch)
        number_sound += 1
        total_sound_pitch = sum(list_sound)
        mean_sound = total_sound_pitch/number_sound
        # output dangerous sign if current sound is higher than 80
        dangerous_level(sound_pitch)
        # track for button pressed and display images
        button_pressed(max_sound)

