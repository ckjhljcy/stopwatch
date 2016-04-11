#this is a mini stopwatch
#if you stop the stopwatch at a whole second, you win
#you can run this code in http://www.codeskulptor.org/
#there is also a copy in http://www.codeskulptor.org/#user41_0jc1kuIUK0_5.py

import simplegui

#global variable
minute = 0
second = 0
dotsecond = 0
success_stop = 0
total_stop = 0

# Handler for mouse click
#Start the timer
def start():
    global timer
    timer.start()

#Stop the timer
def stop():
    global timer, success_stop, total_stop
    timer.stop()
    #To see if success this time
    if dotsecond == 0:
        success_stop = success_stop + 1
    total_stop = total_stop + 1

#Reset the timer
def reset():
    global minute, second, dotsecond, success_stop, total_stop
    timer.stop()
    #clear variable
    minute = 0
    second = 0
    dotsecond = 0
    success_stop = 0
    total_stop = 0

#Timer tick handler
def timer_tick():
    global minute, second, dotsecond
    #calculate minute, second and dotsecond
    dotsecond = (dotsecond + 1) % 10;
    if dotsecond == 0:
        second = (second + 1) % 60
        if second == 0:
            minute = minute + 1
       

# Handler to draw on canvas
def draw(canvas):
    #trans to string
    time = "%01d:%02d:%01d" % (minute, second, dotsecond)
    score = "%d/%d" % (success_stop, total_stop)
    #show string
    canvas.draw_text(time, [80,112], 48, "White")
    canvas.draw_text(score, [230,30], 32, "Green")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Stopwatch", 300, 200)
#register button handler
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
#register draw handler
frame.set_draw_handler(draw)
#register timer tick handler
timer = simplegui.create_timer(1, timer_tick)

# Start the frame animation
frame.start()
