

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
	server.route("/homes/<string:area_id>", GET=Routes.GET("home"), POST=Routes.POST("home"))
	server.route("/rooms/<string:area_id>", GET=Routes.GET("room"), POST=Routes.POST("room"))
	server.route("/curtains/<string:area_id>", GET=Routes.GET("curtain"), POST=Routes.POST("curtain"))
	server.route("/curtains/<string:area_id>/events/<int:event_id>/edit", GET=Routes.GET_event("curtain"),
		POST=Routes.POST_event("curtain")
	)

	server(port=80)


if(__name__ == "__main__"):
	main()
