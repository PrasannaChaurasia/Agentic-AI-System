# Persistence And Recovery

## Persistence Model
- `outputs/` stores generated JSON and Markdown packages.
- Future `database/` migrations will store tasks, logs, approvals, and project records.
- Future vector memory should be rebuildable from source documents and approved outputs.
- GitHub stores code, documentation, skills, examples, and version history.

## Recovery Rules
- Keep `.env` out of Git.
- Recreate local secrets from `.env.example`.
- Restore generated outputs from GitHub releases, Drive, S3, or local backup.
- Treat the database as the task source of truth once Phase 4 is added.
- Keep local worker tasks resumable, with task IDs and output checkpoints.

## Failure Handling
Every agent should record:
- task ID
- agent name
- input summary
- tool call summary
- risk level
- status
- error message
- output paths
- approval state

