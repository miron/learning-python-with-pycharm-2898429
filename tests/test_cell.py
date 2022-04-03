from unittest import TestCase
from cell import *


class TestCell(TestCase):
    def test_set_future_state(self):
        active_test_cell = Cell((0, 0), (0, 0), active=True)
        # i will have values from 0 to 8 inclusive. This works because a cell
        # can have 0 to 8 active neighbors
        for i in range(9):
            active_test_cell.set_future_state(i)
            if i == 2 or i == 3:
                # future state should be active.
                self.assertTrue(active_test_cell.future_state)
            else:
                self.assertFalse(active_test_cell.future_state)

        inactive_test_cell = Cell((0, 0), (0, 0), active=False)
        for i in range(9):
            inactive_test_cell.set_future_state(i)
            if i == 3:
                # future state should be active.
                self.assertTrue(inactive_test_cell.future_state)
            else:
                self.assertFalse(inactive_test_cell.future_state)

    # def test_update(self):
    #     self.fail()


# class TestCell(TestCase):
#     def test_set_future_state(self):
#         # set up your test
#         # only an active cell with 2 neighbors will have future_state = True
#         active_cell = Cell((0, 0), (0, 0), active=True)
#         for neighbor_count in range(9):
#             active_cell.set_future_state(living_neighbors=neighbor_count)
#             if neighbor_count == 2 or neighbor_count == 3:
#                 self.assertTrue(active_cell.future_state, f'should be set up to remain active with {neighbor_count}, '
#                                                           f'neighbors')
#             else:
#                 self.assertFalse(active_cell.future_state, f'should be set up to be inactive with {neighbor_count}, '
#                                                            f'neighbors')
