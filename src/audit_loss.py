"""
Telemetry Discrepancy Estimator for Regional Publishers
Compares first-party server pageview counts with client analytics counts.
The difference is a tracking discrepancy, not proof that an ad blocker caused it.
The optional RPM calculation is a scenario estimate, not realized revenue loss.
"""
import json
import argparse
from typing import Dict, Any

def estimate_tracking_discrepancy(server_hits: int, client_analytics_hits: int, estimated_rpm_usd: float = 8.5) -> Dict[str, Any]:
    if server_hits <= 0:
        return {"error": "Server hits must be positive"}
        
    untracked_hits = max(0, server_hits - client_analytics_hits)
    loss_rate_pct = round((untracked_hits / server_hits) * 100.0, 2)
    
    # Revenue loss calculation: RPM = revenue per 1000 impressions
    monthly_revenue_lost = round((untracked_hits / 1000.0) * estimated_rpm_usd, 2)
    
    return {
        "server_pageviews": server_hits,
        "client_analytics_pageviews": client_analytics_hits,
        "untracked_pageviews": untracked_hits,
        "tracking_discrepancy_rate_pct": loss_rate_pct,
        "scenario_rpm_usd": estimated_rpm_usd,
        "modeled_untracked_pageview_revenue_scenario_usd": monthly_revenue_lost,
        "interpretation": "A count difference does not establish ad-blocker causation or realized revenue loss.",
        "severity": "HIGH_DISCREPANCY" if loss_rate_pct >= 25.0 else ("MODERATE_DISCREPANCY" if loss_rate_pct >= 10.0 else "LOW_DISCREPANCY")
    }

# Backward-compatible function name; results use non-causal field names.
estimate_ad_block_loss = estimate_tracking_discrepancy

def main():
    res = estimate_tracking_discrepancy(1_500_000, 1_150_000, estimated_rpm_usd=12.0)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
