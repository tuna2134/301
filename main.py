from sanic import Sanic, response

from os import getenv


app = Sanic("301")


@app.get("/")
async def main(request):
    return response.redirect("https://knowledge.rext.dev")

app.run("0.0.0.0", int(getenv("PORT")))
