from fastmcp import FastMCP

mcp = FastMCP("server")

@mcp.tool
def mcp_tool(parmas: str) -> list[dict]:
    pass



if __name__ == "__main__":
    mcp.run(host="0.0.0.0", port=3000, transport='http')