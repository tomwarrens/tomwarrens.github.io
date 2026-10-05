# tomwarrens.github.io

Hugo + PaperMod site, deployed to GitHub Pages on every push to `main`.

## Updating Substack posts

Substack blocks GitHub Actions, so the "Latest writing" section and `/writing/`
read from `data/substack.json`. After publishing a post, run:

```sh
python3 scripts/update_substack.py --push
```

It refreshes the file from the RSS feed and, if there are new posts, commits and
pushes it (on `main`, that deploys the site). Drop `--push` to only update the file.
