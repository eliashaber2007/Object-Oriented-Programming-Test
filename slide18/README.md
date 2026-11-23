# Slide 18: Shell and bash scripting

## Part 1: Improve your shell experience

**Which shell am I using?**

```bash
echo $0        # the shell currently running
echo $SHELL    # my login shell
```

On my Mac both give `/bin/zsh` (default shell on modern macOS).

**Step 1.2: Oh My Zsh.** Since my shell is zsh, I installed Oh My Zsh and picked a theme in `~/.zshrc` (`ZSH_THEME="..."`).

**What's the purpose of the `source` command?** `source ~/.zshrc` runs the file inside the current shell, so changes to the config (theme, plugins, aliases) apply right away without opening a new terminal.

**Step 1.3: Git plugin.** In `~/.zshrc`, add git to the plugins list: `plugins=(git)`, then `source ~/.zshrc`. Now `gst` works like `git status` (other aliases: `glog`, `gp` for push, `gl` for pull).

## Part 2: Check Python

```bash
python3 --version
```

Always use `python3` explicitly, since some systems still have Python 2 behind `python`.

## Part 3: The script

`env_install.sh` sets up the environment automatically:

1. `pretty_print` function (uses `printf`, blank lines before and after, colors for success, warnings and errors)
2. OS detection with `$OSTYPE` (macOS or Linux)
3. Installs `python3` if it's missing, otherwise shows the version
4. Checks that `pip` works
5. Installs Jupyter Notebook (Homebrew on macOS, pip on Linux)
6. On macOS, runs `brew doctor`

Bonus done: colored output and strict mode (`set -euo pipefail`).

## Part 4: Run it

```bash
chmod +x env_install.sh
./env_install.sh
```

Checklist:

- [x] Shell prompt shows the Oh My Zsh theme
- [x] `gst` works like `git status`
- [x] `python3 --version` returns 3.x
- [x] `pip --version` shows the version
- [x] `jupyter notebook` launches
- [x] `brew doctor` reports no serious issues
