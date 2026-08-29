import os
import re

import yaml


def convert_frontmatter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pelican frontmatter is typically at the start of the file, consisting of Key: Value lines
    # It ends at the first blank line.

    lines = content.split("\n")
    metadata = {}
    content_start = 0

    for i, line in enumerate(lines):
        if not line.strip():
            content_start = i + 1
            break

        # Match "Key: Value"
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            key = match.group(1).lower()
            value = match.group(2).strip()

            # Special handling for tags and categories (Pelican sometimes uses comma-separated strings)
            if key in ("tags", "category", "categories"):
                value = [v.strip() for v in value.split(",")]

            # Use appropriate types
            if value == "True":
                value = True
            elif value == "False":
                value = False

            # Header cover logic for this specific theme
            if key == "header_cover":
                metadata["image"] = value
            else:
                metadata[key] = value
        else:
            # If a line doesn't match and we haven't hit a blank line, maybe it's not standard Pelican frontmatter
            # Or it's a multi-line value (rare in Pelican but possible). For this simple script, we'll assume standard.
            pass

    if not metadata:
        print(f"No metadata found in {file_path}")
        return

    # Standardize 'categories' for Hugo if 'category' was used
    if "category" in metadata and "categories" not in metadata:
        metadata["categories"] = metadata.pop("category")

    # Generate Hugo YAML frontmatter
    yaml_frontmatter = (
        "---\n"
        + yaml.dump(metadata, default_flow_style=False, sort_keys=False)
        + "---\n"
    )

    new_content = yaml_frontmatter + "\n".join(lines[content_start:])

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Converted: {file_path}")


def main():
    content_dir = "content"
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                convert_frontmatter(file_path)


if __name__ == "__main__":
    main()
