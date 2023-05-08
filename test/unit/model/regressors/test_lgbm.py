# SPDX-FileCopyrightText: 2017-2023 Contributors to the OpenSTEF project <korte.termijn.prognoses@alliander.com> # noqa E501>
#
# SPDX-License-Identifier: MPL-2.0
from test.unit.utils.base import BaseTestCase

from openstef.model.regressors.lgbm import LGBMOpenstfRegressor


class TestXGB(BaseTestCase):
    def setUp(self) -> None:
        self.model = LGBMOpenstfRegressor()

    def test_importance_names(self):
        self.assertIsInstance(self.model._get_importance_names(), dict)
