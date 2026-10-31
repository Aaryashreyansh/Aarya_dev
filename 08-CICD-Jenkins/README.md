# 08. CI/CD and Jenkins
Concepts: Continuous Integration, Continuous Delivery, Continuous Deployment, pipeline stages, agents, artifacts, approvals and rollback planning.

Typical pipeline: checkout → install dependencies → lint/test → build artifact → scan → publish to authorized registry → deploy to test → approval/release.

Exercises: draw a pipeline for a Python project, add a test stage, explain artifact vs image and document a failed pipeline.

Keep deployment credentials in the CI platform's secret store, never in source code.