

import mpzinke
import os
import pathlib


import Routes


FRONTEND_DIRECTORY = str(pathlib.Path(__file__).parent)
TEMPLATE_DIRECTORY = os.path.join(FRONTEND_DIRECTORY, "HTML", "Templates")
STATIC_DIRECTORY = os.path.join(FRONTEND_DIRECTORY, "HTML", "Static")
print(STATIC_DIRECTORY)


def random_keygen(length):
	from random import randint
	ascii_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|" \
	  + "}~ \t\n\r\x0b\x0c"
	return "".join([ascii_chars[randint(0, len(ascii_chars)-1)] for x in range(length)])


def main():
	server = mpzinke.Server(name="SmartCurtain-Frontend", debug=True,
		template_folder=TEMPLATE_DIRECTORY, static_folder=STATIC_DIRECTORY
	)

	server._app.secret_key = random_keygen(64)
	server.route("/", Routes.Root.GET)
	server.route("/homes", Routes.Root.GET)
	server.route("/homes/<int:home_id>", GET=Routes.Home.GET)
	server.route("/rooms/<int:room_id>", GET=Routes.Room.GET)
	server.route("/curtains/<int:curtain_id>", GET=Routes.Curtain.GET, POST=Routes.Curtain.POST)

	server(port=80)


if(__name__ == "__main__"):
	main()