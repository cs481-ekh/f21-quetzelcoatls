from unittest import TestCase

from queue import SimpleQueue
from .test_harness.mock_generator import MockGenerator

import RPfiles


class TestOutputLabel(TestCase):
    def test_forward_output(self):
        # Sequence of commands that will be returned from the window
        input_sequence = SimpleQueue()

        input_sequence.put(("Input", "Fwd", [10, 0]))

        def verify_progress_bar(gui):
            assert str(gui.window['OUTPUT'].title) == "10"

        input_sequence.put(("Assert", "Verify Output Is 10", verify_progress_bar))

        input_sequence.put(("Input", "Fwd", [10, 0]))

        def verify_progress_bar_20(gui):
            assert str(gui.window['OUTPUT'].title) == "20"

        input_sequence.put(("Assert", "Verify Output Is 20", verify_progress_bar_20))

        input_sequence.put(("Input", "Close", []))

        RPfiles.run_frontend(MockGenerator().get_mock_module(input_sequence))

    def test_reverse_output(self):
        # Sequence of commands that will be returned from the window
        input_sequence = SimpleQueue()

        input_sequence.put(("Input", "Rev", [0, 10]))

        def verify_progress_bar(gui):
            assert str(gui.window['OUTPUT'].title) == "-10"

        input_sequence.put(("Assert", "Verify Output Is -10", verify_progress_bar))

        input_sequence.put(("Input", "Rev", [0, 10]))

        def verify_progress_bar_20(gui):
            assert str(gui.window['OUTPUT'].title) == "-20"

        input_sequence.put(("Assert", "Verify Output Is -20", verify_progress_bar_20))

        input_sequence.put(("Input", "Close", []))

        RPfiles.run_frontend(MockGenerator().get_mock_module(input_sequence))