from calendar import monthrange

class CloudCost():
    def lambda_execution(self):
        return (0.0000002 + 3*0.0002080)

    def app_execution(self, execution_times):
        exec_cost = self.lambda_execution()
        return execution_times*(0.0000004 + 2*exec_cost)

    def month(self, execution_times, month_of_year):
        return monthrange(2019,month_of_year)[1]*self.app_execution(execution_times)
    
    def year(self, execution_times):
        result = []
        for i in range(1,13):
            result.append(self.month(execution_times,i))
        return result
