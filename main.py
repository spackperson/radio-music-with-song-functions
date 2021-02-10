def stopcollaborateandlisten():
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.QUARTER))
    music.play_tone(175, music.beat(BeatFraction.QUARTER))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(131, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.QUARTER))
    music.play_tone(175, music.beat(BeatFraction.QUARTER))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(131, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))

def on_received_number(receivedNumber):
    global Countdown
    if receivedNumber == 0:
        stopcollaborateandlisten()
    if receivedNumber == 1:
        FinalCountdown()
        FinalCountdown()
        FinalCountdown()
    if receivedNumber == 1:
        Countdown = 30
        if Countdown > 0:
            Countdown += -1
            basic.pause(1000)
            if Countdown <= 10:
                music.change_tempo_by(40)
radio.on_received_number(on_received_number)

def FinalCountdown():
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.QUARTER))
    music.play_tone(220, music.beat(BeatFraction.QUARTER))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(165, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(247, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(247, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(165, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(220, music.beat(BeatFraction.QUARTER))
    music.play_tone(196, music.beat(BeatFraction.QUARTER))
    music.play_tone(220, music.beat(BeatFraction.HALF))
    music.play_tone(196, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.HALF))
    music.play_tone(220, music.beat(BeatFraction.HALF))
    music.play_tone(196, music.beat(BeatFraction.HALF))

def on_button_pressed_a():
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    stopcollaborateandlisten()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_number(Countdown)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Countdown = 0
radio.set_group(1)
music.set_tempo(110)

def on_forever():
    pass
basic.forever(on_forever)
