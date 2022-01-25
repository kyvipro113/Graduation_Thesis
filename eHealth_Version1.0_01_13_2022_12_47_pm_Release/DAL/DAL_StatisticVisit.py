from SQL.SQLConnection import SQLConnection

class DAL_StatisticVisit(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectVisitTimeViaDay(self, day):
        data = self.queryDataOnly1("Select COUNT(*) From Patient Where DAY(Time) = {}".format(day))
        return data

    def selectVisitTimeViaMonth(self, month):
        data = self.queryDataOnly1("Select COUNT(*) From Patient Where MONTH(Time) = {}".format(month))
        return data

    def selectVisitTimeViaYear(self, year):
        data = self.queryDataOnly1("Select COUNT(*) From Patient Where YEAR(Time) = {}".format(year))
        return data

    def selectAllVisitTime(self):
        data = self.queryDataOnly1("Select COUNT(*) From Patient")
        return data
