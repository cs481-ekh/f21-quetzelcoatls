from unittest import TestCase

from queue import SimpleQueue
from .test_harness.mock_generator import MockGenerator

import RPfiles


class TestMicroInput(TestCase):
    def test_micro_input(self):
        # Sequence of commands that will be returned from the window
        input_sequence = SimpleQueue()
        
        input_sequence.put(("Input", "micro", {'micro':"1.111"}))

        def verify_micro_output(gui):
            assert gui.window['micro'].value == '1.111'

        input_sequence.put(("Assert", "Verify Output Is 1.111", verify_micro_output))

        input_sequence.put(("Input", "micro", {'micro':"1.11"}))

        def verify_micro_output_2(gui):
            assert gui.window['micro'].value == "1.11"

        input_sequence.put(("Assert", "Verify Output Is 1.11", verify_micro_output_2))

        input_sequence.put(("Input", "micro", {'micro':"1.11\n\r 3"}))

        def verify_micro_output_whitespace(gui):
            assert gui.window['micro'].value == "3"

        input_sequence.put(("Assert", "Verify Output Is 3", verify_micro_output_whitespace))

        input_sequence.put(("Input", "micro", {'micro':"1.1111"}))

        def verify_micro_output_empty(gui):
            assert gui.window['micro'].value == ""

        input_sequence.put(("Assert", "Verify Output Is cleared on bad input", verify_micro_output_empty))

        input_sequence.put(("Input", "micro", {'micro':"11.11"}))

        def verify_micro_output_empty2(gui):
           assert gui.window['micro'].value == ""

        input_sequence.put(("Assert", "Verify Output Is empty on bad input", verify_micro_output_empty2))
        
        input_sequence.put(("Input", "micro", {'micro':"a"}))

        def verify_micro_output_empty3(gui):
           assert gui.window['micro'].value == ""

        input_sequence.put(("Assert", "Verify Output Is empty on bad input", verify_micro_output_empty3))
        
        input_sequence.put(("Input", "Close", []))

        RPfiles.run_frontend(MockGenerator().get_mock_module(input_sequence))

