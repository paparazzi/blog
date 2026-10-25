{
  "title": "Flying Robot Commander + PPRZLINK = Improved MultiMAV Management",
  "date": "2016-04-11T06:21:31Z",
  "url": "/2016/04/11/flying-robot-commander-pprzlink-improved-multimav-management/",
  "author": "Rich Burton",
  "wordpress_id": 1181,
  "categories": [
    "Community",
    "Release",
    "Software"
  ],
  "tags": []
}

For those of us that use Paparazzi to fly multiple MAVs, the current [GCS](http://wiki.paparazziuav.org/wiki/GCS) does a great job of managing and presenting just the right amount of information for safe flight. That being said, there's always room for new tools. It's my pleasure to introduce the [Flying Robot Commander](https://github.com/paparazzi/flyingrobotcommander), a [PPRZLINK](https://github.com/paparazzi/pprzlink) enabled web application for managing multiple MAVs.

The [Flying Robot Commander](https://github.com/paparazzi/flyingrobotcommander)(FRC) is a Flask/python based RESTful web application that integrates with [Paparazzi UAV](https://github.com/paparazzi/paparazzi) via [PPRZLINK](https://github.com/paparazzi/pprzlink). That's right, you can now write python code to access/extend Paparazzi UAV capabilities (NOTE: one of the main complaints about the current Paparazzi GCS is that it's written in ocaml). In addition to python, PPRZLINK also provides C and ocaml libraries for those that need them.

For more details related to the Flying Robot Commander, PPRZLINK and Paparazzi UAV in general, see the following links:

- [Flying Robot Commander Github](https://github.com/paparazzi/flyingrobotcommander)
- [PPRZLINK Github](https://github.com/paparazzi/pprzlink)
- [Paparazzi Github](https://github.com/paparazzi/paparazzi)
- [Paparazzi Wiki](http://wiki.paparazziuav.org/wiki/Main_Page)
