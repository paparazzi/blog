{
  "title": "Secure Pprzlink released",
  "date": "2018-03-26T19:26:27Z",
  "url": "/2018/03/26/secure-pprzlink-released/",
  "author": "Michal Podhradsky",
  "wordpress_id": 1311,
  "categories": [
    "Release",
    "Software"
  ],
  "tags": []
}

The Paparazzi team is proud to announce a release of an encrypted version of [pprzlink](https://github.com/paparazzi/pprzlink). The new **secure Pprzlink** uses a strong and fast cipher [ChaCha20](https://en.wikipedia.org/wiki/Salsa20#ChaCha20_adoption) with [Poly1305](https://en.wikipedia.org/wiki/Poly1305) authenticator. For better security and user convenience, a variation of [station-to-station](https://en.wikipedia.org/wiki/Station-to-Station_protocol) key-exchange protocol is implemented, to allow seamless key-exchange between the UAV and the GCS.

**Secure Pprzlink** is backed by a formally verified cryptographic library [HACL\*](https://github.com/mitls/hacl-star)  (yes, the same library that is a part of new Mozilla Firefox).

**Why should you care?** Without encryption, anyone can listen to your drone communication, and can potentially send modified or outright “fake” commands to it, steering it of course, or causing it to crash. Using encrypted radio link is similar to using encrypted connection on internet, and should be a common practice.

**Why is using a formally verified crypto library important?** In short, cryptography is hard to do right, and formal methods help make sure that the encryption algorithms behave as intended. The short video below gives you a better idea:

<iframe src="https://www.youtube-nocookie.com/embed/8_4kG8SEusg" title="YouTube video" loading="lazy" allowfullscreen></iframe>

**Secure Pprzlink** uses a formally verified cryptography library, but is not verified itself. However, it could be verified in the future, to provide additional guarantees.

**How to use it?** We prepared a [wiki page](https://wiki.paparazziuav.org/wiki/Pprzlink#Secure_Ppprzlink) with instructions and examples. In short, choose a secure link as your mode of communication when building the autopilot code, and the rest is handled automatically. Also, the GCS part of **secure pprzlink** is written in [Rust](https://www.rust-lang.org/en-US/), which is a memory-safe language, which guarantees that the code written in Rust is itself memory-safe and thus eliminates a large amount of possible software bugs.

**Secure Pprzlink** was created with the help of [Galois](https://galois.com/), [Senman](https://senman.cz/) and is currently used by [AggieAir](http://aggieair.usu.edu/index) at Utah State University.

Give it a try and give us any feedback and ask questions on paparazzi gitter [channel](https://gitter.im/paparazzi/discuss), or via paparazzi [mailing list](http://lists.paparazziuav.org/).

Wishing everyone happy (and secure) flying!
