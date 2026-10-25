{
  "title": "Paparazzi v5.18 is out, v6.0 is starting",
  "date": "2021-04-13T11:47:01Z",
  "url": "/2021/04/13/paparazzi-v5-18-is-out-v6-0-is-starting/",
  "author": "Gautier Hattenberger",
  "wordpress_id": 1385,
  "categories": [
    "Release"
  ],
  "tags": []
}

The latest Paparazzi stable release is out today with many changes and addition since 5.16 one year ago. One of the biggest changes is the complete rewrite of the build system for the aircraft code generation (good old Ocaml stuff), plus the addition of a proper dependency resolution for the modules. It has no big impact for users so far, but in order to move forward, we will most likely break a few things...

Hence, 5.18 will be the last of the series 5. The main branch is now labeled with 6.0\_unstable and will start by a big cleaning. Most noticeable one is that the boards and tools based on lpc21 and stm32 bare-metal (using libopencm3) will be dropped. So the only supported architectures will be Linux for simulation and Parrot drones and ChibiOS for micro-controllers.

More in-depth changes will also come, including better usage of the new dependency mechanism, rearrangement of the static scheduling of the autopilot, and if possible a new set of messages for pprzlink (lot's of cleaning here as well...).

The complete changelog and release package are available at <https://github.com/paparazzi/paparazzi/releases/tag/v5.18.0_stable>
