"""MCP server for Design Token Extractor."""
import sys
import json
from client import DesignTokenExtractor

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "extract_design_tokens",
                "description": "Converts UI design nodes into CSS custom properties and layout constraints",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "ui_nodes": {"type": "array"}
                    },
                    "required": ["ui_nodes"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "extract_design_tokens":
            nodes = params.get("arguments", {}).get("ui_nodes", [])
            res = DesignTokenExtractor.extract_tokens(nodes)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
