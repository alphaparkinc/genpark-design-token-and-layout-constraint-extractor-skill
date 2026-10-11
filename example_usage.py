"""Example usage for Design Token Extractor."""
from client import DesignTokenExtractor

if __name__ == "__main__":
    nodes = [
        {"name": "Hero Card", "backgroundColor": "#0F172A", "padding": 24, "layoutMode": "VERTICAL"},
        {"name": "CTA Button", "backgroundColor": "#2563EB", "padding": 12, "layoutMode": "HORIZONTAL"}
    ]
    tokens = DesignTokenExtractor.extract_tokens(nodes)
    print("CSS Variables:", tokens["css_color_variables"])
    print("Spacing Scale:", tokens["spacing_scale"])
