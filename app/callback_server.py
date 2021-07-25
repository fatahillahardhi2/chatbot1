from sanic import Sanic, response
from sanic.request import Request
from sanic.response import HTTPResponse


def create_app() -> Sanic:

    bot_app = Sanic(__name__, configure_logging=False)

    @bot_app.post("/bot")
    def print_response(request: Request) -> HTTPResponse:
        """Print bot response to the console."""
        botResponse = request.json.get("text")
        print(f"\n{botResponse}")

        body = {"status": "message sent"}

        return response.json(botResponse, status=200)

    return bot_app


if __name__ == "__main__":
    app = create_app()
    port = 5034

    print(f"Starting callback server on port {port}.")
    app.run("0.0.0.0", port)