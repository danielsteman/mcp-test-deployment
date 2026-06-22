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
- `get_env(name)` — report whether an env var is set and its value (see below)

## Testing secret propagation

`get_env` exists to verify that project secrets configured in mcphost.eu are
propagated into the deployed container as environment variables:

1. In the mcphost.eu dashboard, add a secret to this project, e.g.
   `TEST_SECRET=hello`.
2. Deploy (or redeploy).
3. From an MCP client, call `get_env` with `name="TEST_SECRET"`. A correctly
   propagated secret returns `{"name": "TEST_SECRET", "set": true, "value": "hello"}`.

The platform also injects `MCP_PORT` and `PROJECT_SLUG`, so `get_env("PROJECT_SLUG")`
should always report the deployment slug.
