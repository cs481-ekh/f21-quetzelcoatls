from unittest import TestCase

from queue import SimpleQueue
from .test_harness.mock_generator import MockGenerator

import RPfiles


class TestOutputLabel(TestCase):
    def test_forward_output(self):
        # Sequence of commands that will be returned from the window
        input_sequence = SimpleQueue()

        input_sequence.put(("Input", "Fwd", [10, 0]))
        input_sequence.put(("Input", "Ret0", ""))

        def verify_progress_bar(gui):
            assert str(gui.window['OUTPUT'].title) == "0"

        input_sequence.put(("Assert", "Verify Output Is 0", verify_progress_bar))

        input_sequence.put(("Input", "Fwd", [10, 0]))
        input_sequence.put(("Input", "Rev", [0, 15]))
        input_sequence.put(("Input", "Ret0", ""))


        input_sequence.put(("Assert", "Verify Output Is 0", verify_progress_bar))

        input_sequence.put(("Input", "Rev", [0, 10]))
        input_sequence.put(("Input", "Ret0", ""))

        input_sequence.put(("Assert", "Verify Output Is 0", verify_progress_bar))

        input_sequence.put(("Input", "Rev", [0, 10]))
        input_sequence.put(("Input", "Rev", [23, 0]))
        input_sequence.put(("Input", "Ret0", ""))

        input_sequence.put(("Assert", "Verify Output Is 0", verify_progress_bar))

        input_sequence.put(("Input", "Close", []))

        RPfiles.run_frontend(MockGenerator().get_mock_module(input_sequence))
