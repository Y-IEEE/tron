# YIEEE JUMBOTRON
A modular Jumbotron display using octows2811

<br/>

## Objectives:

### "Fire Hazard" Problem:
Slightly offputting to have loose wires / someone called in a fire hazard
    - Purchase a tv roler stand
        - https://www.amazon.com/VIVO-Mobile-Trolley-Locking-STAND-TV04M/dp/B07581Z9SM/ref=sr_1_12?keywords=rolling+tv+stand&qid=1582142337&sr=8-12
        - https://www.amazon.com/Mobile-Rolling-Stand-Plasma-002-0038/dp/B075WD9MY3/ref=sr_1_24?keywords=rolling+tv+stand&qid=1582142380&sr=8-24
    - Idea: In place of laptop use clear acryllic case so you can still see wires (looks cool)

### SSH into Raspberry Pi:
Can't SSH into Raspberry Pi over wifi
    - Static IP, still waiting on ITS

### Front-End:
Possible merge with Building Team
    - Web interface that can send data to the Raspberry Pi
    - MQTT?

### Arduino End:
Set up live input feed from Raspberry Pi
    - Should be relatively easy?
    - https://www.pjrc.com/teensy/td_libs_OctoWS2811.html
        - Video Display Example Program

### Raspberry Pi End:
Subscribe to front-end and send data to arduino
    - MQTT?

### Idea: Raspberry Pi direct to lights using GPIO pins?
    - possibly easier?

## Timeline:
feb 22:
    - Arduino End
    - Raspberry Pi SSH
feb 29:
    - Front-End
    - Raspberry Pi subscriber
mar 28:
    - New stand, put everything together
apr 04:
    - Back-End
    - Raspberry Pi
apr 11:
    - Finish up?