from auto_moving import AutoMoving


class AutoMovingBlinking(AutoMoving):
    def __init__(self, direction):
        super().__init__(direction)
        self.active = True

    def on_run_timer(self):
        if self.active:
            self.deactivate()
        else:
            self.activate()

        super().on_run_timer()

    def draw(self, pixels):
        if self.active:
            super().draw(pixels)

    def deactivate(self):
        self.active = False
        self.collision_enabled = False

    def activate(self):
        self.active = True
        self.collision_enabled = True
