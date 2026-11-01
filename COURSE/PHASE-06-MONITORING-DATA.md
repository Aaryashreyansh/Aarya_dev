# Phase 6 — Monitoring and databases (Weeks 23–25)

**Outcome:** observe an application and understand how it stores and retrieves data.

## Week 23 — Observability
Learn metrics, logs and traces; instrumentation; labels; cardinality; dashboards; alert thresholds; notification routing; SLI, SLO and SLA. Understand that an alert should describe user impact and a useful action, not simply report noise.

## Week 24 — Prometheus and Grafana
Learn Prometheus scrape model, targets, exporters, time-series samples, labels and PromQL basics. Learn Grafana data sources, panels, variables and dashboards. In a local lab, monitor a demo service and chart request rate, errors and latency. Create a simple alert and test it with controlled sample conditions.

## Week 25 — SQL and NoSQL
SQL: tables, rows, columns, primary/foreign keys, SELECT, WHERE, ORDER BY, GROUP BY, aggregate functions, JOIN, indexes, transactions and constraints. Practise on a local sample database.
NoSQL: understand document, key-value, wide-column and graph models. Learn MongoDB document concepts and Redis key/value, expiry and caching concepts. Compare data models based on access patterns; do not assume NoSQL means no structure.

## Safe data habits
Use fake sample data. Learn parameterized queries to avoid SQL injection. Do not put real personal information, passwords or tokens in test databases or logs. Backups should be tested by restoring a copy.

## Mini project
Add a monitoring dashboard to the Phase 3 app. Document each metric, what a normal value means, what alert triggers, how to investigate and how to silence/resolve an alert responsibly.

## Exit checklist
- [ ] Dashboard shows useful service signals.
- [ ] One alert is tested and documented.
- [ ] SQL joins and aggregations are practised.
- [ ] SQL and NoSQL use cases can be compared.
- [ ] Logs avoid secrets and unnecessary personal data.


## Where to learn this phase
See [Resources Directory](RESOURCES.md): Prometheus → official first-steps guide; Grafana → official learning hub; SQL → PostgreSQL tutorial and SQLBolt; MongoDB and Redis → their official documentation and learning pages.
