"""
tags : math, number theory
"""

import math

t = int(input())

for _ in range(t):

    a, b, c, m = list(map(int, input().split()))

    abc_lcm = math.lcm(a, b, c)
    abc_lcm_count = m // abc_lcm 

    ab_lcm = math.lcm(a, b)
    ab_lcm_count = m // ab_lcm

    bc_lcm = math.lcm(b, c)
    bc_lcm_count = m // bc_lcm

    ac_lcm = math.lcm(a, c)
    ac_lcm_count = m // ac_lcm

    water_a = abc_lcm_count * 2 + (ac_lcm_count + ab_lcm_count - 2 * abc_lcm_count) * 3 + ((m // a) - ac_lcm_count - ab_lcm_count + abc_lcm_count) * 6
    water_b = abc_lcm_count * 2 + (bc_lcm_count + ab_lcm_count - 2 * abc_lcm_count) * 3 + ((m // b) - bc_lcm_count - ab_lcm_count + abc_lcm_count) * 6
    water_c = abc_lcm_count * 2 + (bc_lcm_count + ac_lcm_count - 2 * abc_lcm_count) * 3 + ((m // c) - bc_lcm_count - ac_lcm_count + abc_lcm_count) * 6

    print(f'{water_a} {water_b} {water_c}')
