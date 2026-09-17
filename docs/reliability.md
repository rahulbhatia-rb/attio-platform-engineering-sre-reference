# Reliability operating model

An SLO is an agreement with service users, not a dashboard decoration. Define a user-visible indicator, measurement query, target, window, exclusions and owner before enforcing a gate. The sample function is intentionally simple: real availability must be measured from authenticated telemetry and must avoid counting synthetic noise or double-counting retries.

When budget burn is sustained, pause discretionary release risk, assess customer impact and error/latency/saturation signals, and assign an incident lead. Restore service first; then hold a blameless review that records contributing conditions, detection gaps, decisions and owned code/config follow-ups. Capacity planning should use actual utilization and forecasted load, with headroom targets agreed by service owners.

Use immutable image digests, reviewable desired state and progressive rollout. A passed gate does not make a change safe: test rollback, dependency failure, IAM/network policies and alert routing. Keep raw customer data and secrets out of logs, traces, test fixtures and post-mortems.
