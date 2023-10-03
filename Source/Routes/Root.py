#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2020.12.23                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import asyncio
from datetime import datetime
from flask import render_template, session
import httpx


from Global import BACKEND_DOMAIN


# —————————————————————————————————————————————————————— ROUTES —————————————————————————————————————————————————————— #

async def GET():
	async with httpx.AsyncClient() as client:
		homes = (await client.get(f"{BACKEND_DOMAIN}/homes")).json()
		print(homes)
	return render_template("Index.j2", datetime=datetime, homes=homes, path="")


def favicon():
	return ""
