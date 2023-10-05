

import asyncio
from datetime import datetime, timedelta
from flask import redirect, render_template, request, session
import httpx


from Global import BACKEND_DOMAIN


async def GET(curtain_id: int):
	async with httpx.AsyncClient() as client:
		curtain_request = client.get(f"{BACKEND_DOMAIN}/curtains/{curtain_id}")
		structure_request = client.get(f"{BACKEND_DOMAIN}/curtains/{curtain_id}/structure")
		curtain_response, structure_response = await asyncio.gather(curtain_request, structure_request)

	curtain = curtain_response.json()

	structure = structure_response.json()
	path = [{"name": curtain["name"], "url": f"""/curtains/{curtain["id"]}"""}]
	for area in ["room", "home"]:
		path.insert(0, {"name": structure[area]["name"], "url": f"""/{area}s/{structure[area]["id"]}"""})

	return render_template("Curtain/Index.j2", curtain=curtain, datetime=datetime, path=path)


async def POST(curtain_id: int):
	percentage_range = request.form["AreaEvent.New.Modal-percentage_range-input"]
	default_time = (datetime.now() + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
	event = {"percentage": int(percentage_range), "option": None, "time": default_time}
	print(request.form)
	if("AreaEvent.New.Modal-select_time-checkbox" in request.form):
		datetime_input = request.form["AreaEvent.New.Modal-datetime-input"]
		datetime.strptime(datetime_input, "%Y-%m-%dT%H:%M")
		datetime_input = f"""{datetime_input.replace("T", " ")}:00"""

	async with httpx.AsyncClient() as client:
		curtain_response = await client.post(f"{BACKEND_DOMAIN}/curtains/{curtain_id}/events", json=event)

	curtain = curtain_response.json()
	print(curtain)
	return redirect(f"/curtains/{curtain_id}")


async def GET_curtain_id_event_id(curtain_id: int, event_id: int):
	async with httpx.AsyncClient() as client:
		curtain_request = client.get(f"{BACKEND_DOMAIN}/curtains/{curtain_id}")
		structure_request = client.get(f"{BACKEND_DOMAIN}/curtains/{curtain_id}/structure")
		curtain_response, structure_response = await asyncio.gather(curtain_request, structure_request)

	curtain = curtain_response.json()
	event = curtain["CurtainEvents"][0]
	event["time"] = event["time"][:16].replace(" ", "T")

	structure = structure_response.json()
	path = [{"name": f"""Event #{event["id"]}""", "url": f"""/curtains/{curtain["id"]}/events/{event["id"]}"""}]
	for area in ["curtain", "room", "home"]:
		path.insert(0, {"name": structure[area]["name"], "url": f"""/{area}s/{structure[area]["id"]}"""})

	return render_template("Curtain/EditEvent.j2", event=event, path=path)


# `/curtains/events/{{ event["id"] }}/delete`
async def DELETE(curtain_id: int, event_id: int):
	async with httpx.AsyncClient() as client:
		curtain_response = await client.delete(f"{BACKEND_DOMAIN}/curtains/{curtain_id}/events/{event_id}")

	curtain = curtain_response.json()
	print(curtain)
	curtain_id =  curtain["id"]
	return redirect(f"/curtains/{curtain_id}")
