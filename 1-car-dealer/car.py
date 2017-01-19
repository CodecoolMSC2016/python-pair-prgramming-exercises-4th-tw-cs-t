from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, ccm =0, top_speed = 0, is_running = False):
        super().__init__(ccm, top_speed)
        self.is_running = is_running

    def start_engine(self):
        self.is_running = True

    def stop_engine(self):
        self.is_running = False
