#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2023.09.17                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   NOTES:       `type` is the string name to describe the area's type                                                 #
#                `area` is the instance of the area.                                                                   #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import Routes.Root
import Routes.Curtain


import asyncio
from datetime import datetime, timedelta
from flask import redirect, render_template, request
import httpx


from Global import BACKEND_DOMAIN


def GET(type: str) -> callable:
	crumbs = {"curtain": ["home", "room", "curtain"], "room": ["home", "room"], "home": ["home"]}[type]
	subtype = {"curtain": None, "room": "Curtain", "home": "Room"}[type]

	async def callback(area_id: int):
		async with httpx.AsyncClient() as client:
			area_request = client.get(f"{BACKEND_DOMAIN}/{type}s/{area_id}")
			structure_request = client.get(f"{BACKEND_DOMAIN}/{type}s/{area_id}/structure")
			area_response, structure_response = await asyncio.gather(area_request, structure_request)

		area = area_response.json()
		area["Events"] = area[f"{type.title()}Events"]
		subareas = area.get(f"{subtype}s")

		structure = {type: area, **structure_response.json()}
		path = [{"name": structure[area]["name"], "url": f"""/{area}s/{structure[area]["id"]}"""} for area in crumbs]

		arguments = {"area": area, "type": type, "path": path, "subareas": subareas, "subtype": subtype}
		return render_template("Area/Index.j2", datetime=datetime, **arguments)

	return callback


def POST(type: str) -> callable:
	async def callback(area_id: int):
		percentage_range = request.form["AreaEvent.New.Modal-percentage_range-input"]
		default_time = (datetime.now() + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
		event = {"percentage": int(percentage_range), "option": None, "time": default_time}
		if("AreaEvent.New.Modal-select_time-checkbox" in request.form):
			datetime_input = request.form["AreaEvent.New.Modal-datetime-input"]
			datetime.strptime(datetime_input, "%Y-%m-%dT%H:%M")
			event["time"] = f"""{datetime_input.replace("T", " ")}:00"""

		async with httpx.AsyncClient() as client:
			event_response = await client.post(f"{BACKEND_DOMAIN}/{type}s/{area_id}/events", json=event)

		event = event_response.json()
		return redirect(f"/{type}s/{area_id}")

	return callback


def GET_event(type: str) -> callable:
	crumbs = {"curtain": ["home", "room", "curtain"], "room": ["home", "room"], "home": ["home"]}[type]

	async def callback(area_id: int, event_id: int):
		async with httpx.AsyncClient() as client:
			event_request = client.get(f"{BACKEND_DOMAIN}/{type}s/{area_id}/events/{event_id}")
			structure_request = client.get(f"{BACKEND_DOMAIN}/{type}s/{area_id}/structure")
			event_response, structure_response = await asyncio.gather(event_request, structure_request)

		event = event_response.json()
		event["time"] = event["time"][:16].replace(" ", "T")

		structure = structure_response.json()
		path = [{"name": structure[area]["name"], "url": f"""/{area}s/{structure[area]["id"]}"""} for area in crumbs]
		path.append({"name": f"""Event #{event["id"]}""", "url": f""})

		return render_template("Area/EditEvent.j2", event=event, path=path)

	return callback


def POST_event(type: str) -> callable:
	crumbs = {"curtain": ["home", "room", "curtain"], "room": ["home", "room"], "home": ["home"]}[type]

	async def callback(area_id: int, event_id: int):
		percentage_range = request.form["AreaEvent.New.Modal-percentage_range-input"]
		event = {"percentage": int(percentage_range), "option": None}
		datetime_input = request.form["AreaEvent.New.Modal-datetime-input"]
		datetime.strptime(datetime_input, "%Y-%m-%dT%H:%M")
		event["time"] = f"""{datetime_input.replace("T", " ")}:00"""

		async with httpx.AsyncClient() as client:
			event_response = await client.patch(f"{BACKEND_DOMAIN}/{type}s/{area_id}/events/{event_id}", json=event)

		event = event_response.json()
		return redirect(f"/{type}/{area_id}/events/{event_id}")

	return callback
