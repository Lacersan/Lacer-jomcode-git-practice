import httpx #Open a special toolbox "httpx" that contains the tools needed to talk to the web servers.

response = httpx.Response(201, json={"id": "w1", "capacity": 20})
print(response.status_code)
print(response.json()["id"])
