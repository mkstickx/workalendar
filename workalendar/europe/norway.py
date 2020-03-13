from .. import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('NO')
class Norway(WesternCalendar, ChristianMixin):
    'Norway'

    include_holy_thursday = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_whit_sunday = True
    include_boxing_day = True
    boxing_day_label = _("St Stephen's Day")

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, _("Labour Day")),
        (5, 17, _("Constitution Day")),
    )
