import unittest
from app.slo import Window,evaluate
from app.release_gate import admit_release
class SLO(unittest.TestCase):
 def test_budget_is_burned(self): self.assertTrue(evaluate(Window(990,1000),.995)["burned"])
 def test_invalid_counts_fail(self):
  with self.assertRaises(ValueError): evaluate(Window(11,10),.99)
 def test_release_requires_digest_and_budget(self):
  self.assertFalse(admit_release("repo/api:1",Window(1000,1000),.99)["admitted"])
  self.assertFalse(admit_release("repo/api@sha256:abc",Window(990,1000),.995)["admitted"])
  self.assertTrue(admit_release("repo/api@sha256:abc",Window(1000,1000),.995)["admitted"])
