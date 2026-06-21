"""Dummy FastMCP server for exercising mcphost.eu deployments.

Exposes a few trivial tools over the streamable HTTP transport. The platform
injects MCP_PORT (the port to bind) and PROJECT_SLUG at container start; any
project secrets are injected as additional environment variables.
"""

import os

from fastmcp import FastMCP

mcp = FastMCP("dummy-mcp-server")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@mcp.tool
def echo(message: str) -> str:
    """Return the given message unchanged."""
    return message


@mcp.tool
def whoami() -> dict[str, str]:
    """Report the deployment's slug, to confirm which server answered."""
    return {"slug": os.environ.get("PROJECT_SLUG", "unknown")}


def main() -> None:
    port = int(os.environ.get("MCP_PORT", "8000"))
    mcp.run(transport="http", host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
