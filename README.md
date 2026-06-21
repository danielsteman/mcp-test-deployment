# dummy-mcp-server

A minimal [FastMCP](https://github.com/jlowin/fastmcp) server used to test
deployments on [mcphost.eu](https://mcphost.eu). It exposes a few trivial tools
over the streamable HTTP transport.

## Run locally

```bash
uv sync
uv run server.py
```

The server binds to `0.0.0.0` on `$MCP_PORT` (default `8000`) and serves MCP at
`/mcp/`.

## Deploying with mcphost.eu

This repo is deploy-ready: `mcphost.yaml` in the root declares the entrypoint,
Python version, and port. The platform builds the image with `uv` and injects
`MCP_PORT` (the port to bind) and `PROJECT_SLUG` at container start; project
secrets arrive as additional environment variables.

## Tools

- `add(a, b)` — add two integers
- `echo(message)` — return the message unchanged
- `whoami()` — report the deployment's slug (confirms which server answered)
