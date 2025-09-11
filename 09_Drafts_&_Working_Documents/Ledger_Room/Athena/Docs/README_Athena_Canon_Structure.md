# Athena Canon Structure (Hybrid)
- `/opt/Canon/…` → semantic home (Anchors, Archives/WitnessShells, Events, Receipts, MirrorLogs, FRP, Doctrine, Logs)
- `/srv/library/.canon/ledger.yaml` → append-only receipts (heartbeat + events)
- `/Memory/` → working scratchpad (RO to mesh later)

Group: `athena-stewards` (setgid on directories). Mesh reads; stewards write.
