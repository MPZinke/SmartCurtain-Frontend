

import asyncio
from datetime import datetime
from flask import render_template, session
import httpx


from Global import BACKEND_DOMAIN


async def GET(room_id: int):
	async with httpx.AsyncClient() as client:
		room_request = client.get(f"{BACKEND_DOMAIN}/rooms/{room_id}")
		structure_request = client.get(f"{BACKEND_DOMAIN}/rooms/{room_id}/structure")
		room_response, structure_response = await asyncio.gather(room_request, structure_request)

	room = room_response.json()
	structure = structure_response.json()
	print(structure)
	path = [structure["home"], structure["room"]]
	return render_template("Room/Index.j2", datetime=datetime, room=room, path=path)
