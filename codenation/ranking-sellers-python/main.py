from operator import itemgetter
from functools import reduce
from decimal import *
import operator

class SellersRanking:
    def best_seller(self, sellers):
        #result = reduce((lambda x,y: x['name'] if int(x['value'])>=int(y['value']) else y['name']),sellers )
        if len(sellers)>1:
            result = reduce((lambda x,y: x if Decimal(x['value']) >= Decimal(y['value']) else y),sellers)
            return [result['name']]
        elif len(sellers)==1:
            return [sellers[0]['name']]
        else:
            return []


    def ranking_list(self, sellers):
        values = list(map(lambda x: Decimal(x['value']),sellers))
        values.sort()
        values.reverse()
        results = list(map(lambda x: list(filter(lambda y: Decimal(y['value'])==x,sellers)),values))
        results = reduce(operator.iconcat, results, [])
        results = list(map(lambda x: x['name'],results))
        return results


    def best_seller_store(self, sellers, store):
        sellers_to_eval = list(filter(lambda x: int(x['store'])==int(store),sellers))
        best = self.best_seller(sellers_to_eval)
        return best


    def sales_goals(self, sellers):
        sellers_under_goal = list(filter(lambda x: Decimal(x['value']) < Decimal(500),sellers))
        ranked_list = self.ranking_list(sellers_under_goal)
        ranked_list.reverse()
        return ranked_list


