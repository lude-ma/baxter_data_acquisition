#!/usr/bin/env python

# Copyright (c) 2016, BRML
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import argparse

import rospy


def main():
    parser = argparse.ArgumentParser(
            description='Record anomaly data on the baxter research robot.')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-l', '--limb', required=True,
                          choices=['left', 'right'],
                          help='The limb to record data from.')
    required.add_argument('-e', '--experiment', required=True,
                          choices=['randomized', 'fixed'],
                          help='The order of positions in the experiment.')
    parser.add_argument('-n', '--number', required=False,
                        type=int, default=1,
                        help='The number of samples to record.')
    parser.add_argument('-a', '--anomalies', required=False,
                        type=bool, default=False,
                        help='Whether there are anomalies in the data.')
    parser.add_argument('-i', '--images', required=False,
                        type=bool, default=False,
                        help='Whether images are to be recorded.')
    parser.add_argument('-t', '--threed', required=False,
                        type=bool, default=False,
                        help='Whether 3d point clouds are to be recorded.')
    args = parser.parse_args(rospy.myargv()[1:])

    print 'Initializing node ...'
    rospy.init_node('anomaly_data', anonymous=True)

    # Do anomaly data acquisition here.

    print 'Done.'

if __name__ == '__main__':
    main()
