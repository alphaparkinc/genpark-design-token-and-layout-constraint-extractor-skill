"""Design Token & Layout Constraint Extractor.
100% Python Standard Library.
"""

class DesignTokenExtractor:
    """Extracts normalized CSS design tokens and responsive layout rules from UI node definitions."""
    
    @staticmethod
    def extract_tokens(ui_nodes: list) -> dict:
        colors = {}
        spacing = set()
        components = []
        
        for idx, node in enumerate(ui_nodes, start=1):
            name = node.get("name", f"node-{idx}").lower().replace(" ", "-")
            bg = node.get("backgroundColor")
            pad = node.get("padding")
            layout = node.get("layoutMode", "BLOCK")
            
            if bg:
                colors[f"--color-{name}"] = bg
            if pad is not None:
                spacing.add(f"{pad}px")
                
            components.append({
                "component": name,
                "display": "flex" if layout in ["HORIZONTAL", "VERTICAL"] else "block",
                "flex_direction": "row" if layout == "HORIZONTAL" else ("column" if layout == "VERTICAL" else "none")
            })
            
        return {
            "css_color_variables": colors,
            "spacing_scale": sorted(list(spacing)),
            "component_layouts": components
        }
