from BlockClass import Block
import time

class TrainClass():
        def __init__(self,trainID):
                self.ID = trainID
                self.blocks = Block()

        authority = 0
        beacon = "Not In Service"
        announcement = " "
        speed_limit = 0
        commSpeed = 0
        velocityMPH = 0
        velocityKM = 0
        velocity = 0
        prevVel = 0.0001
        acceleration = 0
        prevAcc = 0.0001
        power = 0
        massTon = 40.9     #in tons
        mass = 0
        boarding = 0
        passenger = 0
        crew = 2
        temperature = 68
        doorStatus = False
        internalStatus = False
        externalStatus = False
        emergency = False
        service = False
        brake = False
        brakeFailure = False
        engineFailure = False
        signalFailure = False
        faults = 0
        blockNum = 0
        nextblock = 0
        line = "Green"
        headlightCommand = False
        stationDoors = 0
        maxAcceleration = 0.5       #mps^2
        maxSpeed = 70            #km/hr
        minSpeed = 0
        prevPosition = 0
        currPos = 0
        position=0

        #block grades and elevations
        blockGrade = 0
        elevation = 0
        cElevation = 0
        blockLength = 0
        switchBlock = 0
        signal = 0
        base = 0

        def calculateMass(self):
            self.massTon = 40.9 + (self.passenger+2)*(0.1068)
            self.mass = self.massTon * 907.185   #ton to kg conversion

        lastTime = 0.0
        timeChange = 0.0
        startTime = 0.0
        
        def calculateVelocity(self):

                #time since last calculation
                self.currTime = time.time()
                self.timeChange = self.currTime - self.startTime

                self.calculateMass()
        
                force = self.power / self.prevVel
                if (force != 0):
                        
                        self.acceleration = force / self.mass

                        if self.emergency == 1:
                                self.acceleration = self.maxAcceleration
                        elif self.brake == 1:
                                self.acceleration = self.maxAcceleration
                        elif self.service == 1:
                                self.acceleration = self.maxAcceleration
                        elif (self.acceleration > self.maxAcceleration):
                                self.acceleration = self.maxAcceleration

                        self.velocity = self.prevVel + (self.timeChange/2)*(self.acceleration + self.prevAcc)

                        #stops brakes if speed is now less than speed limit
                        if (self.brake == 1 and self.velocity < self.mphTOmps(self.speed_limit)):
                                self.brakesDone()

                        #makes sure the velocity is never greater than the speed limit
                        if (self.velocity > self.mphTOmps(self.speed_limit)):
                                self.brake = 1
                                self.maxAcceleration = -1.12

                        #makes sure the velocity never exceeds the max speed
                        if self.velocity > self.kmhTOmps(self.maxSpeed):
                                self.velocity = self.kmhTOmps(self.maxSpeed)
                                self.acceleration = 0
                        
                        #if velocity becomes less than zero, it is essentially zero
                        if self.velocity < self.minSpeed:
                                self.velocity = 0
                                self.acceleration = 0
                                self.brakesDone()

                        self.prevAcc = self.acceleration
                        self.prevVel = self.velocity

                #calculate position
                self.position += self.timeChange * self.velocity
                
                if (self.position > self.blockLength):
                        self.blocks.greenLine.pop(0)            #removes firt element
                        self.blockNum = self.blocks.greenLine[0]
                        self.currPos = self.position - self.blockLength
                        self.position=0
                else:
                        self.currPos = self.blockLength - self.position


                if (self.velocity == 0):
                        self.prevVel = 0.0001
                if (self.acceleration == 0):
                        self.prevAcc = 0.0001
                self.startTime = self.currTime

                self.velocityMPH = self.mpsTOmph(self.velocity)
                self.velocityKM = self.mpsTOkm(self.velocity)
                #print(self.currPos)
                return self.mpsTOmph(self.velocity)

        def mphTOmps(self,x):
                return x/2.23694

        def mpsTOmph(self,y):
                return y*2.23694

        def kmhTOmps(self,a):
                return a/3.6

        def mpsTOkm(self,b):
                return b*3.6

        def eBrakePressed(self):
                self.maxAcceleration = -2.73
                self.emergency = 1

        def serviceBrake(self):
                self.maxAcceleration = -1.2
                self.service = 1

        def brakesDone(self):
                self.maxAcceleration = 0.5
                self.emergency = 0
                self.brake = 0
                self.service = 0

        def openDoors(self):
                if(self.stationDoors!=-1 or self.doorStatus == 1):
                        self.doorStatus=True
                else:
                        self.doorStatus=False