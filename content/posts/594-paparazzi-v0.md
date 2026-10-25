{
  "title": "Paparazzi V0",
  "date": "2003-08-01T00:00:02Z",
  "url": "/2003/08/01/paparazzi-v0/",
  "author": "Piotr Esden-Tempski",
  "wordpress_id": 594,
  "categories": [
    "Community",
    "Hardware",
    "Software"
  ],
  "tags": []
}

*This article is based on the gallery on the original [paparazzi savannah website](http://www.nongnu.org/paparazzi/gallery_v0.html).*

The following pictures were taken between February 2003 and August 2003.

This was the very first version of the system. The airborne hardware was minimal. It only consisted in a GPS receiver, a pic micro-controller and a modem. The pic would transmit GPS data to the ground. The plane was steered from the ground laptop using the buddy jack input of the radio control transmitter. The plane was equipped with a genuine FMA stabilizer and we tried to pilot "through" it.

This system suffered two major drawbacks :

- It was not robust at all regarding radio down-link losses.
- It was impossible to tune. The FMA autopilot reactions change a lot with the contrast. The system had to be tuned everyday to cope with this. We have tried several methods to detect this and compensate, but with very little success.

The best method we found was mounting the infrared sensor on a servo arm and command a bank angle through it. This solved the static problem, but the dynamic was still varying.

We also tried with the FMA switched off to reproduce the "GPS only" results of the [minimum complexity uav guidance and flight control system](http://controls.ae.gatech.edu/papers/johnson_dasc_01.pdf) paper by Eric N. Johnson, Aaron D. Kahn (yes, the one from [autopilot](http://autopilot.sf.net/).) and others.

It sort of worked in calm conditions but was unable to cope with turbulences.

Our GPS receiver was a ublox MS1E, hooked to an active car antenna. It would often refuse to start or loose signal. We learned from this that it was not a good idea to tamper with GPSs and antennas. We started to use SAM modules and had much better results.

The plane completed numerous flights. It ended its life in a corn field after becoming unresponsive. The plane was old and not so "well build". We suspect a connector got unplugged.

[![overall](/wp-content/uploads/2015/07/overall.jpg)](/wp-content/uploads/2015/07/overall.jpg)
[![avionic](/wp-content/uploads/2015/07/downlink.jpg)](/wp-content/uploads/2015/07/downlink.jpg)
[![gps antenna](/wp-content/uploads/2015/07/antenna.jpg)](/wp-content/uploads/2015/07/antenna.jpg)
[![infrared sensor](/wp-content/uploads/2015/07/fma_sensor.jpg)](/wp-content/uploads/2015/07/fma_sensor.jpg)
[![buddy jack controller](/wp-content/uploads/2015/07/uplink.jpg)](/wp-content/uploads/2015/07/uplink.jpg)
[![trajectory](/wp-content/uploads/2015/07/track_flight_7_2.png)](/wp-content/uploads/2015/07/track_flight_7_2.png)
[![crash](/wp-content/uploads/2015/07/pprz_v0.9_2.jpg)](/wp-content/uploads/2015/07/pprz_v0.9_2.jpg)
[![crash](/wp-content/uploads/2015/07/pprz_v0.9.png)](/wp-content/uploads/2015/07/pprz_v0.9.png)
