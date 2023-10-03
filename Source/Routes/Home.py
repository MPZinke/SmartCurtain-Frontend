

import asyncio
from datetime import datetime
from flask import render_template, session
import httpx


from Global import BACKEND_DOMAIN


async def GET(home_id: int):
	async with httpx.AsyncClient() as client:
		home = (await client.get(f"{BACKEND_DOMAIN}/homes/{home_id}")).json()
	print(home)
	path = [{"path": f"""/homes/{home["id"]}""", "name": home["name"]}]
	return render_template("Home/Index.j2", datetime=datetime, home=home, path=path)
