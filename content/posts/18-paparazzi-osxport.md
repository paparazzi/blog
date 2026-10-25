{
  "title": "Paparazzi support on Mac OSX: Progress report.",
  "date": "2010-12-01T00:46:07Z",
  "url": "/2010/12/01/paparazzi-osxport/",
  "author": "Eric Parsonage",
  "wordpress_id": 18,
  "categories": [
    "Software"
  ],
  "tags": [
    "cross platform",
    "ground software",
    "mac os x",
    "paparazzi",
    "portability",
    "software"
  ],
  "archived_comments": [
    {
      "author": "esden",
      "date": "2010-12-29 22:29:18",
      "text": "Hi!\nNo we did not run out of topics, we just run out of time. Most of us are busy with attending christmas related events. Felix and me are at the 27C3 at the moment. There will definitely be a new blog post soon. So no worries. The blog will continue very soon! :)\nCheers Esden"
    },
    {
      "author": "Interested",
      "date": "2010-12-29 20:13:24",
      "text": "Its the end of the month.... Did you guys run into issues? Can't wait to see this... Really want to play with it"
    },
    {
      "author": "Chetan",
      "date": "2011-01-31 08:17:10",
      "text": "It's working properly after a long installation but, when I click on edit button in Paparazzi Center window, it doesn't open any editor... Any Solutions??"
    },
    {
      "author": "lamestllama",
      "date": "2011-02-11 07:08:44",
      "text": "You need to export a variable EDITOR which points to the editor you wish to use."
    }
  ]
}

This is a brief note to keep everyone updated on progress towards supporting [Paparazzi on OSX](http://wiki.paparazziuav.org/wiki/Installation/MacOSX). Currently [Paparazzi](http://wiki.paparazziuav.org/wiki/Main_Page "Paparazzi Homepage") is supported only on Linux. With the growing base of Paparazzi developers it has become possible for us to consider supporting multiple operating systems.

Mac OSX was chosen for attention ahead of Windows 7 due to the its similarity to Linux. We hope that the experience gained in supporting this operating system will give an indication of what form a combined build system for all three platforms will take.

[![](/wp-content/uploads/2010/11/paparazzicenter-300x187.jpg "Paparazzi Center")](/wp-content/uploads/2010/11/paparazzicenter.jpg) Paparazzi Center on OSX

The GUI used by the Paparazzi ground segment is based on GTK, this provides a transparent way of building X Windows based applications for OSX. To date all the components of the ground segment have been built in this way and function as intended. Unfortunately this currently requires hand building some packages, attention is now being given to simplifying the process by wherever possible submitting patches to the package maintainers.

[![](/wp-content/uploads/2010/11/gcs_x-300x187.jpg "Paparazzi Ground Control Station running live on OSX")](/wp-content/uploads/2010/11/gcs_x.jpg) Paparazzi Ground Control Station running live on OSX

Once the machinery is in place for [installing Paparazzi on OSX](http://wiki.paparazziuav.org/wiki/Installation/MacOSX) without hand building some packages, only a few extra changes will be required to produce a version that uses the gtk-quartz-engines. This will then provide the look and feel of a native OSX application.

A number of interesting facts have surfaced during this process.

The first is that the Paparazzi development team have over the years have been very careful to adhere to the Posix standard. This has meant that very few code changes have been required to make Paparazzi run on OSX. This portability is something the team should be very proud of.

The second is the amazing depth of talent in the Paparazzi development team. I provide only one example of this but there are many more. A central component required in the ground segment is the build system used by Paparazzi to create firmware for the autopilot. This consists of a cross compiler and related utilities. In this case [Esden](http://www.esden.net/blog/ "Esden's Blog") had already done much of the work required to produce such a toolchain with his [summon-arm-toolchain](https://github.com/esden/summon-arm-toolchain) script. Thanks to that with only a few "clicks" we ended up with a toolchain that we could use for both of our arm targets, lpc21 and stm32.

It is expected that [instructions for installing Paparazzi on OSX](http://wiki.paparazziuav.org/wiki/Installation/MacOSX) with X Windows will be posted at the official [Paparazzi wiki](http://wiki.paparazziuav.org/wiki/Main_Page) in the very near future. With a non X Windows version following in the coming weeks.

And until next time... your Paparazzi team.
