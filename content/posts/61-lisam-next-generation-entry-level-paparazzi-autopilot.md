{
  "title": "Lisa/M next generation entry level Paparazzi Autopilot",
  "date": "2010-12-14T05:53:27Z",
  "url": "/2010/12/14/lisam-next-generation-entry-level-paparazzi-autopilot/",
  "author": "Piotr Esden-Tempski",
  "wordpress_id": 61,
  "categories": [
    "Hardware"
  ],
  "tags": [
    "autopilot",
    "electronics",
    "fixed wing",
    "hardware",
    "Lisa",
    "Lisa/M",
    "Multicopter",
    "Open-Source",
    "Quadrocopter",
    "uav"
  ],
  "archived_comments": [
    {
      "author": "Marius Popescu",
      "date": "2010-12-25 17:11:55",
      "text": "I've been following the Paparazzi project for a couple of years and I must tell you, I'm really excited about the direction it's heading. Lisa/M (with the embedded Aspirin IMU) is an excellent concept. A more cost efficient, compact design, like Lisa/M will surely get more people interested in the Paparazzi project and autonomous flight in general.\nI'm definitely sold. Anxiously awaiting new details/availability.\nThank you for all the awesome work on the Paparazzi project and please keep it coming. Merry Christmas and a Happy New Year to the Paparazzi team and community."
    },
    {
      "author": "max",
      "date": "2010-12-14 18:59:49",
      "text": "very nice, keep the good news coming! :)"
    },
    {
      "author": "Matjaz",
      "date": "2010-12-14 21:29:29",
      "text": "Is it possible to get schematics for Lisa/m, and where can one get more information about aspirine IMU ?\nCheers, Matjaz"
    },
    {
      "author": "esden",
      "date": "2010-12-15 11:10:33",
      "text": "@Matjaz\nNo Lisa/M schematics are not released yet. They will be released as soon as the hardware is stable and available. The same way it was the case with Lisa/L. You will be able to find them in the paparazzi wiki and in the hardware repository. As it is the case for Lisa/L here: http://paparazzi.enac.fr/wiki/Dev/LisaL/Schematics/V1.1\nThere will be an article about Aspirin soon. :) ... But to calm down your curiosity, Aspirin is an SMD carrier board with power supply and EEPROM for an IMU-3000 3 Axis gyro, HMC5843 magnetometer and ADXL345 accelerometer.\nAnd to calm down my curiosity, why are you asking? :)\nCheers Esden"
    },
    {
      "author": "Matt",
      "date": "2011-03-22 22:43:17",
      "text": "Thanks again Esden.\nThose look great projects. Just the kind of items we want everybody to be able to connect up.\nI can't share the spec with you right now. It is in a very early draft.\nHopefully I can send you something in a week.\nIf you are getting desperate, let me know.\nMy application to the dev mailing list did not work. Need to try again. Then I can stop cluttering your beautiful blog with off topic comments.\nRegards Matt"
    },
    {
      "author": "eduardo",
      "date": "2011-01-06 17:14:51",
      "text": "Hello ..\nhow i can be the booz beta-tester ? or where i can order booz hardware ?\ni have high electronic skills and very interested in use paparazzi on my photogrametry jobs.\nregards."
    },
    {
      "author": "Oliver",
      "date": "2010-12-24 10:33:11",
      "text": "I'll buy one as soon as it is available.\nThat thing is great!"
    },
    {
      "author": "Matjaz",
      "date": "2010-12-24 15:02:24",
      "text": "@esden\nI am designing my own UAV system with Atmel microcontrollers , and I'm currently evaluating options for pitch/roll detection. For 1st version of autopilot I will probably use thermopile sensors, but later versions will use some form of inertia measurment circuits.\nCheers and happy xmas ;)"
    },
    {
      "author": "Matt",
      "date": "2011-03-19 08:10:38",
      "text": "Lisa/M has the perfect combination of size and performance for me. Bring it on!\nUnfortunately I am not good with linux so paparazzi will be difficult for me.\nThere is a solution. The Ardupilot32 project is porting the popular ArduPilotMega code to the STM32 processor.\nhttp://www.virtualrobotix.com/\nThere is a possibility here for you to capture hardware volume in both paparazzi and ardupilot projects.\nThere are not quite enough PWM outputs on the STM32 for my airframe. I also prefer using a hardware failsafe to prevent disasters. This failsafe connects using the CAN controller. For this reason it would be good to know if the CAN connection is available on Lisa/M\nThanks to Marc S for directing me to this project. I would never have thought of it otherwise."
    },
    {
      "author": "Piotr Esden-Tempski",
      "date": "2011-03-19 19:57:43",
      "text": "@Matt\nHey! Nice to hear from you. Thanks for the link to virtualrobotix we will definitely take a look at it.\nAnd just so you know paparazzi works on Mac OS X now too so you don't need to use Linux. Port to Windows is in the works as well as other improvements to make it easier to use and that everyone can profit from 8years of experiance building autopilots this project has. :)\nYes Lisa/M offers a high speed CAN interface. I will write a new article as soon as the current revision of the hardware comes back from the manufacturer. We are getting very close to getting the hardware and software in a state where we can let it loose on everyone. :)\nStill I think you are right that the hardware can run any autopilot software, and that we should take a look at the Ardupilot32 project.\nCheers Esden"
    },
    {
      "author": "Piotr Esden-Tempski",
      "date": "2011-03-21 00:25:07",
      "text": "Hey Matt,\nWe are using CAN to talk to the so called CSC's (Can Servo Controller) ... these are expansion boards that provide ADC input, PWM, Serial and so on and are being addressed using the CAN interface.\nThere is a simple protocol implemented for communication to those devices from the autopilot.\nLisa/L and Lisa/M are providing a CAN interface to connect to those.\nI am working also on Open-BLDC (http://open-bldc.org) ... these motor controllers are intended for Quadrocopters and the clogic boards are providing an isolated CAN interface (earlier designs had a non isolated CAN interface). I have not decided on a protocol for communicating with them yet. All I have in software is only a test firmware, but implementing this interface is very high on my priority list, so I guess I will have to decide on a CAN interface protocol soon.\nI saw the invitation to the mavlink discussion, but I did not have time to have a deeper look at their approach yet. I definitely agree that it would be a very good thing to have a standardized protocol between different UAV projects there. Thanks for pointing that out and I will definitely take a deeper look. :)\nI am not sure who besides us (JobyRobotics/JobyEnergy) was using CAN in paparazzi in the past. So I can't point you to anyone besides myself and my collegues really. But you may want to ask on the paparazzi developer mailinglist. (http://lists.nongnu.org/mailman/listinfo/paparazzi-devel)\nCheers Esden"
    },
    {
      "author": "Matt",
      "date": "2011-03-20 07:33:01",
      "text": "Thanks Esden\nI am a win7 user but run VirtualBox for anything linux. I am just not that good at at it yet.\nAre any of you using CAN already?\nThere is a group of us including the MAVlink team trying to define a CAN communication standard for UAV. At the moment it is loosely based on the ARINC825 standard.\nThat discussion is here:\nhttp://diydrones.com/profiles/blogs/can-bus-on-micro-air-vehicles\nand here:\nhttp://groups.google.com/group/mavlink\nIt would be great if all of the CAN items that people create in the UAV community would talk to each other. We would really like to avoid having many different standards.\nIf you can put me in contact with any CAN users that would be excellent.\nRegards Matt"
    },
    {
      "author": "flixr",
      "date": "2011-01-20 20:57:46",
      "text": "@eduardo\nGreat to hear that you want to test paparazzi booz!\nYou can buy bare booz pcbs on ppzauv.com, I'm not aware of any selling assembled booz main boards at the moment. At www.jobyrobotics.com you can buy the newest booz IMU. But I would recommend getting a Lisa/L (also jobyrobotics) or to wait for Lisa/M.\nIt really depends what you are after exactly... Using Lisa/L might be interesting for you to connect some camera hardware to the gumstix running Linux.\nAs for the software part, you can start right away ;-)"
    },
    {
      "author": "Fatih",
      "date": "2011-04-01 14:25:10",
      "text": "Hi,\nThis is a great project. Keep up the good work!\nI am also working on a quadotor right now and is there a chance to have the source code for the adaptive control algorithm?\nBest Regards,\nFatih"
    },
    {
      "author": "Papyjac33",
      "date": "2011-07-25 11:01:05",
      "text": "Hi\nFor LISA/M with IMU how many weeks we have to wait to buy them..?\nFor the Eagle files \\*.brd when we can hope to see them on Savannah CVS ...?\nBest Regards\nPapyjac33"
    },
    {
      "author": "esden",
      "date": "2011-07-25 21:05:38",
      "text": "@fatih The sourcecode is in the paparazzi git repository. https://github.com/paparazzi/paparazzi\n@Papyjac33 There should be more stock of Lisa/M with Aspirin next week. We plan to release the board files soon, but I can't give you an exact date."
    }
  ]
}

[![Lisa/M Bottom](/wp-content/uploads/2010/12/Lisa_m_bot_small-300x256.jpg "lisa_m_bot_small")](/wp-content/uploads/2010/12/Lisa_m_bot_small.jpg) Lisa/M Bottom

As promised, we want to talk about projects we are currently working on. One of them is [Lisa/M](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FM).

[Lisa/M](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FM) will be the medium sized Autopilot based on the [STM32 Cortex-M3](http://www.st.com/internet/mcu/class/1734.jsp) microcontroller. It is part of the [Lisa](http://wiki.paparazziuav.org/wiki/Lisa) series of Autopilots. It is very small (50mm x 25mm), about the size of an RC receiver. We want it to be as affordable as possible so that more people can join the autonomous aircraft revolution. The final cost still needs to be determined, as we are not done with the development yet.

Due to its large capabilities and small size, it can be used as a full Autopilot for fixed wing airplanes, multicopters and helicopters, as well as an IO extender/repeater (in which case the IMU can be left out, cutting the cost significantly).

One other interesting feature is that it can host the SMD mounted [Aspirin IMU](https://wiki.paparazziuav.org/wiki/AspirinIMU) without adding size. The [Aspirin IMU](https://wiki.paparazziuav.org/wiki/AspirinIMU) is the next generation small, flat, low part count and cheap IMU that will get an article by itself.

[Lisa/M](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FM) features a multitude of interfaces:

- CAN serial
- USB
- SPI serial
- I2C serial
- 2 RS232 3V3 and 5V TTL level (UART)
- 6 PWM servo outputs
- 7 analog inputs
- 3 general purpose digital in-/out-puts

[Lisa/M](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FM) with mounted IMU has the following sensors on board:

- 3 Axis Gyroscope
- 3 Axis Accelerometer
- 3 Axis Magnetometer
- Pressure sensor

The pressure sensor is mounted directly on [Lisa/M](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FM) as this sensor is not provided by [Aspirin](http://wiki.paparazziuav.org/wiki/AspirinIMU). Without a GPS unit you have all necessary sensors for full attitude and altitude stabilization in an extremely small package (if you know of a smaller one, let us know!). With an external GPS unit, it is a full fledged Autopilot.

Now you may ask when will it be available for prime time. We can't give you a definite answer just yet. What we definitely can say is that it will be as soon as it is ready.  :)

But now seriously. We are currently working on the second revision of our prototypes. Based on our experience it takes 3 to 4 revisions of a hardware design to get it right. That means in a few months if everything goes well.

Don't lose faith though. The first design was already good enough to be able to fly an airplane. That means that there are no major mistakes in the design.

We will of course keep you up to date on this projects progress in future articles.

Cheers ... your Paparazzi team.
