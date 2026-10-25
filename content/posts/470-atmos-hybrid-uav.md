{
  "title": "ATMOS Hybrid UAV",
  "date": "2012-07-06T00:00:58Z",
  "url": "/2012/07/06/atmos-hybrid-uav/",
  "author": "paparazzi",
  "wordpress_id": 470,
  "categories": [
    "Community",
    "Competition",
    "Events",
    "Hardware",
    "Software"
  ],
  "tags": []
}

**[![Atmos](/wp-content/uploads/2015/07/Atmos.png)](/wp-content/uploads/2015/07/Atmos.png)ATMOS**, a hybrid airplane-quadrotor developed at the [MavLab](http://mavlab.lr.tudelft.nl/) of [TU-Delft](http://www.tudelft.nl/en/), was awarded third place (out of 140) in the [UAVForge](http://www.uavforge.net/) Competition. There were more than 140 initial [contestants](http://www.uavforge.net/uavhtml/milestones.php) and after several selection rounds with only 12 finalists, the paparazzi [Lisa/M](http://1bitsquared.com/collections/autopilots/products/lisa-m-autopilot "Lisa/M") powered ATMOS was one of the few that could actually make it to the remote target site miles away in an RF unfriendly environment. No team fully completed the baseline objectives which is why no prices were issued. The vertical takeoff and landing, together with long range thanks to the wing and flexibility thanks to [open-source paparazzi](https://wiki.paparazziuav.org/wiki/Main_Page) were key factors in this event [[1]](http://www.youtube.com/watch?v=81NvfLFzhqQ).

But probably more important, the development of ATMOS has added a new [code-base](https://github.com/tudelft/paparazzi/tree/atmos-master4-flyoff) to paparazzi to enable the control of any hybrid [multi-lifting](https://github.com/tudelft/paparazzi/blob/atmos-master4-flyoff/sw/airborne/firmwares/rotorcraft/force_allocation_laws.c) device vehicle. ATMOS can take-off vertically as a quadrotor, transition to full forward flight as an airplane but also fly in any intermediate transition stage fully autonomously. So let your imagination go wild!
