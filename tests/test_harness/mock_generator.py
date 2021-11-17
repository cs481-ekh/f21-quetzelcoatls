class MockGenerator:
    def get_mock_module(self, sequence):
        class GuiMocker:
            def __init__(self):
                self.controls = []
                self.window = None

            WIN_CLOSED = "WindowClosedConst"

            def theme(self, *args, **kwargs): pass # Theme is a no-op

            def execute_command_subprocess(script, *args, **kwargs):
                print(f"GuiTestHarness: Subprocess [would have been] started for {script} with args {args}")

                class mock_subprocess_return:
                    def __init__(self):
                        self.returncode = 0

                return mock_subprocess_return()

            class _Control:
                def __init__(self, key, gui_mocker, *args, **kwargs):
                    self.key = key
                    self.gui_mocker = gui_mocker

                    gui_mocker.controls.append(self)

                def Update(self, *args, **kwargs):
                    print(f"GuiTestHarness: Control update: {self.key} received updates: {args} {kwargs}")


            class _ProgressBar(_Control):
                def __init__(self, gui_mocker, *args, **kwargs):
                    self.max_value = kwargs["max_value"]
                    self.key = kwargs['key']
                    self.visible = kwargs["visible"]

                    super(GuiMocker._ProgressBar, self).__init__(self.key, gui_mocker)


            def ProgressBar(self, *args, **kwargs):
                return GuiMocker._ProgressBar(self, *args, **kwargs)

            class _Button(_Control):
                def __init__(self, gui_mocker, title, *args, **kwargs):
                    self.title = title
                    self.key = kwargs['key'] if 'key' in kwargs else title
                    print(f"GuiTestHarness: Button initialized with title {title}")

                    super(GuiMocker._Button, self).__init__(self.key, gui_mocker)

            def Button(self, *args, **kwargs):
                return GuiMocker._Button(self, *args, **kwargs)

            class _Text(_Control):
                def __init__(self, gui_mocker, title, *args, **kwargs):
                    self.title = title
                    self.key = kwargs['key'] if 'key' in kwargs else title
                    print(f"GuiTestHarness: Text initialized with title {title}")

                    super(GuiMocker._Text, self).__init__(self.key, gui_mocker)

                def Update(self, title, *args, **kwargs):
                    self.title = title
                    super(GuiMocker._Text, self).Update(self, title, *args, **kwargs)

            def Text(self, *args, **kwargs):
                return GuiMocker._Text(self, *args, **kwargs)

            class _InputText(_Control):
               def __init__(self, gui_mocker, *args, **kwargs):
                   self.value = "(Input Text)"
                   self.micro = 0
                   self.key = None

                   if "key" in kwargs:
                       self.key = kwargs['key']
                       del kwargs['key']

                   print(f"GuiTestHarness: Text initialized")

                   super(GuiMocker._InputText, self).__init__(self.key, gui_mocker, *args, **kwargs)
                   
               def Update(self, *args, **kwargs):
                   self.value = args[0]
                   super(GuiMocker._InputText, self).Update(self, *args, **kwargs)

            def InputText(self, *args, **kwargs):
                return GuiMocker._InputText(self, *args, **kwargs)

            class _Window:
                def __init__(self, gui_mocker, title, layout):
                    self.gui_mocker = gui_mocker
                    gui_mocker.window = self
                    self.title = title

                    # Flatten it
                    self.layout = [item for sublist in layout for item in sublist]

                    self.layout_dict = {}
                    for elem in self.layout:
                        self.layout_dict[elem.key] = elem

                    print(f"GuiTestHarness: MockWindow initialized with title {title}")


                def __getitem__(self, key):
                    return self.layout_dict[key]

                def getValues(self): return []

                def read(self, *args, **kwargs):
                    if 'timeout' in kwargs and kwargs['timeout'] == 1:
                        return (None, None)

                    return self.next_in_sequence()

                def next_in_sequence(self):
                    next_val = sequence.get()

                    while next_val[0] == "Assert":
                        self.eval_assert(next_val)
                        next_val = sequence.get()

                    if next_val[0] == "Input":
                        return next_val[1:999]

                def eval_assert(self, seq_item):
                    seq_item[2](self.gui_mocker)
                    print(f"Assertion '{seq_item[1]}' passed")
                    pass

                def Refresh(self): pass

                def close(self):
                    print("GuiTestHarness: Window closed")

            def Window(self, *args, **kwargs):
                return GuiMocker._Window(self, *args, **kwargs)

        return GuiMocker()