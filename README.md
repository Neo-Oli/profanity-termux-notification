# profanity-termux-notification
Plugin for Profanity to to enable Android notifications on Termux

![Screenshot](screenshot.png)


## Requirements

You can install [Profanity](http://profanity.im) in [Termux](http://termux.com) with `apt update && apt install profanity`. You also need [Termux API](https://play.google.com/store/apps/details?id=com.termux.api) and the termux-api package (`apt install termux-api`). 


## Installation

1. Download the script

2. Launch Profanity

3. Install the plugin with the following command.

```
/plugins install ~/profanity-termux-notification/termuxnotify.py

```

## Configuration

### Turn the plugin on

`/termuxnotify on`

### Turn the plugin off

`/termuxnotify off`

### Only notify for the currently active window

`/termuxnotify active`

### Enable/Disable notifications for all messages in rooms

`/termuxnotify rooms on|off`

### Enable/Disable vibration

`/termuxnotify vibrate on/off`

