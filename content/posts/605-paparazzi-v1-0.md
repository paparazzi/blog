{
  "title": "Paparazzi V1.0",
  "date": "2003-10-01T00:00:44Z",
  "url": "/2003/10/01/paparazzi-v1-0/",
  "author": "Piotr Esden-Tempski",
  "wordpress_id": 605,
  "categories": [
    "Community",
    "Hardware",
    "Software"
  ],
  "tags": []
}

*This article is based on the gallery on the original [paparazzi savannah website](http://www.nongnu.org/paparazzi/gallery_v0.html).*

The following pictures were taken between August 2003 and October 2003.

We had developed a flight controller board similar to the [autopilot](http://autopilot.sf.net/) one. We had been able to re-use some of their code - for example radio control receiving or servos commanding. Thanks allot Trammel.

The plane now had the potential to become fully autonomous (not controlled from ground anymore).

We made some test with the autopilot inertial sensor (3 gyros, 3 accels) and discovered that it was not that easy to go from ["tilt.c"](http://cvs.sf.net/viewcvs.py/autopilot/onboard/rev2/tilt.c?rev=1.4&view=auto) to something that would work in our plane.

Out of despair, we plugged the FMA sensor to our controller board ADCs, wrote some cheap proportional controllers and ... surprise, it worked very well.

We worked on calibration (how to estimate attitude angles from temperature differences), and Pascal came out with a Linear Least Square method that gave good results. We observe the turn radius given by GPS. Under the coordinated turn hypothesis, we can convert it to bank angle that will be compared with the one obtained from infrared. The Linear Least Square algorithm will minimize this error.

This system was awarded first price for autonomous flight at the [Ensica/Supaero second European MAV trophy](http://www.ensica.fr/microdrone/index_en.html) in front of 4 international teams.

We had a bad surprise during this competition. A radio control interference disengaged the autopilot during the flight. I was able to reengage it and the flight continued with no other problem. We now filter the radio control signal on mode toggling channels and didn't experience such phenomenon since. This is not satisfying. The only solution to be really sure would be to go PCM. Trouble is that radio control makers won't publish their signal specifications. The Futaba PCM was more or less reverse engineered and we are thinking about buying a transmitter from that brand.

The airframe was still a twinstar. It was loaded with several packs of batteries - was very heavy and had a small flight endurance.

We have mounted the autopilot in a maxi-kiool, an enlarged version of the [minus-kiool](http://perso.wanadoo.fr/scherrer/matthieu/english/kioole.html). This plane was light and flew long and well. It had a brushless motor and lipos batteries. This high priced gear had been offered to us by the [Pyrénées Modèles](http://www.pyreneesmodeles.fr/) shop in Toulouse. Thank you Mr Garat. Saint IGNUcius will give it back to you :)

We stopped using it because it was very fragile. The 56g version had no trouble landing on its motor but the 800g one didn't like it very much. Another reason why we abandoned that plane is that [Supaero](http://www.supaero.fr/) regarded the design as his and intended to use it for competitions were we would be opposed. They made a high tech carbon/kevlar molded version which they measured in their wind tunnel. I'm not aware that this plane is regularly flying.

After the trophy, we were contacted by people wishing to use Paparazzi. We took conscience that our code was not configurable and would cause problem to port to another airframe.

We began to rewrite it to support an high level configuration language.

[![GPS](/wp-content/uploads/2015/07/pprz10_01_sam_bottom.jpg)](/wp-content/uploads/2015/07/pprz10_01_sam_bottom.jpg)
[![GPS](/wp-content/uploads/2015/07/pprz10_02_sam_top.jpg)](/wp-content/uploads/2015/07/pprz10_02_sam_top.jpg)
[![Dev PCB](/wp-content/uploads/2015/07/pprz10_03_dev_board_1.jpg)](/wp-content/uploads/2015/07/pprz10_03_dev_board_1.jpg)
[![avionics](/wp-content/uploads/2015/07/pprz10_04_avr_ctrl_top.jpg)](/wp-content/uploads/2015/07/pprz10_04_avr_ctrl_top.jpg)
[![avionics](/wp-content/uploads/2015/07/pprz10_05_avr_ctrl_bot.jpg)](/wp-content/uploads/2015/07/pprz10_05_avr_ctrl_bot.jpg)
[![rc receiver](/wp-content/uploads/2015/07/pprz10_06_pprz_rx115.png)](/wp-content/uploads/2015/07/pprz10_06_pprz_rx115.png)
[![rc receiver](/wp-content/uploads/2015/07/pprz10_07_pprz_rx115_2.png)](/wp-content/uploads/2015/07/pprz10_07_pprz_rx115_2.png)
[![avionics](/wp-content/uploads/2015/07/pprz10_08_pprz_v1.0_2.png)](/wp-content/uploads/2015/07/pprz10_08_pprz_v1.0_2.png)
[![fuselage](/wp-content/uploads/2015/07/pprz10_09_pprz_v1.0_3.png)](/wp-content/uploads/2015/07/pprz10_09_pprz_v1.0_3.png)
[![fuselage](/wp-content/uploads/2015/07/pprz10_10_pprz_v1.0.png)](/wp-content/uploads/2015/07/pprz10_10_pprz_v1.0.png)
[![twinstar](/wp-content/uploads/2015/07/pprz10_11_tripod.jpg)](/wp-content/uploads/2015/07/pprz10_11_tripod.jpg)
[![trajectory](/wp-content/uploads/2015/07/pprz10_12_vol_27_09_03.jpg)](/wp-content/uploads/2015/07/pprz10_12_vol_27_09_03.jpg)
[![trajectory](/wp-content/uploads/2015/07/pprz10_13_screen_shot_trophee.png)](/wp-content/uploads/2015/07/pprz10_13_screen_shot_trophee.png)
[![Maxi kiool](/wp-content/uploads/2015/07/pprz10_14_maxi_kiool.jpg)](/wp-content/uploads/2015/07/pprz10_14_maxi_kiool.jpg)
[![Maxi kiool](/wp-content/uploads/2015/07/pprz10_15_maxi_kiool_2.jpg)](/wp-content/uploads/2015/07/pprz10_15_maxi_kiool_2.jpg)
