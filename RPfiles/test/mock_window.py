from queue import SimpleQueue

WIN_CLOSED = "WindowClosedConst"

def theme(self, *args, **kwargs): pass # Theme is a no-op

def execute_command_subprocess(script, *args, **kwargs):
    print(f"GuiTestHarness: Subprocess [would have been] started for {script} with args {args}")

class _Control:
    def __init__(self, key):
        self.key = key

    def Update(self, *args, **kwargs):
        print(f"GuiTestHarness: Control update: {self.key} received updates: {args} {kwargs}")

class Button(_Control):
    def __init__(self, title, *args, **kwargs):
        self.title = title
        self.key = kwargs['key'] if 'key' in kwargs else title
        print(f"GuiTestHarness: Button initialized with title {title}")

        super(Button, self).__init__(self.key)


class Text(_Control):
    def __init__(self, title, *args, **kwargs):
        self.title = title
        self.key = kwargs['key'] if 'key' in kwargs else title
        print(f"GuiTestHarness: Text initialized with title {title}")

        super(Text, self).__init__(self.key)


class InputText(_Control):
   def __init__(self):
       self.key = "(Input Text)"
       print(f"GuiTestHarness: Text initialized")

       super(InputText, self).__init__(self.key)


class Window:
    def __init__(self, title, layout):
        self.title = title

        # Flatten it
        self.layout = [item for sublist in layout for item in sublist]

        self.layout_dict = {}
        for elem in self.layout:
            self.layout_dict[elem.key] = elem

        print(f"GuiTestHarness: MockWindow initialized with title {title}")

        self.input_sequence = SimpleQueue()

        # Sequence of commands that will be returned from the window
        self.input_sequence.put(("Fwd", [10, 0]))
        self.input_sequence.put(("Close", []))

    def __getitem__(self, key):
        return self.layout_dict[key]

    def getValues(self): return []

    def read(self, *args, **kwargs):
        if 'timeout' in kwargs and kwargs['timeout'] == 1:
            return (None, None)

        return self.input_sequence.get()

    def Refresh(self): pass

    def close(self):
        print("GuiTestHarness: Window closed")
