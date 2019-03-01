from mtf.magic.backend.backend_suite import BackendSuite


class TestSuiteBackendScanning(BackendSuite):

    def test_get_protocols(self):
        resp = self.request_api('get','protocols')