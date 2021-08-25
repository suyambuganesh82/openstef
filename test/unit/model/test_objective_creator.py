# SPDX-FileCopyrightText: 2017-2021 Alliander N.V. <korte.termijn.prognoses@alliander.com> # noqa E501>
#
# SPDX-License-Identifier: MPL-2.0
import unittest

from test.utils.base import BaseTestCase

from openstf.enums import MLModelType
from openstf.model.objective_creator import ObjectiveCreator
from openstf.model.objective import XGBRegressorObjective, RegressorObjective


class TestObjectiveCreator(BaseTestCase):
    def test_create_objective_happy(self):
        Objective = ObjectiveCreator.create_objective(MLModelType.XGB)
        self.assertEqual(Objective, XGBRegressorObjective)

    def test_create_objective_not_implemented_model_type(self):
        """Test if a nice error is returned if a not-implemented model is requested"""
        with self.assertRaises(NotImplementedError):
            ObjectiveCreator.create_objective("AnUnimplementedModelType")


if __name__ == "__main__":
    unittest.main()
