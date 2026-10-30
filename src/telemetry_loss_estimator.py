#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

def estimate_telemetry_loss(log_path):
    server_hits = 0
    client_beacon_hits = 0

    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            if "GET /product/" in line or "GET /categories/" in line:
                server_hits += 1
            if "/analytics/collect" in line or "/gtm/collect" in line:
                client_beacon_hits += 1

    discrepancy = server_hits - client_beacon_hits
    loss_rate = (max(discrepancy, 0) / max(server_hits, 1)) * 100
    return {
        "server_pageviews": server_hits,
        "client_analytics_hits": client_beacon_hits,
        "pageview_count_discrepancy": discrepancy,
        "unmatched_server_pageviews": max(discrepancy, 0),
        "tracking_discrepancy_rate_pct": round(loss_rate, 1),
        "interpretation": "A count difference does not establish ad-blocker causation."
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--logs", required=True)
    args = p.parse_args()

    res = estimate_telemetry_loss(args.logs)
    print(res)

if __name__ == "__main__":
    main()
