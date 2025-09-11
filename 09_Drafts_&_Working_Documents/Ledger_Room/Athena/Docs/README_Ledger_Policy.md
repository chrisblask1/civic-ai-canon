# Ledger Policy (Athena)
- Path: `/srv/library/.canon/ledger.yaml`
- Default: RO to mesh; RW only for `athena-stewards`.
- Appends via `kusanagi-heartbeat` (systemd service or timer).
- Receipts must include integrity fields for publication (hash/sign).
