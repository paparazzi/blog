{
  "title": "Circle formations of fixed-wing aircraft",
  "date": "2017-02-21T10:18:59Z",
  "url": "/2017/02/21/circle-formations-of-fixed-wings/",
  "author": "Hector Garcia de Marina",
  "wordpress_id": 1269,
  "categories": [
    "Research",
    "Videos"
  ],
  "tags": []
}

We have recently developed and tested a formation control algorithm for fixed-wing aircraft in Paparazzi at ENAC. The position of an arbitrary number of vehicles can be controlled in a circular path. In fact, we are not restricting ourselves to circles but to any closed orbit, such as ellipses, thanks to the [guidance vector field](https://wiki.paparazziuav.org/wiki/Module/guidance_vector_field) that guides the planes.
The algorithm is under more tests, but it should be soon available for the general public. It is quite easy to employ, the user has to declare only the IDs of the planes, the communication topology (neighbors' relationships) and the desired inter-angles. A detailed explanation will be posted soon in the wiki.
In the following video the planes exchange positions every second. Delays, out-of-date positions (GPS delays), packet losses, etc are expected to be (and actually they are) present. It is quite interesting to remark how robust the algorithm is. According to our calculations the impact of such nasty things are not very important (ofc up to a certain point) for the convergence of the algorithm.

<iframe src="https://www.youtube-nocookie.com/embed/q4b8JRU1Gbw" title="YouTube video" loading="lazy" allowfullscreen></iframe>
