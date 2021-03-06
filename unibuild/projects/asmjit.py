# Copyright (C) 2015 Sebastian Herbord. All rights reserved.
#
# This file is part of Mod Organizer.
#
# Mod Organizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mod Organizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mod Organizer.  If not, see <http://www.gnu.org/licenses/>.


from unibuild import Project
from unibuild.modules import cmake, github
from config import config


# asmjit doesn't currently have any tags/branches but not every commit is usable
asmjit_tag = "31c0b467101bf53d15c8f0cbc2d40107a9ff1ea6"


Project("AsmJit") \
    .depend(cmake.CMake().arguments(
    [
        "-DASMJIT_STATIC=TRUE",
        "-DASMJIT_DISABLE_COMPILER=TRUE",
        "-DCMAKE_INSTALL_PREFIX:PATH={}/install".format(config['__build_base_path'].replace('\\', '/')),
        "-DCMAKE_BUILD_TYPE={0}".format(config["build_type"]),
    ]).install()
            .depend(github.Source("kobalicek", "asmjit", asmjit_tag, update=False)
                    .set_destination("asmjit"))
            )

