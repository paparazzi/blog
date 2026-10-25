{
  "title": "Stable Paparazzi Releases",
  "date": "2012-05-09T00:00:42Z",
  "url": "/2012/05/09/stable-paparazzi-releases/",
  "author": "Felix Ruess",
  "wordpress_id": 466,
  "categories": [
    "Release",
    "Software"
  ],
  "tags": []
}

**[![Git-Logo-2Color](/wp-content/uploads/2015/07/Git-Logo-2Color-300x125.png)](/wp-content/uploads/2015/07/Git-Logo-2Color.png)In order to improve the development workflow and provide stable releases we have changed our git branching model.**

**The branch "master" is now our development branch.**

- The "dev" branch was renamed to the release preparation branch "v3.9". Switch to this branch if you want stable code.
- "master" was reset to the previous "locm3" branch, where development will happen now with libopencm3 for the STM32 architecture.

Please see the [RepositoryStructure](http://wiki.paparazziuav.org/wiki/RepositoryStructure "RepositoryStructure") page for more details.

As soon as we are ready to release v4.0 there will be tarballs available if you don't want to use [Git](http://wiki.paparazziuav.org/wiki/Git "Git").
