function Countdown_Timer () {
    Countdown = 300
    if (Countdown > 0) {
        Countdown += -1
        basic.pause(1000)
        if (Countdown <= 10) {
            music.changeTempoBy(40)
        }
    }
}
function stopcollaborateandlisten () {
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Quarter))
    music.playTone(175, music.beat(BeatFraction.Quarter))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(131, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Quarter))
    music.playTone(175, music.beat(BeatFraction.Quarter))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(131, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Whole))
}
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        stopcollaborateandlisten()
    }
    if (receivedNumber == 1) {
        FinalCountdown()
    }
})
function FinalCountdown () {
    music.rest(music.beat(BeatFraction.Whole))
    music.playTone(247, music.beat(BeatFraction.Quarter))
    music.playTone(220, music.beat(BeatFraction.Quarter))
    music.playTone(247, music.beat(BeatFraction.Whole))
    music.playTone(165, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.playTone(247, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(247, music.beat(BeatFraction.Half))
    music.playTone(220, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.playTone(247, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Whole))
    music.playTone(165, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Half))
    music.playTone(220, music.beat(BeatFraction.Quarter))
    music.playTone(196, music.beat(BeatFraction.Quarter))
    music.playTone(220, music.beat(BeatFraction.Half))
    music.playTone(196, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Half))
    music.playTone(220, music.beat(BeatFraction.Half))
    music.playTone(196, music.beat(BeatFraction.Half))
}
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(0)
})
input.onButtonPressed(Button.AB, function () {
    stopcollaborateandlisten()
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(1)
    Countdown = 300
    for (let index = 0; index < 300; index++) {
        Countdown += -1
        basic.pause(1000)
    }
    music.changeTempoBy(40)
    radio.sendNumber(1)
})
let Countdown = 0
radio.setGroup(1)
music.setTempo(110)
basic.forever(function () {
    led.plotBarGraph(
    Countdown,
    300
    )
})
