from __future__ import annotations

from pathlib import Path
from typing import Any


def write_prompt_package(output: dict[str, Any], output_dir: Path, slug: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{slug}_prompt_package.md"

    structured_prompt = output["structured_prompt"]
    prompt_lines = [
        "# Urban Matrix Prompt Package",
        "",
        f"Project: {output['input']['project_name']}",
        f"Location: {output['input']['location']}",
        f"Generated: {output['created_at']}",
        "",
        "## Project Summary",
        "",
        output["project_summary"],
        "",
        "## Structured Prompt",
        "",
    ]

    for key, value in structured_prompt.items():
        prompt_lines.extend([f"### {key.replace('_', ' ').title()}", "", str(value), ""])

    prompt_lines.extend(
        [
            "## Negative Prompt",
            "",
            output["negative_prompt"],
            "",
            "## Camera Direction",
            "",
            output["camera_direction"],
            "",
            "## Lighting Direction",
            "",
            output["lighting_direction"],
            "",
            "## Consistency Lock",
            "",
            output["consistency_lock"],
            "",
            "## Platform",
            "",
            output["platform_version"],
            "",
            "## Next Steps",
            "",
        ]
    )

    for step in output["next_steps"]:
        prompt_lines.append(f"- {step}")

    path.write_text("\n".join(prompt_lines) + "\n", encoding="utf-8")
    return path
