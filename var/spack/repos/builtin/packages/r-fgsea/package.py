##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RFgsea(RPackage):
    """The package implements an algorithm for fast gene set enrichment
    analysis. Using the fast algorithm allows to make more permutations
    and get more fine grained p-values, which allows to use accurate
    stantard approaches to multiple hypothesis correction."""

    homepage = "https://www.bioconductor.org/packages/fgsea/"
    url      = "https://git.bioconductor.org/packages/fgsea"

    version('1.2.1', git='https://git.bioconductor.org/packages/fgsea', commit='99b04eef664204d0dca4b9f8027cd7eefb006b72')

    depends_on('r@3.4.0:3.4.9', when='@1.2.1')
    depends_on('r-fastmatch', type=('build', 'run'))
    depends_on('r-gridextra', type=('build', 'run'))
    depends_on('r-ggplot2', type=('build', 'run'))
    depends_on('r-biocparallel', type=('build', 'run'))
    depends_on('r-data-table', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'))
