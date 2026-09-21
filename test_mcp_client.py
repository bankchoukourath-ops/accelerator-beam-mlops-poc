"""Client de test pour valider les outils du serveur MCP."""
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_test():
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_epics_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("--- Outils exposes par le serveur MCP ---")
            for tool in tools.tools:
                print(f"• {tool.name} : {tool.description.splitlines()[0]}")

            print("\n--- Test 1 : Lecture PV faisceau ---")
            diag = await session.call_tool("read_beam_diagnostics", {})
            print("Reponse :", diag.content[0].text)

            print("\n--- Test 2 : Envoi consigne dangereuse (80 A > limite 60 A) ---")
            rejection = await session.call_tool("apply_magnet_correction", {"target_current": 80.0})
            print("Reponse :", rejection.content[0].text)

if __name__ == "__main__":
    asyncio.run(run_test())
