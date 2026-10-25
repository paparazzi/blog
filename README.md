# Paparazzi UAV Blog — Hugo migration

This is a local migration. The live WordPress site has not been changed.

## Preview

Hugo 0.168.0 is downloaded locally in `.tools/` (Linux amd64).

```sh
.tools/hugo server --bind 127.0.0.1 --baseURL http://localhost:1313/
```

Open http://localhost:1313/. To build for production:

```sh
.tools/hugo --minify
```

Upload the contents of `public/` to a static web server. PHP and a database are not required. Keep the original WordPress backup separately until the migration is accepted. No deployment has been performed.

## GitHub Pages deployment

The workflow in `.github/workflows/pages.yml` builds with Hugo **0.168.0** and deploys on every push to **main**. It can also be started manually from the Actions tab. It uses GitHub's built-in token; no personal access token or deployment secret is needed.

1. Create your GitHub repository and push this source tree on `main`.
2. In **Settings → Pages → Build and deployment**, set **Source** to **GitHub Actions**.
3. Push a commit, or run **Deploy Hugo to GitHub Pages** from the Actions tab. If the first run happened before Pages was enabled, rerun it.
4. The deployment job and **Settings → Pages** show the published URL.

The workflow takes the base URL from GitHub Pages and rewrites root-relative navigation and media URLs. It supports both `https://OWNER.github.io/REPOSITORY/` and a custom domain. To keep `blog.paparazziuav.org`, configure it under **Settings → Pages → Custom domain**, follow GitHub's domain verification instructions, and update DNS when ready. The workflow does not change DNS or the live WordPress site. GitHub Pages does not support server-side redirect configuration; any old RSS redirect needs a separate solution.

Commit `content/`, `static/` (including the imported media), `layouts/`, `hugo.toml`, scripts, documentation, and `.github/`. The importer and Python dependencies are for migration checks only; Actions needs only Hugo. Generated `public/` and `dist/` directories, local tools, and original XML/tar exports are excluded by `.gitignore`.

To publish another article, add or edit a Markdown file under `content/posts/`, add images under `static/`, preview locally, then commit and push to `main`. The workflow rebuilds the complete site, including the sidebar.

## Content

153 published posts, the About page, categories, tags, original post/page URLs, original media paths, and 56 approved comments have been imported. Two drafts are excluded and remain in the original XML export. Authors use the display names from WordPress. Dates use WordPress UTC timestamps. YouTube embeds remain external video services.

Imported posts live in `content/posts/` as Markdown with JSON front matter. Edit those files directly. New posts can use normal Markdown and front matter containing `title`, `date`, `author`, `categories`, and `url`. Use an explicit URL to preserve the dated URL convention. Raw HTML rendering is enabled for historical embeds; review contributed HTML before publishing.

This site uses a small custom layout, not the original WordPress theme. The old search and comment submission forms have been replaced with browsing by archive/category and read-only archived comments. The existing home page pagination paths are retained; individual historical WordPress monthly/author archive URLs and attachment pages are not yet recreated. RSS is at `/feed.xml`; configure a permanent redirect from the old `/feed/` URL on the production server.

## Re-run the import

Re-running overwrites imported content files, so do this before making editorial changes, or back up those changes first. The original XML and tar archive are untouched.

```sh
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/import_wordpress.py
.tools/hugo --minify
.venv/bin/python scripts/verify_site.py
```

`migration-manifest.json` maps all 154 original post/page URLs to content files. `migration-report.json` records content counts and unsupported shortcodes. `link-report.json` lists missing local targets after a build.

## Known issue and checks before switching

`/wp-content/uploads/2011/01/27C3-desk.jpg` is referenced in the historical content, but is absent from the supplied archive and also returns HTTP 404 on the live site. Restore it from an older backup if available.

The build succeeds and all 154 imported post/page routes resolve. Local links and image references are checked; external links and video playback have not all been verified. Review representative posts (including galleries/videos), the design, and production redirects before switching the domain. Keep original exports private: they include drafts and comment metadata. `.gitignore` excludes the input XML/archive, tools, environment, and generated site.
