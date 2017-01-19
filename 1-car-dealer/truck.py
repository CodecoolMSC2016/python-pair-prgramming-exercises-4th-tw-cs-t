from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, ccm = 0, top_speed = 0, carry_limit =0, current_carriage_weight = None):
        super().__init__(ccm,top_speed)
        self.carry_limit = carry_limit
        self.current_carriage_weight = current_carriage_weight

    def has_carriage(self):
        return self.current_carriage_weight != None

    def attach_carriage(self, weight):
        if weight > self.carry_limit:
            return False
        else:
            return True

    def detach_carriage(self):
        self.current_carriage_weight = None
