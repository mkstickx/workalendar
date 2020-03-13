from .. import gettext as _
from ..core import WesternCalendar, IslamicMixin
from ..registry_tools import iso_register


@iso_register('DZ')
class Algeria(WesternCalendar, IslamicMixin):
    "Algeria"
    # Islamic holidays
    include_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_islamic_new_year = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, _("Labour Day")),
        (7, 5, _("Independence Day")),
        (11, 1, _("Anniversary of the revolution")),
    )

    ISLAMIC_HOLIDAYS = IslamicMixin.ISLAMIC_HOLIDAYS + (
        (1, 10, _("Ashura")),
    )
