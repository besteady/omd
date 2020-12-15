import unittest
from unittest.mock import patch, Mock
import json
import io

import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):
    @patch("what_is_year_now.urllib.request.urlopen")
    def testYMD(self, mock_urlopen):
        m = Mock()

        def enter_override(self):
            f = io.StringIO()
            json.dump(
                {"currentDateTime": "2019-03-01T14:41Z"},
                f,
            )
            f.seek(0)
            return f

        m.__enter__ = enter_override
        m.__exit__ = lambda self, *args, **kw: None
        mock_urlopen.return_value = m

        self.assertEqual(what_is_year_now.what_is_year_now(), 2019)

    @patch("what_is_year_now.urllib.request.urlopen")
    def testDMY(self, mock_urlopen):
        m = Mock()

        def enter_override(self):
            f = io.StringIO()
            json.dump(
                {"currentDateTime": "01.03.2019T14:41Z"},
                f,
            )
            f.seek(0)
            return f

        m.__enter__ = enter_override
        m.__exit__ = lambda self, *args, **kw: None
        mock_urlopen.return_value = m

        self.assertEqual(what_is_year_now.what_is_year_now(), 2019)

    @patch("what_is_year_now.urllib.request.urlopen")
    def testIncorFormat(self, mock_urlopen):
        m = Mock()

        def enter_override(self):
            f = io.StringIO()
            json.dump(
                {"currentDateTime": "01.2019.03T14:41Z"},
                f,
            )
            f.seek(0)
            return f

        m.__enter__ = enter_override
        m.__exit__ = lambda self, *args, **kw: None
        mock_urlopen.return_value = m

        with self.assertRaises(ValueError):
            self.assertEqual(what_is_year_now.what_is_year_now(), 2019)

    @patch("what_is_year_now.urllib.request.urlopen")
    def testMain(self, mock_urlopen):
        m = Mock()

        def enter_override(self):
            f = io.StringIO()
            json.dump(
                {"currentDateTime": "01.03.2019T14:41Z"},
                f,
            )
            f.seek(0)
            return f

        m.__enter__ = enter_override
        m.__exit__ = lambda self, *args, **kw: None
        mock_urlopen.return_value = m

        try:
            what_is_year_now.main(None)
        except Exception:
            self.fail("")
