{
  "title": "Lisa/M for developers",
  "date": "2011-06-22T02:51:05Z",
  "url": "/2011/06/22/lisam-for-developers/",
  "author": "Piotr Esden-Tempski",
  "wordpress_id": 276,
  "categories": [
    "Hardware"
  ],
  "tags": [
    "Aspirin",
    "autopilot",
    "fixed wing",
    "hardware",
    "Lisa",
    "Lisa/M",
    "Platform",
    "Quadrocopter"
  ],
  "archived_comments": [
    {
      "author": "flixr",
      "date": "2012-04-20 18:32:09",
      "text": "Hi Met,\nthere is currently no detailed step-by-step guide. But you should be able to find the information on how to setup your airframe file in the wiki: http://paparazzi.enac.fr/wiki/Airframe\\_Configuration\nThe control loops are documented in http://paparazzi.enac.fr/wiki/Control\\_Loops#Rotorcraft\\_autopilot\nCheers, Felix"
    },
    {
      "author": "sahul venkat",
      "date": "2012-04-10 10:15:30",
      "text": "Can Lisa M autopilot with aspirin IMU be used for controlling quadcopter?"
    },
    {
      "author": "flixr",
      "date": "2012-04-10 21:35:52",
      "text": "yes!"
    },
    {
      "author": "Metalman Baris",
      "date": "2012-04-14 18:23:44",
      "text": "Is there a step by step guide for gathering a quadrocopter using LisaM/Aspirin ?\nI mostly intrested on PID tuning part :)\nMet"
    },
    {
      "author": "jpeeeg",
      "date": "2011-06-22 14:44:57",
      "text": "Why not to use a smartphone for paparazzi? They have a lot of sensors and a good processor. We should use an iPhone or Android phone. Is there this king of projects?"
    },
    {
      "author": "esden",
      "date": "2011-06-22 18:40:55",
      "text": "Hi,\nThe problem with a cellphone is mostly the IO, it does not have i2c, several serial interfaces, PWM outputs and so on. Also most of the phones don't have sensors that can be read out with high enough frequency and/or have enough range to deal with the accelerations and angular speeds present in small flying aircraft.\nAlso aircrafts tend to crash from time to time, I would be scared putting the $600 IPhone on it. :)\nStill I think it is a nice challenge to try doing something like that, tell us about it when you try it. :)\nCheers Esden"
    },
    {
      "author": "jackb",
      "date": "2011-07-02 14:43:16",
      "text": "Look forward to Eagle files"
    },
    {
      "author": "Guillermo",
      "date": "2012-03-05 11:58:59",
      "text": "Hello Esden,\nI'm doing a research comparing several autopilot products out in the market. I chose Lisa/M as our reference Paparazzi product. However, I could not find any information regarding the operating temperature of this device. Is there any information available?"
    },
    {
      "author": "esden",
      "date": "2012-03-05 18:21:54",
      "text": "Hi thanks for asking,\nThat is a very good question. We did not conduct maximum temperature testing for Lisa/M. I only know that we were flying with Lisa/M 1.0 in the desert at 60C and then in the winter in Germany at -10C.\nI know that other controller boards like the tiny and twog are being used in polar expeditions. But then they are encapsulated in styrofoam to keep them warm.\nWe will not add any official guaranteed temperature specifications to Lisa/M 1.0 any more as that is an end of life product.\nWe may add temperature specification to Lisa/M 2.0 though as soon as we get a chance to do temperature testing.\nCheers!"
    },
    {
      "author": "esden",
      "date": "2011-12-02 01:13:41",
      "text": "Hi AJ,\nJoby Robotics is experiencing some technical difficulties. I don't know about their ETA of having it back up and running though.\nCheers Esden"
    },
    {
      "author": "AJ",
      "date": "2011-12-01 21:08:26",
      "text": "What happened to Jobyrobotics.com? it's been offline for at least a week. Anyone know?"
    },
    {
      "author": "ABL",
      "date": "2011-08-15 08:29:45",
      "text": "When it will be available to buy? JoyRobotics site lists it as \"Out of stock\"."
    },
    {
      "author": "dor",
      "date": "2011-08-13 09:07:37",
      "text": "hi,\nLisa/m is out of stock on jobyrobotics. Where can I get one ?\nthanks"
    },
    {
      "author": "sahulvenkat",
      "date": "2012-06-11 05:57:58",
      "text": "we are having a paparazzi\\_tiny 2.1 board , we would like to know if there is any open source 'c' code for a quadcopter that can be implemented on this board."
    },
    {
      "author": "esden",
      "date": "2012-06-11 06:15:24",
      "text": "Hi,\nAs far as I know paparazzi does not currently support rotorcraft code on the tiny boards.\nIt should be practically possible to connect an Aspirin IMU to the tiny board and make the rotorcraft code work on a tiny. I don't see a reason why that should not be possible.\nRotorcraft codebase is currently known to work on the LPC based Booz boards and the stm32 based Lisa/L, Lisa/M and Lia boards.\nCheers Piotr"
    },
    {
      "author": "sahulvenkat",
      "date": "2012-06-13 05:45:07",
      "text": "Thank you Esden,\ncan you please suggest which files of the rotorcraft code need to be modified in order to make it work for a quadrotor."
    },
    {
      "author": "sahulvenkat",
      "date": "2012-06-28 00:32:40",
      "text": "I would like to know the procedure for calibrating esc for a quadcopter which I am planning to fly using paparazzi tiny autopilot along with aspirin imu."
    },
    {
      "author": "sahulvenkat",
      "date": "2012-06-28 18:34:46",
      "text": "somebody please provide a solution for the above mentioned query. I have built the quad frame, as well mounted the motors but unable to calibrate the ESC's .\nThanks in advance,\nsahul"
    },
    {
      "author": "esden",
      "date": "2012-06-28 19:12:02",
      "text": "What do you mean with calibrating the esc?\nAlso you may want to ask questions like that on the paparazzi mailinglist by subscribing here: https://lists.nongnu.org/mailman/listinfo/paparazzi-devel and after that writing an email to paparazzi-devel@nongnu.org. There are much more people reding your questions and you are more likely to get an answer faster. Also #paparazzi channel on freenode is a good place to ask your questions. http://paparazzi.enac.fr/wiki/Contact\nCheers Esden"
    },
    {
      "author": "Viktor",
      "date": "2012-06-30 23:45:12",
      "text": "Whats the difference between paparazzi booz and twog hardware ,also I would like to know the feasibility of implementing rotorcraft on a twog autopilot. Somebody please help me in this regard.\nCheers,\nViktor."
    }
  ]
}

[![](/wp-content/uploads/2011/06/Lisa_M_V1_0_scale_top_streightened_white_bg-150x150.jpg "Lisa_M_V1_0_scale_top_streightened_white_bg")](/wp-content/uploads/2011/06/Lisa_M_V1_0_scale_top_streightened_white_bg.jpg)
Hello everyone,

After many months of hard work we have finally reached a version of [Lisa/M](http://wiki.paparazziuav.org/wiki/Lisa/M) that is ready for a wider range of developers. Although there are still some things missing that would allow a beginning user to use it with ease, we decided it is better to provide it to all of the other brilliant non core developers and users. You can find out more about it in the [Paparazzi Wiki](http://wiki.paparazziuav.org/wiki/LisaM). A big thanks go to [OpenUAS](https://github.com/OpenUAS) for his great help with the documentation.

[![](/wp-content/uploads/2011/06/Lisa_M_V1_0_scale_bottom_streightened_white_bg-150x150.jpg "Lisa_M_V1_0_scale_bottom_streightened_white_bg")](/wp-content/uploads/2011/06/Lisa_M_V1_0_scale_bottom_streightened_white_bg.jpg)

And before you start asking, it is not fully Open-Hardware YET! The schematics are available in the [SVN](http://svn.savannah.nongnu.org/viewvc/paparazzi-hardware/trunk/lisa_m/v1.0/?root=paparazzi) as well as in the [Wiki](http://paparazzi.enac.fr/wiki/LisaM#Schematic). The eagle board layout files will follow soon.

Let us know what you plan to build with this autopilot. Also if you have built an aircraft with [Lisa/L](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FM) or [Aspirin](http://wiki.paparazziuav.org/wiki/AspirinIMU) we would be very happy to see them. Just drop a comment below with a link to a picture. Let's spread the word of what is possible with Paparazzi!!!

Let's get flying!

Cheers Esden
