# Best of Hermes

A Hermes Agent skill for keeping up with a hand-picked list of Hermes Agent projects. Tell your Hermes:

> show me the best of Hermes

It shows you each project with a one-line description and a link, you pick the ones you like, and
only then does it star them and follow the builders from your own GitHub account. Nothing happens
without your yes. When projects are added, the next run shows only the new ones.

The list is in [list.md](list.md).

## Install

Ask your Hermes to install it for you:

> install the skill from github.com/LocutusOfTheEye/bestofhermes

Or do it yourself:

```bash
git clone https://github.com/LocutusOfTheEye/bestofhermes ~/.hermes/skills/bestofhermes
```

On Windows (PowerShell):

```powershell
git clone https://github.com/LocutusOfTheEye/bestofhermes "$env:USERPROFILE\.hermes\skills\bestofhermes"
```

Already have it? Update to the latest version:

```bash
git -C ~/.hermes/skills/bestofhermes pull
```

The first time you use it, Hermes checks that Python and the GitHub CLI are installed and walks you
through signing in to GitHub in your browser.

## Good to know

- Preview first, every time. It only acts after you approve.
- Look before you star: each project is shown with its description and link, and only the ones you
  pick get a star. In a terminal, `--review` walks through them one at a time (o opens it in your
  browser). Anything you skip comes back next time.
- Skips your own repos and anything you already starred or follow.
- Paced (a few seconds between actions, with a little random time) and logged.
- Reads the latest list from this repo, with a copy included as a backup.
- Stars are voluntary: star what you actually like.

## License

MIT
