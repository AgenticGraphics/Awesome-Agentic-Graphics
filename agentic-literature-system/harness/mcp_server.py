"""Expose the exact same ResearchTools to the actual Codex CLI baseline."""
import asyncio, os
import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server
from research_tools import ResearchTools, TOOL_SPECS
server=Server('agentic-graphics-research')
tools=ResearchTools(os.environ['RESEARCH_RUN_DIR'])
@server.list_tools()
async def list_tools():return [types.Tool(**s) for s in TOOL_SPECS]
@server.call_tool()
async def call_tool(name,arguments):
    import json
    r=await asyncio.to_thread(tools.call,name,arguments)
    if isinstance(r,dict) and r.get('_image'):
        return [types.TextContent(type='text',text=r['path']),types.ImageContent(type='image',data=r['_image'],mimeType=r['mime_type'])]
    return [types.TextContent(type='text',text=json.dumps(r,ensure_ascii=False))]
async def main():
    try:
        async with stdio_server() as (read,write):await server.run(read,write,server.create_initialization_options())
    finally:tools.close()
if __name__=='__main__':asyncio.run(main())
