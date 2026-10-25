{
  "title": "Paparazzi V5.8 release",
  "date": "2015-12-24T14:29:20Z",
  "url": "/2015/12/24/paparazzi-v5-8-release/",
  "author": "Piotr Esden-Tempski",
  "wordpress_id": 1070,
  "categories": [
    "Release",
    "Software"
  ],
  "tags": []
}

[![Penguin_logo](/wp-content/uploads/2015/07/Penguin_logo-150x150.gif)](/wp-content/uploads/2015/07/Penguin_logo.gif)Merry Christmas dear Paparazzians!

We are happy to announce the release of Paparazzi; **v5.8**, providing you with lots of new features and improvements!

Just to pick out a few:

- [ADS-B](https://en.wikipedia.org/wiki/Automatic_dependent_surveillance_%E2%80%93_broadcast) support
- improved use of optic flow for velocity estimation
- improved [mavlink](http://qgroundcontrol.org/mavlink/start) support
- possibility to reduce RAM and Flash usage by compressing the sine table
- this allowed us to add basic support for naze32, CC3D and CJMCU boards
- flip mode for multicopters
- [INDI](http://wiki.paparazziuav.org/wiki/Subsystem/stabilization#INDI) guidance loop
- lots of improvements/additions for computer vision modules
- high speed logging to SD Card via SPI
- improve support for Bebop and add Bebop2
- guided mode for rotorcrafts

For a detailed overview refer to the [CHANGELOG](https://github.com/paparazzi/paparazzi/blob/v5.8/CHANGELOG.md). :)

If you are already using paparazzi with [Git](http://wiki.paparazziuav.org/wiki/Git "Git"), to enjoy all improvements you can switch to this new version via:
**`git remote update && git checkout v5.8`**

If you are new to Paparazzi and want to join in flying with it, you can you can simply download a [tarball](https://github.com/paparazzi/paparazzi/releases/download/v5.6.0_stable/paparazzi_v5.6.0_stable.tar.gz) or get the source code via:

**`git clone https://github.com/paparazzi/paparazzi.git -b v5.8`**
