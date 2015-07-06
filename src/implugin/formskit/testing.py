from mock import patch

from pytest import yield_fixture
from pytest import fixture

from impaf.testing import ControllerFixture


class FormskitControllerFixture(ControllerFixture):

    @yield_fixture
    def madd_form(self, controller):
        patcher = patch.object(controller, 'add_form')
        with patcher as mock:
            yield mock

    @fixture
    def fform(self, madd_form):
        return madd_form.return_value
