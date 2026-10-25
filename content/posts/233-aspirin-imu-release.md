{
  "title": "Aspirin IMU Release",
  "date": "2011-02-21T23:27:48Z",
  "url": "/2011/02/21/aspirin-imu-release/",
  "author": "Piotr Esden-Tempski",
  "wordpress_id": 233,
  "categories": [
    "Hardware"
  ],
  "tags": [
    "Aspirin",
    "hardware",
    "IMU",
    "purchase",
    "release",
    "shop",
    "video"
  ],
  "archived_comments": [
    {
      "author": "Chris Anderson",
      "date": "2011-02-25 19:12:25",
      "text": "Is this open source?"
    },
    {
      "author": "esden",
      "date": "2011-02-25 21:26:43",
      "text": "Yes it is Open-Source. The driver source code is available in the [paparazzi GitHub repository](https://github.com/paparazzi/paparazzi/blob/master/sw/airborne/subsystems/imu/imu_aspirin.c). For more information look in the [Wiki](http://paparazzi.enac.fr/wiki/AspirinIMU)."
    },
    {
      "author": "Simon",
      "date": "2011-03-23 14:29:53",
      "text": "Looking closer, the bypass capacitor values for the VDD and VLOGIC pins of the gyro seem to be switched compared to the datasheet."
    },
    {
      "author": "Simon",
      "date": "2011-03-23 12:59:31",
      "text": "Are you quite sure the HMC5843 is wired correctly? According to the schematic, pin DVDD is connected to +3V3, while according to Honeywell's admittedly crappy datasheet, it should be tied with pin C1 and connected to ground through a capacitor.\nAccording to the datasheet, when VREN is tied to AVDD, the digital logic part is powered from an internal regulator. This implies that by connecting DVDD to +3V3 you are connecting the output of the internal regulator to +3V3, which sounds quite bad."
    },
    {
      "author": "Simon",
      "date": "2011-02-28 15:55:36",
      "text": "but why does the chip on the photo say ITG-3200?"
    },
    {
      "author": "esden",
      "date": "2011-02-28 17:47:07",
      "text": "Hehe, I knew someone would notice sooner or later. :) Yes the IMU in the photo has an ITG-3200 mounted. The unit we took the photos on had that chip mounted. It is an earlier prototype. The units from the Joby Robotics shop are shipping with IMU-3000. As soon as I have newer photos I will update the picture. Promissed! :)"
    },
    {
      "author": "Paul",
      "date": "2011-02-28 20:54:37",
      "text": "You did a wonderful job, congratulations! but ... IMU3000 you used as a simple gyroscope. In truth IMU3000 is a sensor fusion and contains a DMP Digital Motion Processor can calculate quaternion, rotation matrix and other complex functions independently. Unfortunately it is very complex because you use it INVENSENSE does not release specific information. Thanks to some \"knowledge\" I managed to get the Motion Processing Library for XMEGA (INVENSENSE original) but I need help to use them on Arduino system. Can you help me? Thanks......."
    },
    {
      "author": "esden",
      "date": "2011-02-28 18:03:32",
      "text": "No for the time being the Eagle files for Aspirin are not released in a OSHW definition compatible way. We at Joby Robotics would love to be able to release the files. But we don't feel comfortable with that at the moment. It is a continuing discussion here at Joby Robotics, so let's hope for the best! :)\nP.S. Aspirin is not a \"Paparazzi\" design as such, it was developed at Joby Robotics with close collaboration with Paparazzi community. It may have not been reflected by the article properly for some readers."
    },
    {
      "author": "Chris Anderson",
      "date": "2011-02-25 22:23:49",
      "text": "Thanks esden, but I meant the hardware, not the software. Where are the Eagle files?"
    },
    {
      "author": "esden",
      "date": "2011-09-06 00:56:48",
      "text": "The picture is of a little bit earlier board. Currently we use IMU-3000 on Aspirins.\nCheers Esden"
    },
    {
      "author": "Henry",
      "date": "2011-09-05 23:13:03",
      "text": "Hello, it's noted that you use IMU-3000, but in the picture it seems to be an ITG3200, what's used on the board?"
    }
  ]
}

[![Aspirin IMU on Booz Compatible Carrier Board](/wp-content/uploads/2011/02/IMG_7963_1-150x150.jpg "aspirin_imu_on_carrier")](/wp-content/uploads/2011/02/IMG_7963_1.jpg)Today we are pleased to announce the public release of our next generation IMU, [Aspirin](http://wiki.paparazziuav.org/wiki/AspirinIMU)! After a lengthy research, development, and testing period we are now happy with the hardware and the software drivers for this unique IMU. It is incredibly small and light, three digital sensors packed onto a single 19x14mm PCB. The footprint allows you to integrate it into your own designs too. We are also making it available via a carrier board for drop in use on [Lisa/L](http://wiki.paparazziuav.org/wiki/User/LisaL).

Besides its small size [Aspirin](http://wiki.paparazziuav.org/wiki/AspirinIMU) is cheaper then the [Booz IMU](http://wiki.paparazziuav.org/wiki/Booz) you already know. The use of all digital sensors reduces size, cost and complexity while simplifying calibration.

[Aspirin](http://wiki.paparazziuav.org/wiki/AspirinIMU) provides 9 degrees of measurement (DOM): 3 axis linear acceleration, 3 axis angular velocity, and 3 axis magnetic field measurement.

It consists of:

- 3 axis accelerometer (ADXL345)
- 3 axis gyroscope (IMU-3000)
- 3 axis magnetometer (HMC5843)

This IMU is ready for the next generation  [Lisa/M](http://paparazziuav.org/2010/12/14/lisam-next-generation-entry-level-paparazzi-autopilot/) autopilot that we wrote about before. The module fits directly on [Lisa/M](http://wiki.paparazziuav.org/wiki/Lisa/M) without the need of a carrier board.

We did not add an MCU on the board to save space, reduce cost, and improve latency behavior when connected to an autopilot. You have direct access to the sensor busses.

[Aspirin](http://wiki.paparazziuav.org/wiki/AspirinIMU) uses the latest generation of Invensense 3 axis MEMS gyroscopes. IMU-3000's advantage over other sensors (such as ITG-3200 found in similar IMU designs) is its selectable range. Selectable range allows the user to obtain maximum resolution and optimum performance, depending on vehicle dynamics and desired flight mode. No longer will it be necessary to limit vehicle dynamics to 300º/s, as [Aspirin's](http://wiki.paparazziuav.org/wiki/AspirinIMU) gyroscopes have a range of up to 2000º/s.

Here a small video of a Quad with [Lisa/L](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FM) autopilot with [Aspirin IMU](http://wiki.paparazziuav.org/wiki/AspirinIMU) running Paparazzi rotorcraft firmware, for some additional entertainment. Have fun! :)

httpvh://www.youtube.com/watch?v=k1\_iPCJLuwA

Cheers your Paparazzi team.
