"""
Display recieved messages as an Android Notification on Termux
"""

import prof
import os
import time
from sys import platform

def termuxnotify(sender,message):
	vibrate = prof.settings_string_get("termuxnotify", "vibrate", "off")
	os.system("termux-notification -t 'Profanity: {} says:' -c '{}'".format(sender,message))
	if vibrate == "on":
		os.system("termux-vibrate -d 400")
		time.sleep(0.3)
		os.system("termux-vibrate -d 400")


def prof_post_chat_message_display(barejid, resource, message):
	enabled = prof.settings_string_get("termuxnotify", "enabled", "on")
	current_recipient = prof.get_current_recipient()
	if enabled == "on" or (enabled == "active" and current_recipient == barejid):
		termuxnotify(barejid, message)

	return message


def prof_post_room_message_display(barejid, nick, message):
	enabled = prof.settings_string_get("termuxnotify", "enabled", "on")
	rooms = prof.settings_string_get("termuxnotify", "rooms", "off")
	current_muc = prof.get_current_muc()
	if rooms == "on":
		if enabled == "on":
			termuxnotify(nick + " in " + barejid, message)
		elif enabled == "active" and current_muc == barejid:
			termuxnotify(nick, message)

	return message


def prof_post_priv_message_display(barejid, nick, message):
	if enabled:
		termuxnotify(nick,message)

	return message


def _cmd_say(arg1=None, arg2=None):
	if arg1 == "on":
		prof.settings_string_set("termuxnotify", "enabled", "on")
		prof.cons_show("Termuxnotify plugin enabled")
	elif arg1 == "off":
		prof.settings_string_set("termuxnotify", "enabled", "off")
		prof.cons_show("Termuxnotify plugin disabled")
	elif arg1 == "active":
		prof.settings_string_set("termuxnotify", "enabled", "active")
		prof.cons_show("Termuxnotify plugin enabled for active window only")
	elif arg1 == "vibrate":
		if arg2 == None:
			prof.cons_bad_cmd_usage("/termuxnotify")
		else:
			prof.settings_string_set("termuxnotify", "vibrate", arg2)
			prof.cons_show("termuxnotify plugin vibrate set to: " + arg2)
	elif arg1 == "rooms":
		if arg2 == None:
			prof.cons_bad_cmd_usage("/termuxnotify")
		else:
			prof.settings_string_set("termuxnotify", "rooms", arg2)
			prof.cons_show("termuxnotify plugin notifications for rooms set to: " + arg2)
	else:
		enabled = prof.settings_string_get("termuxnotify", "enabled", "on")
		rooms = prof.settings_string_get("termuxnotify", "rooms", "off")
		vibrate = prof.settings_string_get("termuxnotify", "vibrate", "off")
		prof.cons_show("Termuxnotify plugin settings:")
		prof.cons_show("enabled : " + enabled)
		prof.cons_show("vibrate : " + vibrate)
		prof.cons_show("rooms : " + rooms)

def prof_init(version, status, account_name, fulljid):
	synopsis = [
		"/termuxnotify on|off|active",
		"/termuxnotify vibrate on|off",
		"/termuxnotify rooms on|off"
	]
	description = "Read messages out loud"
	args = [
		[ "on|off",		 "Enable/disable termuxnotify for all windows" ],
		[ "active",		 "Enable termuxnotify for active window only" ],
		[ "vibrate <args>",    "Turn vibrate on or off" ],
		[ "rooms <args>",    "Turn notifications for rooms on or off" ]
	]
	examples = []

	prof.register_command("/termuxnotify", 0, 2, synopsis, description, args, examples, _cmd_say)
	prof.completer_add("/termuxnotify", [ "on", "off","active","vibrate","rooms" ])
	prof.completer_add("/termuxnotify vibrate", [ "on", "off" ])
	prof.completer_add("/termuxnotify rooms", [ "on", "off" ])
