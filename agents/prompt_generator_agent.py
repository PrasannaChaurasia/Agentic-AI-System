from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tools.markdown_writer import write_prompt_package


@dataclass
class PromptInput:
    project_name: str
    project_type: str
    location: str
    design_intent: str
    geometry: str = ""
    site_context: str = ""
    materials: str = ""
    style: str = ""
    output_type: str = "architectural render prompt"
    platform: str = "ComfyUI / Midjourney style"
    camera_angle: str = "cinematic eye-level and aerial variations"
    lighting: str = "soft daylight with controlled contrast"
    references: str = ""


class UrbanMatrixPromptGeneratorAgent:
    name = "Urban Matrix Prompt Generator Agent"
    version = "0.1.0"

    def generate(self, prompt_input: PromptInput) -> dict[str, Any]:
        project_summary = (
            f"{prompt_input.project_name} is a {prompt_input.project_type} in "
            f"{prompt_input.location}, focused on {prompt_input.design_intent}."
        )

        structured_prompt = {
            "role": "You are an architectural visualisation director for Urban Matrix.",
            "task": f"Create a high-quality {prompt_input.output_type}.",
            "context": project_summary,
            "geometry": prompt_input.geometry or "Expressive but buildable architectural massing.",
            "logic": "Prioritise spatial clarity, urban response, material credibility, and cinematic composition.",
            "site": prompt_input.site_context or f"Respond to the urban context of {prompt_input.location}.",
            "material": prompt_input.materials or "Use a refined palette of glass, metal, concrete, timber, and landscape elements where appropriate.",
            "output": prompt_input.output_type,
            "constraints": "Avoid impossible structure, distorted scale, cluttered signage, text artifacts, and generic sci-fi styling.",
            "refinement": "Make the result feel like a competition-grade architecture visual with clear foreground, middle ground, and background.",
            "style": prompt_input.style or "Urban Matrix cinematic architectural realism.",
            "prompt_engineering": "Use precise nouns, controlled adjectives, camera language, lighting cues, and consistency locks.",
        }

        return {
            "agent": self.name,
            "version": self.version,
            "created_at": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "input": asdict(prompt_input),
            "project_summary": project_summary,
            "structured_prompt": structured_prompt,
            "negative_prompt": (
                "low resolution, blurry, warped geometry, impossible columns, broken perspective, "
                "overexposed sky, messy people, illegible text, duplicated objects, cartoon render, "
                "generic sci-fi, poor materials, distorted facade, unrealistic shadows"
            ),
            "camera_direction": prompt_input.camera_angle,
            "lighting_direction": prompt_input.lighting,
            "consistency_lock": (
                f"Keep the project identity consistent: {prompt_input.project_name}, "
                f"{prompt_input.location}, {prompt_input.style or 'Urban Matrix design language'}."
            ),
            "platform_version": prompt_input.platform,
            "next_steps": [
                "Review prompt package for project accuracy.",
                "Send to QA / Reviewer Agent before production use.",
                "Create render variations or ComfyUI workflow JSON in the next phase.",
            ],
        }


def load_input(path: Path) -> PromptInput:
    data = json.loads(path.read_text(encoding="utf-8"))
    return PromptInput(**data)


def save_json(output: dict[str, Any], output_dir: Path, slug: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{slug}_prompt_package.json"
    path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    return path


def slugify(value: str) -> str:
    return "".join(char.lower() if char.isalnum() else "_" for char in value).strip("_")


def main() -> None:
    input_path = Path("examples/flux_pavilion_input.json")
    output_dir = Path("outputs")
    agent = UrbanMatrixPromptGeneratorAgent()
    prompt_input = load_input(input_path)
    output = agent.generate(prompt_input)
    slug = slugify(prompt_input.project_name)
    json_path = save_json(output, output_dir, slug)
    md_path = write_prompt_package(output, output_dir, slug)
    print(f"Generated JSON: {json_path}")
    print(f"Generated Markdown: {md_path}")


if __name__ == "__main__":
    main()
