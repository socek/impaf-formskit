from mock import patch

from pytest import fixture
from pytest import yield_fixture
from pytest import mark

from impaf.testing import ControllerFixture
from impaf.testing import RequestFixture


class FormskitControllerFixture(ControllerFixture):

    @yield_fixture
    def madd_form(self, testable):
        patcher = patch.object(testable, 'add_form')
        with patcher as mock:
            yield mock

    @fixture
    def fform(self, madd_form):
        return madd_form.return_value


class FormFixture(RequestFixture):

    @fixture
    def testable(self, mrequest, registry):
        return self._testable_cls(mrequest)
