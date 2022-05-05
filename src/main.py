import datetime as dt

class WashingMachine:
    def __init__(self,id):
        self.machineId = id # so the customer know what machine that they should use
        self.washprograms = [("Kokvask",60,90),("Tøyvask",40,60),("Håndvask",30,20)]
        self.reservations = list()
        self.reservationId = 0

    def reserveMachine(self, userId, resTime, resType ):
        duration = self.washprograms[resType][2] 
        resFrom = resTime
        resTo = resTime + dt.timedelta(minutes=duration)
        self.reservationId += 1
        self.reservations.append({"reservationId": self.reservationId,"userId": userId,"from": resFrom, "to":resTo})
        return (resFrom,resTo)
    
    def getReservationsByUserId(self, userId):
        reservationsByUserId = list()
        for reservation in self.reservations:
            if reservation["userId"] == userId:
                reservationsByUserId.append(reservation)
        return reservationsByUserId
    
    def findNextAvailableTime(self, type: int):
        duration = self.washprograms[type][2]
        lastReservation = None
        self.reservations.sort(key=lambda x: x["from"])
        for reservation in self.reservations:
            if lastReservation and (lastReservation["from"] - reservation["to"]).total_seconds() / 60 > duration:
                return lastReservation["to"]
            lastReservation = reservation
        if lastReservation:
            return (lastReservation["to"],dt.datetime.now())[lastReservation["to"] <= dt.datetime.now()]
        else:
            return dt.datetime.now()
    def removeReservation(self, reservationId):
        self.reservations[:] = [reservation for reservation in self.reservations if not reservation["reservationId"] == reservationId]

machinelist=[]
wm1 = WashingMachine("Vaskemaskin 1")
machinelist.append(wm1)
wm2 = WashingMachine("Vaskemaskin 2")
machinelist.append(wm2)
wm3 = WashingMachine("Vaskemaskin 3")
machinelist.append(wm3)
wm4 = WashingMachine("Vaskemaskin 4")
machinelist.append(wm4)
wm5 = WashingMachine("Vaskemaskin 5")
machinelist.append(wm5)
wm6 = WashingMachine("Vaskemaskin 6")
machinelist.append(wm6)
wm7 = WashingMachine("Vaskemaskin 7")
machinelist.append(wm7)
wm8 = WashingMachine("Vaskemaskin 8")
machinelist.append(wm8)
wm9 = WashingMachine("Vaskemaskin 9")
machinelist.append(wm9)
wm10 = WashingMachine("Vaskemaskin 10")
machinelist.append(wm10)
wm11 = WashingMachine("Vaskemaskin 11")
machinelist.append(wm11)
wm12 = WashingMachine("Vaskemaskin 12")
machinelist.append(wm12)

def reserveNextAvailableMachine(userId, type):
    bestMachine,bestTime = None,None
    for machine in machinelist:
        nextAvailable = machine.findNextAvailableTime(type)
        if bestTime:
            if nextAvailable < bestTime:
                bestTime = nextAvailable
                bestMachine = machine
        else:
            bestTime = nextAvailable
            bestMachine = machine
    reserved = bestMachine.reserveMachine(userId,bestTime,type)

    print(f"Reservert maskin: {bestMachine.machineId}")
    print(f"Dato: {reserved[0].strftime('%d/%m %Y')}")
    print(f"Fra: {reserved[0].strftime('%H:%M ')}")
    print(f"Til: {reserved[1].strftime('%H:%M')}")

def getAllReservationsByUserid(userId):
    allReservationsByUserid = list()
    
    for machine in machinelist:
        for reservation in machine.getReservationsByUserId(userId):
            allReservationsByUserid.append((machine, reservation))            
            
    return allReservationsByUserid

def menu_maker(header: str, options: list):
    print(f"{header:^40}")
    print("-" * 40)
    choice = None
    choices = list()
    for (index, description) in enumerate(options):
        choices.append(str(index))
        print(f"[{index}] {description}")
    choices.append("A")
    print("[A] Avbryt")
    print("-" * 40)
    while(choice not in choices):
        choice = input(f"Valg: ")
        choice = choice.capitalize()
    return choice

def login():
    userId = ""
    while len(userId) < 1:
        userId = input("Logg inn med identifikasjon: ")
    return userId

def main():
    userId = login()
    mainmenu = True
    while mainmenu:
        mainchoice = menu_maker("Washit",["Reserver vaskemaskin","Avlys reservasjon","Registrere på venteliste","Endre bruker"])
        if mainchoice == "0":
            washmenu = True
            while washmenu:
                washchoice = menu_maker("Hvordan type vask?",["Kokvask","Tøyvask","Håndvask"])
                if washchoice == "A":
                    washmenu = False
                else:
                    reserveNextAvailableMachine(userId,int(washchoice))
                    washmenu = False
        if mainchoice == "1":
            allReservations = getAllReservationsByUserid(userId)
            reservationmenulist = list()
            for reservation in allReservations:
                reservationmenulist.append(f"{reservation[1]['from'].strftime('%d/%m %Y %H:%M')} - {int((reservation[1]['to']-reservation[1]['from']).total_seconds() / 60)} minutes")
            
            deletechoice = menu_maker("Hvilke reservasjon vil du avlyse?", reservationmenulist)
            if deletechoice != "A":
                machine = allReservations[int(deletechoice)][0]
                reservationId = allReservations[int(deletechoice)][1]["reservationId"]
                machine.removeReservation(reservationId)
            
        if mainchoice == "2":
            # TODO Here i would create a function that registered users, contact information and timeslot needed
            # TODO I would also add in the Washingmachine.removeReservation functionin that would check this list for users would could fit in the deleted timeslot
            
            pass
        if mainchoice == "3":
            userId = login()
        if mainchoice == "A":
            mainmenu = False

main()