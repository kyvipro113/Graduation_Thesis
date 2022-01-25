from DAL.DAL_StatisticVisit import DAL_StatisticVisit

class BUS_StatisticVisit():
    def __init__(self):
        self.dalStatisticVisit = DAL_StatisticVisit()

    def loadAllVisitTime(self):
        return self.dalStatisticVisit.selectAllVisitTime()

    def loadVisitTimeViaDay(self, day):
        return self.dalStatisticVisit.selectVisitTimeViaDay(day=day)

    def loadVisitTimeViaMonth(self, month):
        return self.dalStatisticVisit.selectVisitTimeViaMonth(month=month)

    def loadVisitTimeViaYear(self, year):
        return self.dalStatisticVisit.selectVisitTimeViaYear(year=year)