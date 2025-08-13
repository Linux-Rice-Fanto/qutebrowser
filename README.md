# Qutebrowser

The most minimalist browser VIM intuitive ever created.

## Configuration

- Install qutebrowser with the following command:

```bash
sudo pacman -S qutebrowser
```

- Add this repository in `~/.config/` if there is an already created, delete that one and put this repo.
- All the configuration are in the file `config.py`

## Keymaps


### My special configuration

| Keymap | Description |
|---|---|
| X + B | Hide/Show the status bar|
| X + T | Hide/Show the tabs |


### Basic Navigation

| Keymap | Description |
|---|---|
| O | Open an URL into the actual tab
| Shift + T | Open an URL in a new tab (from history)
| Shift + H | Go back one page
| Shift + L | Advance one page
| Shift + J | Change to next tab
| Shift + K | Change to previous tab
| D | Close current tab
| U | Reopen last tab
| g0 | Go to the first tab
| g$ | Go to the last tab
| Alt + number | Go to tab by the number

### Page interaction

| Keymap | Description |
|---|---|
| F | Activate hint mode (click on links from the keyboard)
| Shift + F | Open the link into a new tab
| Y + Y | Copy the URL from the current tab
| Shift + P | Paste the URL into a new tab
| P | Paste the URL into the current tab
| R | Reload the page
| G + G | Go to the top of the page
| Shift + G | Go to the end of the page
| / | Start a search in the current page

### Qutebrowser commands

| Keymap | Description |
|---|---|
| :q | Quit Qutebrowser
| :wq | Save session and quit
| :help | Open complete documentation
| :config-source | Relad the config.py file to see changes into qutebrowser
