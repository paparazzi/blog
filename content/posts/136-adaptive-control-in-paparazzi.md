{
  "title": "Adaptive Control in Paparazzi",
  "date": "2010-12-09T17:33:51Z",
  "url": "/2010/12/09/adaptive-control-in-paparazzi/",
  "author": "Felix Ruess",
  "wordpress_id": 136,
  "categories": [
    "Software"
  ],
  "tags": [
    "autopilot",
    "control",
    "fixed wing",
    "paparazzi",
    "Quadrocopter",
    "uav"
  ]
}

[Paparazzi](http://paparazziuav.org/) features adaptive control loops that can cope with substantial "changes" of the airframe in flight. May it be a motor dropout, partial loss of control surfaces or dropping a heavy payload. As videos usually say more than words, here are two that demonstrate this.

The first video shows Paparazzi's adaptive control loops (written by Pascal Brisset and Gautier Hattenberger at [ENAC](http://enac.fr)) for fixedwing aircraft keeping a Multiplex Twinstar on track, despite dropping a portion of the right wing and aileron and then switching the right motor off.

httpv://www.youtube.com/watch?v=TFrognLZ2Ak

Martin Mueller equipped the Twinstar with video cameras to document this. You can easily see that after part of the right wing is dropped the adaptive controller compensates for this automatically although only 50% of the aileron control surface remains. To make things even worse, the motor on the same side was switched off to simulate engine failure but the autopilot manages to keep it stable. At that point the aircraft became virtually impossible to fly by the very skilled safety pilot in manual control.

Although the adaptive vertical control for multicopters (by Antoine Drouin at [ENAC](http://enac.fr/)) has been around for almost two years now, here is a demo of a [Paparazzi Booz quadrotor](http://wiki.paparazziuav.org/wiki/Booz) suddenly dropping 50% off its weight.

httpv://www.youtube.com/watch?v=N0H9xWckeYQ

In this case, a [Kalman filter](http://en.wikipedia.org/wiki/Kalman_filter) of dimension one is used to estimate the the ratio of vertical acceleration over the produced thrust. This basically equates to the inverse of the mass during flight. Then the inverted dynamic model is used to issue a nominal thrust command based on this estimate. With this the quadrotor is able to stay very near same height, whereas with standard feedback control loops it would "go through the roof" when the payload is suddenly dropped.

Cheers, your Paparazzi Team
