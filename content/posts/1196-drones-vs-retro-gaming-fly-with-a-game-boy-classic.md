{
  "title": "Drones vs. Retro-gaming: fly with a Game Boy Classic",
  "date": "2016-08-01T22:23:44Z",
  "url": "/2016/08/01/drones-vs-retro-gaming-fly-with-a-game-boy-classic/",
  "author": "Gautier Hattenberger",
  "wordpress_id": 1196,
  "categories": [
    "Hardware",
    "Software",
    "Videos"
  ],
  "tags": []
}

Some time ago, I found my old Game Boy at my parents' house. So the first thing that came to my mind was: can I fly a drone with this ? (and also where is my Mario Bros cartridge).

So I spend some time searching the web to see if I could find some idea to solve my problem. And if it seems that piloting unmanned aircraft with a Game Boy is not so common, you can find everything you need to program it!

But you can't expect to go directly to an old custom serial com port to a wifi-based drone without some intermediate steps:

[![gb-ardrone2-wiring](/wp-content/uploads/2016/08/wiring-300x212.jpg)](/wp-content/uploads/2016/08/wiring.jpg)Finally, the Game Boy is just sending the bitmask corresponding to the buttons being pressed (with an Arduino and a FTDI to convert Game Link signals to USB), and a small program on the ground station converts this into actual commands for the drone (an ARDrone2 from Parrot with an extra GPS in my case).

The result is here:

<iframe src="https://www.youtube-nocookie.com/embed/LoLxrchwSpo" title="YouTube video" loading="lazy" allowfullscreen></iframe>

See <https://github.com/enacuavlab/PPRZonGB>for more information and source code of this demo.
