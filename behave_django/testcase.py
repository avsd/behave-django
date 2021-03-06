from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class BehaviorDrivenTestCase(StaticLiveServerTestCase):
    """
    Test case attached to the context during behave execution

    This test case prevents the regular tests from running.
    """

    def runTest(self):
        pass


class ExistingDatabaseTestCase(BehaviorDrivenTestCase):
    """
    Test case used for the --use-existing-database setup

    This test case prevents fixtures from being loaded to the database in use.
    """

    def _fixture_setup(self):
        pass

    def _fixture_teardown(self):
        pass
