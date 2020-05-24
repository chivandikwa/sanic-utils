import snapshottest

from examples.server import create_app


class TestClass(snapshottest.TestCase):

    def setUp(self):
        self.app = create_app()
        print('creating app')

    def test_valid_json_no_exception_returns_object(self):
        # no exception throw, test pass
        request, response = self.app.test_client.post('/test', json={
            "name": "test_name",
            "identifier": "test_id"
        })
        self.assertTrue(response.status == 200)
        self.assertMatchSnapshot(response.json)

    def test_invalid_json_no_exception_returns_none(self):
        # no exception throw, test pass
        request, response = self.app.test_client.post('/test', data='{"name": "test_na}')
        self.assertTrue(response.status == 200)
        self.assertIsNone(response.json)
