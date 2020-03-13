from datetime import date
from .. import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('NL')
class Netherlands(WesternCalendar, ChristianMixin):
    'Netherlands'

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 5, _("Liberation Day")),
    )

    def get_king_queen_day(self, year):
        """27 April unless this is a Sunday in which case it is the 26th

        Before 2013 it was called Queensday, falling on
        30 April, unless this is a Sunday in which case it is the 29th.
        """
        if year > 2013:
            if date(year, 4, 27).weekday() != 6:
                return date(year, 4, 27), _("King's day")
            else:
                return date(year, 4, 26), _("King's day")
        else:
            if date(year, 4, 30).weekday() != 6:
                return date(year, 4, 30), _("Queen's day")
            else:
                return date(year, 4, 29), _("Queen's day")

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_king_queen_day(year))
        return days
