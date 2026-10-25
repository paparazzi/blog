{
  "title": "JMD 04 Results",
  "date": "2004-09-20T10:18:38Z",
  "url": "/2004/09/20/jmd04-results/",
  "author": "paparazzi",
  "wordpress_id": 860,
  "categories": [
    "Community",
    "Competition",
    "Hardware"
  ],
  "tags": []
}

Paparazzi was very successful at the JMD04 (Journées Micro Drones) competition/conference in Toulouse, France. The ENAC team won first place with the Microjet. Here is the [report](https://lists.gnu.org/archive/html/paparazzi-devel/2004-09/msg00000.html) from
Antoine Drouin.

```
Hi everybody
```

Paparazzi's microjet won the JMD04 MAV event
( <http://www.micro-uav04.net/> )

During the event, we had contact with industrials who told us they were interested in manufacturing our board. Maybe the end of the nightmare for those of you who don't enjoy the soldering iron :)

We've received PCBs and assembled the new version of the controller board (v1.2.1) - The servo driver reset bug is fixed and the board seems to behave well on the desk - We'll let you know how it does in flight in the following days.

We've tagged the version that we used for the trophy (jmd-04 ). You should be able to safely upgrade from the previous tagged version (emav-04). Most noticable difference is the use of UTM in place of GWS84. You'll have to setup your GPS receiver to output the correct messages. Maybe we could add our receiver configuration in the CVS ?

You will also need a patched version of ivy (the network software bus) while the guy at openatc.org make a new release with the patches we sent them.

We're setting up a debian package repository and let you know when it's done.

We intend to break everything in the CVS head in the following days to add ground station support for several aircraft at once, so you'd better stick to the jmd-04 version for now.

During the flight competition, we once again had trouble with radio jamming. We really need a checksumed rf transmission. I will call Multiplex once more to ask for their PCM specifications. If they refuse once again to disclose it, I want to define and implement a new "open" PCM protocol, eventually with low throughput data in it. We could use a commercial HF module (maybe even a
frequency synthesys once) and connect it to the laptop. Then fly using a joystick or a simulator transmitter.

Do you have an idea about a suitable protocol or know the interface of a commercial HF module ?

A+

Antoine
