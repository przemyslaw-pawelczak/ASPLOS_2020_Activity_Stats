# MIT License
#
# Copyright (c) 2020 Przemysław Pawełczak.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import matplotlib.pyplot as plt
import numpy as np

# Data collected manually on March 22, 2020 between 16:30PM and 16:50PM (two days after official end of a conference)
# by inspecting video clicks one by one at https://www.youtube.com/playlist?list=PLsLWHLZB96VeVp3IVzvSH58ttVz_Anr7H

# Naming of videos: [session name] - [firs three letters of video]
titles = [
    'Intr (Lar.)', # https://www.youtube.com/watch?v=TqZDSx4VENo
    'Intr (Cez./Str.)', # https://www.youtube.com/watch?v=hFn_VLjlX3g
    'Most Infl.', # https://www.youtube.com/watch?v=5c0IhQ07Hfo
    '1A - Shr', # https://www.youtube.com/watch?v=AmT0efuE4F8
    '1A - DNN', # https://www.youtube.com/watch?v=jdicv_HPUKA
    '1A - Gam', # https://www.youtube.com/watch?v=3_8sx5kkeBY
    '1B - Rel', # https://www.youtube.com/watch?v=sOCKZ8zDV14
    '1B - For', # https://www.youtube.com/watch?v=2E-y2FTuliU
    '1B - Tim', # https://www.youtube.com/watch?v=mxOGDBHs0YE
    '2A - IOc', # https://www.youtube.com/watch?v=RXBYjiVdsY8
    '2A - Lyn', # https://www.youtube.com/watch?v=W-PUkuY7zYQ
    '2B - Ega', # https://www.youtube.com/watch?v=9Mv0-PfiXeg
    '2B - Noi', # https://www.youtube.com/watch?v=7PU-6cWQQkE
    '3A - Rep', # https://www.youtube.com/watch?v=NuDIZqBdM08
    '3A - Ato', # https://www.youtube.com/watch?v=pJfl3_hWzQ4
    '3A - Her', # https://www.youtube.com/watch?v=5HwOdAjqEdE
    '3B - Fle', # https://www.youtube.com/watch?v=sOV_cz-1CWQ
    '3B - Acc', # https://www.youtube.com/watch?v=FB_2h5UyH1o
    '3B - Why', # https://www.youtube.com/watch?v=ShcjkBDs8TI
    '4A - Osi', # https://www.youtube.com/watch?v=cdwDaBmltfA
    '4A - Mit', # https://www.youtube.com/watch?v=ON0dmv7NJv8
    '4A - Hai', # https://www.youtube.com/watch?v=7-X9cXdNA1g
    '4B - Dur', # https://www.youtube.com/watch?v=_Ddw2cul7-4
    '4B - Pea', # https://www.youtube.com/watch?v=Gbl4sUcaESg
    '4B - Per', # https://www.youtube.com/watch?v=J20mjew4Edg
    '5A - Int', # https://www.youtube.com/watch?v=vy3s6VZr8TQ
    '5A - Dee', # https://www.youtube.com/watch?v=5c53T7riN2k
    '5A - Pra', # https://www.youtube.com/watch?v=nMcSXyVybJE
    '5B - Liv', # https://www.youtube.com/watch?v=Vu_ibDPRjOU
    '5B - A C', # https://www.youtube.com/watch?v=6lOKmsH_cz8
    '5B - Cry', # https://www.youtube.com/watch?v=aa_ItbK6S1I
    '6A - Cat', # https://www.youtube.com/watch?v=nMu_wFy_ZRc
    '6A - Hig', # https://www.youtube.com/watch?v=M5eUkygcc88
    '6A - Dat', # https://www.youtube.com/watch?v=zYo9n-nQCp8
    '6B - Cla', # https://www.youtube.com/watch?v=bpLl6PfUcmw
    '6B - The', # https://www.youtube.com/watch?v=w0e0Q-Vp01U
    '6B - Lea', # https://www.youtube.com/watch?v=gs8m5W-xdDM
    '7A - Opt', # https://www.youtube.com/watch?v=h_rtm1IjEiI
    '7A - HaR', # https://www.youtube.com/watch?v=2EHEyiwfEho
    '7A - Lea', # https://www.youtube.com/watch?v=Gyn9eABQwTQ
    '7B - Cha', # https://www.youtube.com/watch?v=jRo4SdNrIKY
    '7B - Vor', # https://www.youtube.com/watch?v=yF9j_KgH1_U
    '7B - Fle', # https://www.youtube.com/watch?v=4nQu9zt0AHk
    '8A - Hur', # https://www.youtube.com/watch?v=QdE2Ec7HlAo
    '8A - Exp', # https://www.youtube.com/watch?v=OLQshI-1KBc
    '8A - A B', # https://www.youtube.com/watch?v=Kq5KJ1NWd-s
    '8B - BYO', # https://www.youtube.com/watch?v=iQKkSgUGGk4
    '8B - Fir', # https://www.youtube.com/watch?v=42_5q-NPYyM
    '8B - Acc', # https://www.youtube.com/watch?v=H1a6FPFKG4A
    '9A - Asy', # https://www.youtube.com/watch?v=qo8gDbQyp6c
    '9A - MOD', # https://www.youtube.com/watch?v=IKVOc7zOiDA
    '9A - Pro', # https://www.youtube.com/watch?v=5v0wHFlIumQ
    '9B - AvA', # https://www.youtube.com/watch?v=vkU36Bt01BM
    '9B - A H', # https://www.youtube.com/watch?v=qPjpDfqIEmw
    '9B - Vir', # https://www.youtube.com/watch?v=bGy4s4f72_Q
    '10A - Fle', # https://www.youtube.com/watch?v=Ee15mcGc8RA
    '10A - Aut', # https://www.youtube.com/watch?v=flTN3H6-uLM
    '10A - Cap', # https://www.youtube.com/watch?v=eBF6Rq3w3GM
    '10B - Pat', # https://www.youtube.com/watch?v=c3X2WtoNdx0
    '10B - Cot', # https://www.youtube.com/watch?v=gI_GXiUb6Yo
    '10B - Orb', # https://www.youtube.com/watch?v=ft1R4kWky6U
    '11A - Occ', # https://www.youtube.com/watch?v=9IxpI_R_bSU
    '11A - COI', # https://www.youtube.com/watch?v=oL6aACFCrLA
    '11A - MER', # https://www.youtube.com/watch?v=96OUTHkBdY0
    '11B - Sof', # https://www.youtube.com/watch?v=xEEOHa6PnJU
    '11B - Qua', # https://www.youtube.com/watch?v=KaTjniXU0bc
    '11B - Tow', # https://www.youtube.com/watch?v=ipKND_bi3b8
    '12A - SAC', # https://www.youtube.com/watch?v=IJanO9NCDsQ
    '12A - Fai', # https://www.youtube.com/watch?v=WVpCYwS-sqs
    '12A - Fla', # https://www.youtube.com/watch?v=TCq6iLuVRHE
    '12B - Ela', # https://www.youtube.com/watch?v=BIvpGx-znlk
    '12B - Neu', # https://www.youtube.com/watch?v=oiqo35EDM7U
    '12B - Saf', # https://www.youtube.com/watch?v=auKcSndPjuw
    '13A - Eff', # https://www.youtube.com/watch?v=Pb1jh-70wxo
    '13A - HMC', # https://www.youtube.com/watch?v=h3x9GPFIYFE
    '13A - Laz', # https://www.youtube.com/watch?v=rE0dpTosYjE
    '13B - Opt', # https://www.youtube.com/watch?v=I86IoSmnFHo
    '13B - The', # https://www.youtube.com/watch?v=Lu6XuSPkRFw
    '13B - IIU', # https://www.youtube.com/watch?v=C2z3ogzDEaI
    '13B - Chr', # https://www.youtube.com/watch?v=B5U-J_fKVFY
    '14A - Klo', # https://www.youtube.com/watch?v=Zaf7k_mAw0E
    '14A - The', # https://www.youtube.com/watch?v=xyM28XmH_DA
    '14A - HEA', # https://www.youtube.com/watch?v=YQ51Q-DhoQo
    '14B - Dim', # https://www.youtube.com/watch?v=QzpjawIJn14
    '14B - Swa', # https://www.youtube.com/watch?v=RhV_TAgDJyc
    '14B - Bat', # https://www.youtube.com/watch?v=jMfQEZNvhg8
    '14B - HSM', # https://www.youtube.com/watch?v=uvO_iLY-iQk
]

views = [
    682, # 'Intr (Lar.)', # https://www.youtube.com/watch?v=TqZDSx4VENo
    597, # 'Intr (Cez./Str.)', # https://www.youtube.com/watch?v=hFn_VLjlX3g
    587, # 'Most Infl.', # https://www.youtube.com/watch?v=5c0IhQ07Hfo
    481, # '1A - Shr', # https://www.youtube.com/watch?v=AmT0efuE4F8
    190, # '1A - DNN', # https://www.youtube.com/watch?v=jdicv_HPUKA
    414, # '1A - Gam', # https://www.youtube.com/watch?v=3_8sx5kkeBY
    212, # '1B - Rel', # https://www.youtube.com/watch?v=sOCKZ8zDV14
    151, # '1B - For', # https://www.youtube.com/watch?v=2E-y2FTuliU
    130, # '1B - Tim', # https://www.youtube.com/watch?v=mxOGDBHs0YE
    334, # '2A - IOc', # https://www.youtube.com/watch?v=RXBYjiVdsY8
    347, # '2A - Lyn', # https://www.youtube.com/watch?v=W-PUkuY7zYQ
    338, # '2B - Ega', # https://www.youtube.com/watch?v=9Mv0-PfiXeg
    107, # '2B - Noi', # https://www.youtube.com/watch?v=7PU-6cWQQkE
    151, # '3A - Rep', # https://www.youtube.com/watch?v=NuDIZqBdM08
    116, # '3A - Ato', # https://www.youtube.com/watch?v=pJfl3_hWzQ4
    208, # '3A - Her', # https://www.youtube.com/watch?v=5HwOdAjqEdE
    92,  # '3B - Fle', # https://www.youtube.com/watch?v=sOV_cz-1CWQ
    85,  # '3B - Acc', # https://www.youtube.com/watch?v=FB_2h5UyH1o
    177, # '3B - Why', # https://www.youtube.com/watch?v=ShcjkBDs8TI
    167, # '4A - Osi', # https://www.youtube.com/watch?v=cdwDaBmltfA
    144, # '4A - Mit', # https://www.youtube.com/watch?v=ON0dmv7NJv8
    130, # '4A - Hai', # https://www.youtube.com/watch?v=7-X9cXdNA1g
    187, # '4B - Dur', # https://www.youtube.com/watch?v=_Ddw2cul7-4
    69,  # '4B - Pea', # https://www.youtube.com/watch?v=Gbl4sUcaESg
    158, # '4B - Per', # https://www.youtube.com/watch?v=J20mjew4Edg
    139, # '5A - Int', # https://www.youtube.com/watch?v=vy3s6VZr8TQ
    107, # '5A - Dee', # https://www.youtube.com/watch?v=5c53T7riN2k
    107, # '5A - Pra', # https://www.youtube.com/watch?v=nMcSXyVybJE
    173, # '5B - Liv', # https://www.youtube.com/watch?v=Vu_ibDPRjOU
    117, # '5B - A C', # https://www.youtube.com/watch?v=6lOKmsH_cz8
    135, # '5B - Cry', # https://www.youtube.com/watch?v=aa_ItbK6S1I
    141, # '6A - Cat', # https://www.youtube.com/watch?v=nMu_wFy_ZRc
    194, # '6A - Hig', # https://www.youtube.com/watch?v=M5eUkygcc88
    157, # '6A - Dat', # https://www.youtube.com/watch?v=zYo9n-nQCp8
    293, # '6B - Cla', # https://www.youtube.com/watch?v=bpLl6PfUcmw
    153, # '6B - The', # https://www.youtube.com/watch?v=w0e0Q-Vp01U
    545, # '6B - Lea', # https://www.youtube.com/watch?v=gs8m5W-xdDM
    87,  # '7A - Opt', # https://www.youtube.com/watch?v=h_rtm1IjEiI
    101,  # '7A - HaR', # https://www.youtube.com/watch?v=2EHEyiwfEho
    126, # '7A - Lea', # https://www.youtube.com/watch?v=Gyn9eABQwTQ
    132, # '7B - Cha', # https://www.youtube.com/watch?v=jRo4SdNrIKY
    111, # '7B - Vor', # https://www.youtube.com/watch?v=yF9j_KgH1_U
    122, # '7B - Fle', # https://www.youtube.com/watch?v=4nQu9zt0AHk
    72,  # '8A - Hur', # https://www.youtube.com/watch?v=QdE2Ec7HlAo
    337, # '8A - Exp', # https://www.youtube.com/watch?v=OLQshI-1KBc
    115, # '8A - A B', # https://www.youtube.com/watch?v=Kq5KJ1NWd-s
    210, # '8B - BYO', # https://www.youtube.com/watch?v=iQKkSgUGGk4
    184, # '8B - Fir', # https://www.youtube.com/watch?v=42_5q-NPYyM
    395, # '8B - Acc', # https://www.youtube.com/watch?v=H1a6FPFKG4A
    99,  # '9A - Asy', # https://www.youtube.com/watch?v=qo8gDbQyp6c
    71,  # '9A - MOD', # https://www.youtube.com/watch?v=IKVOc7zOiDA
    104,  # '9A - Pro', # https://www.youtube.com/watch?v=5v0wHFlIumQ
    92,  # '9B - AvA', # https://www.youtube.com/watch?v=vkU36Bt01BM
    112, # '9B - A H', # https://www.youtube.com/watch?v=qPjpDfqIEmw
    121, # '9B - Vir', # https://www.youtube.com/watch?v=bGy4s4f72_Q
    164, # '10A - Fle', # https://www.youtube.com/watch?v=Ee15mcGc8RA
    114, # '10A - Aut', # https://www.youtube.com/watch?v=flTN3H6-uLM
    81,  # '10A - Cap', # https://www.youtube.com/watch?v=eBF6Rq3w3GM
    104, # '10B - Pat', # https://www.youtube.com/watch?v=c3X2WtoNdx0
    79,  # '10B - Cot', # https://www.youtube.com/watch?v=gI_GXiUb6Yo
    165, # '10B - Orb', # https://www.youtube.com/watch?v=ft1R4kWky6U
    90,  # '11A - Occ', # https://www.youtube.com/watch?v=9IxpI_R_bSU
    65,  # '11A - COI', # https://www.youtube.com/watch?v=oL6aACFCrLA
    60,  # '11A - MER', # https://www.youtube.com/watch?v=96OUTHkBdY0
    61,  # '11B - Sof', # https://www.youtube.com/watch?v=xEEOHa6PnJU
    67,  # '11B - Qua', # https://www.youtube.com/watch?v=KaTjniXU0bc
    72,  # '11B - Tow', # https://www.youtube.com/watch?v=ipKND_bi3b8
    52,  # '12A - SAC', # https://www.youtube.com/watch?v=IJanO9NCDsQ
    50,  # '12A - Fai', # https://www.youtube.com/watch?v=WVpCYwS-sqs
    95,  # '12A - Fla', # https://www.youtube.com/watch?v=TCq6iLuVRHE
    329, # '12B - Ela', # https://www.youtube.com/watch?v=BIvpGx-znlk
    136, # '12B - Neu', # https://www.youtube.com/watch?v=oiqo35EDM7U
    58,  # '12B - Saf', # https://www.youtube.com/watch?v=auKcSndPjuw
    81,  # '13A - Eff', # https://www.youtube.com/watch?v=Pb1jh-70wxo
    79,  # '13A - HMC', # https://www.youtube.com/watch?v=h3x9GPFIYFE
    141, # '13A - Laz', # https://www.youtube.com/watch?v=rE0dpTosYjE
    119, # '13B - Opt', # https://www.youtube.com/watch?v=I86IoSmnFHo
    57,  # '13B - The', # https://www.youtube.com/watch?v=Lu6XuSPkRFw
    72,  # '13B - IIU', # https://www.youtube.com/watch?v=C2z3ogzDEaI
    117, # '13B - Chr', # https://www.youtube.com/watch?v=B5U-J_fKVFY
    74,  # '14A - Klo', # https://www.youtube.com/watch?v=Zaf7k_mAw0E
    133, # '14A - The', # https://www.youtube.com/watch?v=xyM28XmH_DA
    100, # '14A - HEA', # https://www.youtube.com/watch?v=YQ51Q-DhoQo
    80,  # '14B - Dim', # https://www.youtube.com/watch?v=QzpjawIJn14
    116, # '14B - Swa', # https://www.youtube.com/watch?v=RhV_TAgDJyc
    167, # '14B - Bat', # https://www.youtube.com/watch?v=jMfQEZNvhg8
    93,  # '14B - HSM', # https://www.youtube.com/watch?v=uvO_iLY-iQk
]

# Calculate stats for technical talks only
mean_views = round(np.mean(views[3:len(views)]),1) # mean views
median_views = round(np.median(views[3:len(views)]),1) # median views

# Sort views in descending order
titles = [x for _,x in sorted(zip(views, titles), reverse = True)]
views = sorted(views, reverse = True)

font_size = 7 # figure font size
width = 0.5 # bar width

y_pos = np.arange(len(titles)) # position of bars
plt.figure(figsize = (12, 3)) # figure size
plt.rc('ytick', labelsize = font_size) # change ytick size
ax = plt.subplot() # create subplot
ax.bar(y_pos, views) # plot bars
ax.set_xlabel('Video name ([session code] - [first three letters of a title])', fontsize = font_size) # set x label
ax.set_ylabel('Number of views', fontsize = font_size) # set y label
ax.set_title('ASPLOS 2020 YouTube channel: number of views per video (collected manually on March 22, 2020 '
             'from 16:30PM to 16:50PM CET - two days after conference completion)',
             fontsize = font_size, fontweight = 'bold') # set title
plt.xticks(y_pos, titles, rotation = 90, fontsize = font_size, zorder = 100, ha = 'center',
           color = 'black') # set x ticks bar properties

# annotate graph with statistics
plt.annotate('for technical presentations only - ',
             xy = (0.1, 0.85),
             xycoords = 'axes fraction',
             fontsize = font_size,
             color = 'red')

text_annotation = 'mean: ' + str(mean_views) + ' views; ' + ' median: ' + str(median_views) + ' views'

plt.annotate(text_annotation,
             xy = (0.25, 0.85),
             xycoords = 'axes fraction',
             fontsize = font_size,
             color = 'red')

plt.tight_layout() # tight figure layout
plt.show() # show figure