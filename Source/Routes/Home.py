

import asyncio
from datetime import datetime
from flask import render_template, session
import httpx


from Global import BACKEND_DOMAIN


async def GET(home_id: int):
	async with httpx.AsyncClient() as client:
		home = (await client.get(f"{BACKEND_DOMAIN}/homes/{home_id}")).json()

	path = [{"name": home["name"], "url": f"""/homes/{home["id"]}"""}]

	return render_template("Home/Index.j2", datetime=datetime, home=home, path=path)
