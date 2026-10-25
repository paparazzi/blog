{
  "title": "Lisa STM32 Paparazzi Autopilot Overview Part 1.",
  "date": "2010-12-06T23:13:20Z",
  "url": "/2010/12/06/lisa-stm32-paparazzi-autopilot-overview-part-1/",
  "author": "Eric Parsonage",
  "wordpress_id": 62,
  "categories": [
    "Hardware"
  ],
  "tags": [
    "autopilot",
    "fixed wing",
    "hardware",
    "introduction",
    "Lisa",
    "Lisa/L",
    "Multicopter",
    "Open-Source",
    "overview",
    "Quadrocopter",
    "uav"
  ],
  "archived_comments": [
    {
      "author": "Danstah",
      "date": "2010-12-08 16:16:17",
      "text": "Keep up the good work guys. Can't wait to see more on the LISA. I am thinking I may order one or two"
    }
  ]
}

Many Paparazzi followers will be familiar with the popular [TINY](http://wiki.paparazziuav.org/wiki/Twog_v1) and [TWOG](http://wiki.paparazziuav.org/wiki/Twog_v1) fixed wing autopilot boards that have allowed so many UAV pilots their first taste of autonomous flight. A few will even have had the pleasure of using the [Booz](http://wiki.paparazziuav.org/wiki/Booz) multicopter autopilot board. All three of these designs are based on the Phillips LPC2148 microcontroller, which has proven to be a solid performer in this role. Antoine Drouin, the genius behind the Booz board, has once again outdone himself with a completely new series of autopilot boards based on the [STM32 ARM Cortex-M3](http://www.st.com/internet/mcu/class/1734.jsp) microcontroller, which has the umbrella name [Lisa](http://wiki.paparazziuav.org/wiki/Lisa). The first available is the [Lisa/L](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FL) and it is this board that will be explored in coming articles.

In the case of [Lisa/L](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FL) the 64 pin STM32F103RE processor has 64k of RAM, 512k of FLASH and runs at 72Mhz. To ensure that future autopilot features are not restricted by board design, Antoine has ensured that all of the processor's pins are exposed on Molex PicoBlade connectors. This allows access to all of the available peripherals, which include 3 USARTS, 2 SPI, 2 I2C, 1 CAN and 3 ADC channels and many more.

The board also provides an interface which is both electronically and mechanically compatible with that of the  [Gumstix Overo](http://www.gumstix.com/store/catalog/index.php?cPath=27_33), providing the option of running autopilot code (and any other applcations) under [Embedded Linux](http://www.openembedded.org/index.php/Main_Page) on an Overo with the STM32 acting as an I/O processor.

[![Lisa/L showing Gumstix Overo connector](/wp-content/uploads/2010/12/Lisa_l_bot.jpg "Lisa_l_bot")](/wp-content/uploads/2010/12/Lisa_l_bot.jpg) Lisa/L showing Gumstix Overo connector

The board is equipped with a pair of pressure sensors, one absolute to measure altitude and one differential to measure airspeed. Additionally, [Lisa/L](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FL) is fully compatible with the [BOOZ IMU module](http://wiki.paparazziuav.org/wiki/Booz) which can be conveniently mounted above the [Lisa/L board](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FL).

The addition of further sensors and external peripherals like modems, servos, USB webcams or wifi sticks is facilitated through the inclusion of three different power supplies (5V for external peripherals, 3V3 for avionics and a linear supply to provide clean power to sensitive sensors).

For the first time in a Paparazzi autopilot board, a USB based JTAG interface to the STM32 has been incorporated. This high speed interface allows for both fast programming and run time debugging using [GDB](http://www.gnu.org/software/gdb/). Debugging doesn't get any easier :). If the Gumstix module is mounted, this USB interface also provides the serial console.

Even from these few short paragraphs, it should be apparent that [Lisa/L](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FL) has been designed with power and flexibility in mind. This has already demonstrated with the flight of both quadrocopters, hexacopters and fixed wing aircraft utilising very different sensor suites (such as the [Paparazzi Booz IMU](http://wiki.paparazziuav.org/wiki/BoozIMU) and [Paparazzi IR sensors](http://wiki.paparazziuav.org/wiki/Infrared_Double_Wide_Sensor_Board) ).

For those that can't wait until next time the [Lisa/L Gallery](http://wiki.paparazziuav.org/wiki/LisaL_Gallery) is a must see.

In the upcoming articles we will explore the features of [Lisa/L](http://wiki.paparazziuav.org/wiki/Lisa#Lisa.2FL) further.

Until next time... Your Paparazzi Team
