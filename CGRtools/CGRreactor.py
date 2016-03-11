# -*- coding: utf-8 -*-
#
# Copyright 2014-2016 Ramil Nugmanov <stsouko@live.ru>
# This file is part of cgrtools.
#
# cgrtools is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
import operator
from collections import defaultdict
from networkx.algorithms import isomorphism as gis
import networkx as nx


class CGRReactor(object):
    def __init__(self, stereo):
        self.__rctemplate = self.__reactioncenter()
        stereo = (['s_stereo', 'p_stereo', 'sp_stereo'], [None] * 3,
                  [operator.eq] * 2 + [lambda a, b: a in b if b is not None else True]) if stereo else ([], [], [])
        pstereo = (['p_stereo'], [None], [operator.eq]) if stereo else ([], [], [])

        self.__node_match = gis.generic_node_match(['element', 's_charge', 'p_charge', 'isotop'] + stereo[0],
                                                   [None] * 4 + stereo[1],
                                                   [lambda a, b: a in b if
                                                   isinstance(b, list) else a == b if b is not None else True] * 3 +
                                                   [lambda a, b: a == b if b is not None else True] + stereo[2])
        self.__edge_match = gis.categorical_edge_match(['s_bond', 'p_bond'] + stereo[0], [None] * 2 + stereo[1])

        self.__node_match_products = gis.categorical_node_match(['element', 'isotop', 'p_charge'] + pstereo[0],
                                                                [None] * 3 + pstereo[1])
        self.__edge_match_products = gis.categorical_edge_match(['p_bond'] + pstereo[0], [None] + pstereo[1])

        self.__edge_match_only_bond = gis.categorical_edge_match(['s_bond', 'p_bond'], [None] * 2)

    @staticmethod
    def __reactioncenter():
        g1 = nx.Graph()
        g2 = nx.Graph()
        g3 = nx.Graph()
        g1.add_edges_from([(1, 2, dict(s_bond=1, p_bond=None)), (2, 3, dict(s_bond=None, p_bond=1)),
                           (3, 4, dict(s_bond=1, p_bond=None))])
        g2.add_edges_from([(1, 2, dict(s_bond=1, p_bond=None)), (2, 3, dict(s_bond=None, p_bond=1))])

        g3.add_edges_from([(1, 2, dict(s_bond=None, p_bond=1))])
        return g1, g2, g3

    def spgraphmatcher(self, g, h):
        return gis.GraphMatcher(g, h, node_match=self.__node_match, edge_match=self.__edge_match)

    def searchtemplate(self, templates, patch=True):
        def searcher(g):
            for i in templates:
                gm = self.spgraphmatcher(g, i['substrats'])
                for j in gm.subgraph_isomorphisms_iter():

                    res = dict(substrats=g, meta=i['meta'],
                               products=self.__remapgroup(i['products'], g,
                                                          {y: x for x, y in j.items()})[0] if patch else None)
                    yield res

            return None

        return searcher

    @staticmethod
    def getbondbrokengraph(g, rc_templates, edge_match):
        g = g.copy()
        lose_map = {}
        lose_bonds = defaultdict(dict)
        for i in rc_templates:
            gm = gis.GraphMatcher(g, i, edge_match=edge_match)
            for j in gm.subgraph_isomorphisms_iter():
                mapping = {y: x for x, y in j.items()}
                if 3 in mapping:
                    lose_map[mapping[2]] = mapping[1]
                    lose_bonds[mapping[2]][mapping[1]] = g[mapping[1]][mapping[2]]
                    g.remove_edge(mapping[2], mapping[3])
                    if 4 in mapping:
                        # todo: есть проблема с ядром графа. можно проебать фрагментацию...
                        lose_map[mapping[3]] = mapping[4]
                        lose_bonds[mapping[3]][mapping[4]] = g[mapping[3]][mapping[4]]
                        g.remove_edge(mapping[3], mapping[4])

                    g.remove_edge(mapping[1], mapping[2])
                elif not any(nx.has_path(g, x, y) for y in lose_map for x in mapping.values()):
                    # запилить проверку связности атомов 1 или 2 с lose_map атомами
                    g.remove_edge(mapping[1], mapping[2])
        components = list(nx.connected_component_subgraphs(g))
        return components, lose_bonds, lose_map

    def clonesubgraphs(self, g):
        r_group = {}
        x_group = {}
        r_group_clones = defaultdict(list)
        newcomponents = []

        ''' search bond breaks and creations
        '''
        components, lose_bonds, lose_map = self.getbondbrokengraph(g, self.__rctemplate,
                                                                   self.__edge_match_only_bond)
        ''' extract subgraphs and sort by group type (R or X)
        '''
        setlose = set(lose_map.values())
        setlosekey = set(lose_map)

        for i in components:
            x_terminal_atom = setlose.intersection(i)
            r_terminal_atom = setlosekey.intersection(i)

            if x_terminal_atom:
                x_group[x_terminal_atom.pop()] = i
            elif r_terminal_atom:
                r_group[r_terminal_atom.pop()] = i
            else:
                newcomponents.append(i)
        ''' search similar R groups and patch.
        '''
        tmp = g.copy()
        for i in newcomponents:
            for k, j in r_group.items():
                gm = gis.GraphMatcher(j, i, node_match=self.__node_match_products,
                                      edge_match=self.__edge_match_products)
                ''' search for similar R-groups started from bond breaks.
                '''
                mapping = next((x for x in gm.subgraph_isomorphisms_iter() if k in x), None)
                if mapping:
                    r_group_clones[k].append(mapping[k])
                    tmp = nx.compose(tmp, self.__remapgroup(j, tmp, mapping)[0])
                    break
        ''' add lose X groups to R groups
        '''
        for i, j in r_group_clones.items():
            for k in j:
                remappedgroup, mapping = self.__remapgroup(x_group[lose_map[i]], tmp, {})
                tmp = nx.union(tmp, remappedgroup)
                tmp.add_edge(k, mapping[lose_map[i]], attr_dict=lose_bonds[i][lose_map[i]])

        return tmp

    @staticmethod
    def __remapgroup(g, h, mapping):
        newmap = mapping.copy()
        newmap.update({x: y for x, y in zip(set(g).difference(newmap), set(range(1, 1000)).difference(h))})
        return nx.relabel_nodes(g, newmap, copy=True), newmap