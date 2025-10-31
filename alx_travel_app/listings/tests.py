from django.test import TestCase


class ListingsSmokeTest(TestCase):
    def test_listings_module_imports(self):
        # simple import smoke test
        import importlib
        mod = importlib.import_module('alx_travel_app.listings')
        self.assertIsNotNone(mod)
