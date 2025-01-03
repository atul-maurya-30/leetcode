class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        #we use below codes for making copies of the class(also called as object)
        self.parking=[0,big,medium,small]
        

    def addCar(self, carType: int) -> bool:
        if self.parking[carType]>0:
            self.parking[carType]-=1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)