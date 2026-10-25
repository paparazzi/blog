{
  "title": "Elle0 Autopilot",
  "date": "2015-12-01T02:05:12Z",
  "url": "/2015/12/01/elle0-autopilot/",
  "author": "Piotr Esden-Tempski",
  "wordpress_id": 1038,
  "categories": [
    "Community",
    "Hardware",
    "Release"
  ],
  "tags": []
}

[![Elle0-in-hand-watermark_1024x1024](/wp-content/uploads/2015/12/Elle0-in-hand-watermark_1024x1024-300x202.jpg)![Elle0-back-watermark_1024x1024](/wp-content/uploads/2015/12/Elle0-back-watermark_1024x1024-300x203.jpg)](/wp-content/uploads/2015/12/Elle0-back-watermark_1024x1024.jpg)[1BitSquared](http://1bitsquared.com) has released [Elle0](http://1bitsquared.com/products/elle0-autopilot), a new [Paparazzi UAV](http://paparazziuav.org) autopilot. [Elle0](http://1bitsquared.com/products/elle0-autopilot) is the lowest cost autopilot developed specifically for use with the [Paparazzi UAV framework](http://paparazziuav.org). It was inspired by the [Lisa/MX](http://1bitsquared.com/products/lisa-mx-autopilot) and [Apogee](http://wiki.paparazziuav.org/wiki/Apogee/v1.00) autopilots and has been stripped down to the most essential features while preserving the flexibility that Paparazzi autopilots are famous for.

Here are some of the specs:

- STM32F4 168MHz ARM Cortex-M4 microcontroller with FPU
  - 1 Mbyte of Flash memory
  - 192+4 Kbytes of SRAM including 64-Kbyte of CCM (core coupled memory) data RAM
  - Cryptographic acceleration: hardware acceleration for AES 128, 192, 256, Triple DES, HASH (MD5, SHA-1), and HMAC
  - True random number generator
- 3 axis gyroscope (connected over SPI for high speed sampling and low latency)
- 3 axis accelerometer (connected over SPI for high speed sampling and low latency)
- 3 axis magnetometer (connected over SPI for high speed sampling and low latency)
- barometer (connected over dedicated SPI for low noise operation and low latency)
- 1 I2C auxilary sensor connection
- 2 TTL level serial ports for telemetry radio and GPS
- 2 serial input interfaces for remote control receivers (using Spektrum compatible JST connectors)
- 1 USB port for easy firmware upgrade
- 8 PWM outputs/inputs for servos or legacy PPM RC receivers
- 2 Analog inputs for system battery voltage and current measurement
- CAN TX and RX lines are accessible

[![Elle0-LisaMX-angle-watermark_1024x1024](/wp-content/uploads/2015/12/Elle0-LisaMX-angle-watermark_1024x1024-300x201.jpg)](/wp-content/uploads/2015/12/Elle0-LisaMX-angle-watermark_1024x1024.jpg)Mechanically [Elle0](http://wiki.paparazziuav.org/wiki/Apogee/v1.00) is designed around the 30.5mm M3 hole pattern, popularized by the Nano Quad community. But [Elle0](http://wiki.paparazziuav.org/wiki/Apogee/v1.00) can be used on more than just Nano Quads, it has everything on board to control anything from a small Quad through a big Octocopter to Airplanes or Helicopters. For an autonomous UAV you just need to add a GPS, Telemetry radio and maybe RC receivers. ;)

Apropos RC receivers, [Elle0](http://1bitsquared.com/products/elle0-autopilot) provides two Spektrum Satellite compatible connectors. You don't have to crimp special wires to connect your Spektrum Diversity setup to your autopilot anymore!

For more information check out [our Wiki Page](http://wiki.paparazziuav.org/wiki/Elle0). [1BitSquared](http://1bitsquared.com) is offering [Elle0 for Pre-Order](http://1bitsquared.com/products/elle0-autopilot) in their store. Elle0 will start shipping early 2016.
