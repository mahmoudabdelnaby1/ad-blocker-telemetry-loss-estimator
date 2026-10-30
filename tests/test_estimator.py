"""
Unit tests for Ad Blocker Loss Estimator
"""
import unittest
from src.audit_loss import estimate_tracking_discrepancy

class TestLossEstimator(unittest.TestCase):
    def test_loss_estimation(self):
        res = estimate_tracking_discrepancy(100000, 80000, estimated_rpm_usd=10.0)
        self.assertEqual(res["untracked_pageviews"], 20000)
        self.assertEqual(res["tracking_discrepancy_rate_pct"], 20.0)
        self.assertEqual(res["modeled_untracked_pageview_revenue_scenario_usd"], 200.0)

if __name__ == "__main__":
    unittest.main()
