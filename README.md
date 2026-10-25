# Paparazzi UAV Blog

Source for [docs.paparazziuav.org/blog/](https://docs.paparazziuav.org/blog/), built with Hugo.

## Requirements

Install [Hugo](https://gohugo.io/installation/) **0.168.0**, the version used by GitHub Actions. Run commands below from the repository root. If you have a local binary in `.tools/`, use `.tools/hugo` instead of `hugo`.

## Add an article

Create a Markdown file in `content/posts/`, for example `content/posts/new-flight-tests.md`:

```markdown
+++
title = "New flight tests"
date = 2026-10-25T14:00:00+01:00
author = "Your name"
categories = ["Research"]
tags = ["Flight tests"]
url = "/2026/10/25/new-flight-tests/"
draft = true
+++

Write your introduction here.

## Results

Describe the results here.

![Aircraft during testing](/images/new-flight-tests/aircraft.jpg)
```

Replace the example title, date, author, and URL. Use a unique URL with the article's publication date and slug. Articles appear automatically on the homepage, in the archives, and in the sidebar, ordered by date.

For the example image, save the file as `static/images/new-flight-tests/aircraft.jpg`. Files under `static/` are served from the site root, so omit `static` from image URLs.

## Preview locally

Start the preview server, including drafts:

```sh
hugo server -D --bind 127.0.0.1 --baseURL http://localhost:1313/
```

Open **http://localhost:1313/**. The preview refreshes automatically when you edit files. Press **Ctrl+C** to stop it. Add `--buildFuture` to preview articles with future publication dates.

Alternatively, build and serve with Python:

```sh
hugo --minify --destination dist --baseURL http://localhost:1313/
python3 -m http.server 1313 --bind 127.0.0.1 --directory dist
```

This alternative excludes drafts and requires rebuilding after edits, then refreshing the browser.

## Publish

Set `draft = false` when the article is ready, and ensure its publication date is not in the future. Commit the article and any new images, then push to `main`. GitHub Actions builds and deploys the site to GitHub Pages automatically; check the repository's **Actions** tab for progress.
