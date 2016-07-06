from operator import attrgetter

class Violation(object):

    def __init__(self, v_id,
                 inspection_id,
                 category,
                 violation_date,
                 violation_date_closed,
                 violation_type):
        self.v_id = v_id
        self.inspection_id = inspection_id
        self.category = category
        self.violation_date = violation_date
        self.violation_date_closed = violation_date_closed
        self.violation_type = violation_type


class CategoryResult(object):
    def __init__(self, name):
        self.name = name
        self.violations = []

    @property
    def number_of_violations(self):
        return len(self.violations)

    @property
    def first_violation(self):
        sorted_list = sorted(self.violations, key=attrgetter('violation_date'))
        return sorted_list[0].violation_date

    @property
    def last_violation(self):
        sorted_list = sorted(self.violations, key=attrgetter('violation_date'), reverse=True)
        return sorted_list[0].violation_date
