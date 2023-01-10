from statistics import mode
from collections import Counter


class TrackOrders:
    def __init__(self) -> None:
        self.orders = []
        self.customerOrders = []
        self.neverOrdered = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        orders = self.orders
        cOrders = self.customerOrders
        for order in orders:
            if order[0] == customer:
                cOrders.append(order[1])
      
        return mode(cOrders)

    def get_never_ordered_per_customer(self, customer):
        orders = self.orders
        cDishes = self.customerOrders
        neverOrderes = self.neverOrdered
        for order in orders:
            if order[0] == customer:
                cDishes.append(order[1])
        for dish in orders:
            if dish[1] not in cDishes:
                neverOrderes.add(dish[1])
        
        return neverOrderes


    def get_days_never_visited_per_customer(self, customer):
        orders = self.orders
        cDays = self.customerOrders
        neverOrderes = self.neverOrdered
        for order in orders:
            if order[0] == customer:
                cDays.append(order[2])
        for day in orders:
            if day[2] not in cDays:
                neverOrderes.add(day[2])
        
        return neverOrderes

    def get_busiest_day(self):
        orders = self.orders
        days = self.customerOrders
        for day in orders:
            days.append(day[2])
        
        return mode(days)

    def get_least_busy_day(self):
        orders = self.orders
        days = self.customerOrders
        for day in orders:
            days.append(day[2])
        
        return Counter(days).most_common()[-1][0]
