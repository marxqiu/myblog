# My blog

This is the repository of my blog, powered by [Hugo](https://gohugo.io/) and themed by [Hugo-ht](https://github.com/hongtaoh/hugo-ht).

## Deploy to Cloudflare Pages

This site is deployed by GitHub Actions to Cloudflare Pages.

Required GitHub Actions secrets:

- `CLOUDFLARE_API_TOKEN`: a Cloudflare API token with `Cloudflare Pages:Edit` permission.
- `CLOUDFLARE_ACCOUNT_ID`: the Cloudflare account ID.

Optional GitHub Actions variables:

- `CLOUDFLARE_PROJECT_NAME`: Cloudflare Pages project name. Defaults to `myblog`.
- `SITE_BASE_URL`: production site URL. Defaults to `https://myblog.pages.dev/`.

When using a custom domain, add the domain in Cloudflare Pages first, then set `SITE_BASE_URL` to the final URL, for example `https://www.example.com/`.
