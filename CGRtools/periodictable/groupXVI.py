# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Dayana Bashirova <dayana.bashirova@yandex.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
#  Copyright 2019 Tansu Nasyrova <tansu.nasyrova@gmail.com>
#  This file is part of CGRtools.
#
#  CGRtools is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#
from .element import Element, FrozenDict
from .groups import GroupXVI
from .periods import PeriodII, PeriodIII, PeriodIV, PeriodV, PeriodVI, PeriodVII


class O(Element, PeriodII, GroupXVI):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 8

    @property
    def isotopes_distribution(self):
        return FrozenDict({16: 0.99757, 17: 0.00038, 18: 0.00205})

    @property
    def isotopes_masses(self):
        return FrozenDict({16: 15.994915, 17: 16.999132, 18: 17.99916})

    @property
    def _common_valences(self):
        return 2,

    @property
    def _valences_exceptions(self):
        return (-1, False, 1, ()), (0, True, 1, ()), (1, False, 0, ((3, 'C'),))


class S(Element, PeriodIII, GroupXVI):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 16

    @property
    def isotopes_distribution(self):
        return FrozenDict({32: 0.9493, 33: 0.0076, 34: 0.0429, 36: 0.0002})

    @property
    def isotopes_masses(self):
        return FrozenDict({32: 31.972071, 33: 32.971458, 34: 33.967867, 36: 35.967081})

    @property
    def _common_valences(self):
        return 2,

    @property
    def _valences_exceptions(self):
        return ((-1, False, 1, ()),
                (0, False, 0, ((2, 'O'), (2, 'O'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (2, 'O'))),

                (0, False, 0, ((2, 'O'), (1, 'O'), (1, 'O'))),
                (0, False, 0, ((2, 'O'), (1, 'Cl'), (1, 'Cl'))),
                (0, False, 0, ((2, 'O'), (1, 'C'), (1, 'C'))),

                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'O'), (1, 'O'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'Cl'), (1, 'Cl'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'C'), (1, 'Cl'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'C'), (1, 'O'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'C'), (1, 'C'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'O'), (1, 'S'))),  # [S2O3]2-
                (0, False, 0, ((2, 'O'), (2, 'S'), (1, 'O'), (1, 'O'))),  # [S2O3]2-

                (0, False, 0, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))))


class Se(Element, PeriodIV, GroupXVI):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 34

    @property
    def isotopes_distribution(self):
        return FrozenDict({74: 0.0089, 76: 0.0937, 77: 0.0763, 78: 0.2377, 80: 0.4961, 82: 0.0873})

    @property
    def isotopes_masses(self):
        return FrozenDict({74: 73.922477, 76: 75.919214, 77: 76.919915, 78: 77.91731, 80: 79.916522, 82: 81.9167})

    @property
    def _common_valences(self):
        return 2,

    @property
    def _valences_exceptions(self):
        return ((-1, False, 1, ()),
                (0, False, 0, ((2, 'O'), (2, 'O'))),
                (0, False, 0, ((2, 'S'), (2, 'S'))),

                (0, False, 0, ((2, 'O'), (1, 'O'), (1, 'O'))),
                (0, False, 0, ((2, 'O'), (1, 'Cl'), (1, 'Cl'))),
                (0, False, 0, ((2, 'O'), (1, 'F'), (1, 'F'))),

                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'O'), (1, 'O'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'Cl'), (1, 'Cl'))),

                (0, False, 0, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))))


class Te(Element, PeriodV, GroupXVI):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 52

    def isotopes_distribution(self):
        return FrozenDict({120: 0.0009, 122: 0.0255, 123: 0.0089, 124: 0.0474, 125: 0.0707, 126: 0.1884, 128: 0.3174,
                           130: 0.3408})

    @property
    def isotopes_masses(self):
        return FrozenDict({120: 119.90402, 122: 121.903047, 123: 122.904273, 124: 123.90282, 125: 124.904425,
                           126: 125.903306, 128: 127.904461, 130: 129.906223})

    @property
    def _common_valences(self):
        return 2,

    @property
    def _valences_exceptions(self):
        return ((0, False, 0, ((2, 'O'), (2, 'O'))),
                (0, False, 0, ((2, 'O'), (1, 'O'), (1, 'O'))),

                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'O'), (1, 'O'))),
                (0, False, 0, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),
                (0, False, 0, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, False, 0, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'O'))))


class Po(Element, PeriodVI, GroupXVI):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 84

    @property
    def isotopes_distribution(self):
        return FrozenDict({210: 1.0})

    @property
    def isotopes_masses(self):
        return FrozenDict({210: 209.982874})

    @property
    def _common_valences(self):
        return 0, 2

    @property
    def _valences_exceptions(self):
        return ((0, False, 0, ((2, 'O'), (2, 'O'), (2, 'O'))),
                (0, False, 0, ((2, 'O'), (2, 'O'))),
                (0, False, 0, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),
                (0, False, 0, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))),
                (0, False, 0, ((1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'))),
                (0, False, 0, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))))


class Lv(Element, PeriodVII, GroupXVI):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 116

    @property
    def isotopes_distribution(self):
        return FrozenDict({293: 1.0})

    @property
    def isotopes_masses(self):
        return FrozenDict({293: 293.204555})

    @property
    def _common_valences(self):
        return 0,

    @property
    def _valences_exceptions(self):
        return ()


__all__ = ['O', 'S', 'Se', 'Te', 'Po', 'Lv']