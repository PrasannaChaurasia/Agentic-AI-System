# Urban Matrix Prompt Generator

## Purpose
Convert rough architectural ideas into structured, production-ready visual prompts.

## When To Use
Use this skill when the user asks for architectural render prompts, concept prompts, ComfyUI prompts, Midjourney-style prompts, camera direction, lighting direction, negative prompts, or visual consistency rules.

## Inputs Required
- project_name
- project_type
- location
- design_intent
- output_type
- platform

## Optional Inputs
- geometry
- site_context
- materials
- style
- camera_angle
- lighting
- references

## Output Format
Return both JSON and Markdown with:
- project_summary
- structured_prompt
- negative_prompt
- camera_direction
- lighting_direction
- consistency_lock
- platform_version
- next_steps

## Rules
- Keep prompts architectural, specific, and buildable.
- Include site, material, camera, lighting, and constraints.
- Avoid generic futuristic language unless the brief explicitly needs it.
- Use a negative prompt to reduce visual artifacts.
- Preserve Urban Matrix design identity through a consistency lock.

## Tools Allowed
- Local file read/write inside the project workspace
- JSON export
- Markdown export

## Tools Forbidden
- Sending files externally
- Publishing outputs
- Modifying original project files
- Running paid render jobs without approval

## Quality Checklist
- Project name and location are present.
- Prompt has clear spatial and material logic.
- Camera and lighting are specific enough for image generation.
- Negative prompt prevents common architectural render failures.
- Output is valid JSON and readable Markdown.

