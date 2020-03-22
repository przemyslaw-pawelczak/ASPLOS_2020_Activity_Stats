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

# Data collected manually on March 22, 2020 between X and Y (two days after official end of a conference)
# by inspecting asplos2020.slack.com manually

channel_type = [
    'special_session', # 'best-paper-awards', # https://app.slack.com/client/TUCSNGTB4/CUFN31465/details/info
    'special_session', # 'waci', # https://app.slack.com/client/TUCSNGTB4/CUEBJBRUK/details/info
    'special_session', # 'most-influential-paper-awards', # https://app.slack.com/client/TUCSNGTB4/CUD1WR8CA/details/info
    'techical_session', # 'accelerators', # https://app.slack.com/client/TUCSNGTB4/CUP4PUSM8/details/info
    'techical_session', # 'memory_management', # https://app.slack.com/client/TUCSNGTB4/CURR70B89/details/info
    'chat', # 'jobs', # https://app.slack.com/client/TUCSNGTB4/CV83Z4EKC/details/info
    'techical_session', # 'memory_behavior', # https://app.slack.com/client/TUCSNGTB4/CUQE179NX/details/info
    'techical_session', # 'datacenter-cloud_power-performance', # https://app.slack.com/client/TUCSNGTB4/CV1TS3LRW/details/info
    'techical_session', # 'exotic_architectures', # https://app.slack.com/client/TUCSNGTB4/CUQE0HWKD/details/info
    'techical_session', # 'enclaves_and_memory_security', # https://app.slack.com/client/TUCSNGTB4/CV44LL29L/details/info
    'techical_session', # 'speculation_and_security', # https://app.slack.com/client/TUCSNGTB4/CURR56TTK/details/info
    'techical_session', # 'frameworks_for_deep_learning', # https://app.slack.com/client/TUCSNGTB4/CV3PR5C9M/details/info
    'techical_session', # 'security_with_little_performance_loss', # https://app.slack.com/client/TUCSNGTB4/CV1TVCKNC/details/info
    'techical_session', # 'huge_memories_and_distributed_databases', # https://app.slack.com/client/TUCSNGTB4/CV1TR1L4Q/details/info
    'techical_session', # 'privacy_and_security_in_machine_learning', # https://app.slack.com/client/TUCSNGTB4/C0101R453E3/details/info
    'workshop', # 'vee', # https://app.slack.com/client/TUCSNGTB4/CUWERP5TN/details/info
    'techical_session', # 'dynamic_compilation', # https://app.slack.com/client/TUCSNGTB4/CUQDZ91L3/details/info
    'techical_session', # 'persistence_and_correctness', # https://app.slack.com/client/TUCSNGTB4/CUP4PNMPU/details/info
    'techical_session', # 'evaluation_techniques', # https://app.slack.com/client/TUCSNGTB4/CV1UC2ZJR/details/info
    'techical_session', # 'speculation_and_consistency', # https://app.slack.com/client/TUCSNGTB4/CV1ECGC3E/details/info
    'techical_session', # 'storage', # https://app.slack.com/client/TUCSNGTB4/CV1UDEGLD/details/info
    'techical_session', # 'persistent_data_structures', # https://app.slack.com/client/TUCSNGTB4/CV1UCEM6H/details/info
    'techical_session', # 'simt', # https://app.slack.com/client/TUCSNGTB4/CV44N25HU/details/info
    'techical_session', # 'virtualized_environments', # https://app.slack.com/client/TUCSNGTB4/CUP4MB50A/details/info
    'techical_session', # 'acid', # https://app.slack.com/client/TUCSNGTB4/CV1U9K0JH/details/info
    'techical_session', # 'tensor_computation_and_data_orchestration', # https://app.slack.com/client/TUCSNGTB4/CV1EEV8Q4/details/info
    'techical_session', # 'streaming_computational_models', # https://app.slack.com/client/TUCSNGTB4/CV1EDV24C/details/info
    'chat', # 'diversity-and-inclusion', # https://app.slack.com/client/TUCSNGTB4/C0108JB3G5D/details/info
    'techical_session', # 'virtualized_acceleration', # https://app.slack.com/client/TUCSNGTB4/CUQE25Y91/details/info
    'techical_session', # 'automata', # https://app.slack.com/client/TUCSNGTB4/CV1TQPRFS/details/info
    'workshop', # 'workshop-eurolab4hpc-industry-day-on-convergence-of-ml-and-hpc', # https://app.slack.com/client/TUCSNGTB4/CV8BPQ7GU/details/info
    'workshop', # 'workshop-the-young-architect-workshop', # https://app.slack.com/client/TUCSNGTB4/CV8R4CCC8/details/info
    'techical_session', # 'smart_peripherals', # https://app.slack.com/client/TUCSNGTB4/CUP4K0EHG/details/info
    'tutorial', # 'tutorial-esp-soc-platform', # https://app.slack.com/client/TUCSNGTB4/CUXBE3HJP/details/info
    'chat', # 'feedback', # https://app.slack.com/client/TUCSNGTB4/C0106MZTW7N/details/info
    'workshop', # 'yarch', # https://app.slack.com/client/TUCSNGTB4/C010BUKN2HJ/details/info
    'tutorial', # 'tutorial-firesim-and-chipyard-end-to-end-architecture-research', # https://app.slack.com/client/TUCSNGTB4/CUXB2L51R/details/info
    'tutorial', # 'tutorial-side-and-covert-channels-attacks-and-defenses', # https://app.slack.com/client/TUCSNGTB4/CV8BUJBC4/details/info
    'tutorial', # 'tutorial-a-deep-dive-into-deep-learning-benchmarking-and-analysis', # https://app.slack.com/client/TUCSNGTB4/CUXBFE42F/details/info
    'tutorial', # 'tutorial-understanding-system-implications-for-neural-recommendation', # https://app.slack.com/client/TUCSNGTB4/CUW1GDW1Y/details/info
    'workshop', # 'workshop-nope-negative-results-opportunities-perspectives-and-experience', # https://app.slack.com/client/TUCSNGTB4/CVALQ4X47/details/info
    'tutorial', # 'tutorial-full-system-instrumentation-with-qflex', # https://app.slack.com/client/TUCSNGTB4/CVALVGRKR/details/info
    'workshop', # 'workshop-approximate-computing-across-the-stack', # https://app.slack.com/client/TUCSNGTB4/CV8RRJQ69/details/info
    'tutorial', # 'tutorial-bigdatabench-and-aibench', # https://app.slack.com/client/TUCSNGTB4/CVB1YBR8W/details/info
    'tutorial', # 'tutorial-fpga-as-efficient-accelerator-platform-for-neural-networks-and-graphs', # https://app.slack.com/client/TUCSNGTB4/CUXB7QALT/details/info
    'chat', # 'chairs-announcements', # https://app.slack.com/client/TUCSNGTB4/CURLZE0MB/details/info
    'chat', # 'general', # https://app.slack.com/client/TUCSNGTB4/CUCSNHHU2/details/info
    'chat', # 'random', # https://app.slack.com/client/TUCSNGTB4/CUTGDGHCP/details/info
    'chat', # 'hallway', # https://app.slack.com/client/TUCSNGTB4/CV7S51PA6/details/info
    'techical_session', # 'edge_intermittent_computing_support', # https://app.slack.com/client/TUCSNGTB4/CUP4JNSAE/details/info
    'techical_session', # 'quantum_computing', # https://app.slack.com/client/TUCSNGTB4/CV1TUB69W/details/info
    'techical_session', # 'mobile-intermittent_applications', # https://app.slack.com/client/TUCSNGTB4/CV44LCMEJ/details/info
    'tutorial', # 'tutorial-practical-aspects-of-software-for-noisy-intermediate-scale-quantum' # https://app.slack.com/client/TUCSNGTB4/CV8BN9ECU/details/info
]

channel_names = [
    'best-paper-awards', # https://app.slack.com/client/TUCSNGTB4/CUFN31465/details/info
    'waci', # https://app.slack.com/client/TUCSNGTB4/CUEBJBRUK/details/info
    'most-influential-paper-awards', # https://app.slack.com/client/TUCSNGTB4/CUD1WR8CA/details/info
    'accelerators', # https://app.slack.com/client/TUCSNGTB4/CUP4PUSM8/details/info
    'memory_management', # https://app.slack.com/client/TUCSNGTB4/CURR70B89/details/info
    'jobs', # https://app.slack.com/client/TUCSNGTB4/CV83Z4EKC/details/info
    'memory_behavior', # https://app.slack.com/client/TUCSNGTB4/CUQE179NX/details/info
    'datacenter-cloud_power-performance', # https://app.slack.com/client/TUCSNGTB4/CV1TS3LRW/details/info
    'exotic_architectures', # https://app.slack.com/client/TUCSNGTB4/CUQE0HWKD/details/info
    'enclaves_and_memory_security', # https://app.slack.com/client/TUCSNGTB4/CV44LL29L/details/info
    'speculation_and_security', # https://app.slack.com/client/TUCSNGTB4/CURR56TTK/details/info
    'frameworks_for_deep_learning', # https://app.slack.com/client/TUCSNGTB4/CV3PR5C9M/details/info
    'security_with_little_performance_loss', # https://app.slack.com/client/TUCSNGTB4/CV1TVCKNC/details/info
    'huge_memories_and_distributed_databases', # https://app.slack.com/client/TUCSNGTB4/CV1TR1L4Q/details/info
    'privacy_and_security_in_machine_learning', # https://app.slack.com/client/TUCSNGTB4/C0101R453E3/details/info
    'vee', # https://app.slack.com/client/TUCSNGTB4/CUWERP5TN/details/info
    'dynamic_compilation', # https://app.slack.com/client/TUCSNGTB4/CUQDZ91L3/details/info
    'persistence_and_correctness', # https://app.slack.com/client/TUCSNGTB4/CUP4PNMPU/details/info
    'evaluation_techniques', # https://app.slack.com/client/TUCSNGTB4/CV1UC2ZJR/details/info
    'speculation_and_consistency', # https://app.slack.com/client/TUCSNGTB4/CV1ECGC3E/details/info
    'storage', # https://app.slack.com/client/TUCSNGTB4/CV1UDEGLD/details/info
    'persistent_data_structures', # https://app.slack.com/client/TUCSNGTB4/CV1UCEM6H/details/info
    'simt', # https://app.slack.com/client/TUCSNGTB4/CV44N25HU/details/info
    'virtualized_environments', # https://app.slack.com/client/TUCSNGTB4/CUP4MB50A/details/info
    'acid', # https://app.slack.com/client/TUCSNGTB4/CV1U9K0JH/details/info
    'tensor_computation_and_data_orchestration', # https://app.slack.com/client/TUCSNGTB4/CV1EEV8Q4/details/info
    'streaming_computational_models', # https://app.slack.com/client/TUCSNGTB4/CV1EDV24C/details/info
    'diversity-and-inclusion', # https://app.slack.com/client/TUCSNGTB4/C0108JB3G5D/details/info
    'virtualized_acceleration', # https://app.slack.com/client/TUCSNGTB4/CUQE25Y91/details/info
    'automata', # https://app.slack.com/client/TUCSNGTB4/CV1TQPRFS/details/info
    'workshop-eurolab4hpc-industry-day-on-convergence-of-ml-and-hpc', # https://app.slack.com/client/TUCSNGTB4/CV8BPQ7GU/details/info
    'workshop-the-young-architect-workshop', # https://app.slack.com/client/TUCSNGTB4/CV8R4CCC8/details/info
    'smart_peripherals', # https://app.slack.com/client/TUCSNGTB4/CUP4K0EHG/details/info
    'tutorial-esp-soc-platform', # https://app.slack.com/client/TUCSNGTB4/CUXBE3HJP/details/info
    'feedback', # https://app.slack.com/client/TUCSNGTB4/C0106MZTW7N/details/info
    'yarch', # https://app.slack.com/client/TUCSNGTB4/C010BUKN2HJ/details/info
    'tutorial-firesim-and-chipyard-end-to-end-architecture-research', # https://app.slack.com/client/TUCSNGTB4/CUXB2L51R/details/info
    'tutorial-side-and-covert-channels-attacks-and-defenses', # https://app.slack.com/client/TUCSNGTB4/CV8BUJBC4/details/info
    'tutorial-a-deep-dive-into-deep-learning-benchmarking-and-analysis', # https://app.slack.com/client/TUCSNGTB4/CUXBFE42F/details/info
    'tutorial-understanding-system-implications-for-neural-recommendation', # https://app.slack.com/client/TUCSNGTB4/CUW1GDW1Y/details/info
    'workshop-nope-negative-results-opportunities-perspectives-and-experience', # https://app.slack.com/client/TUCSNGTB4/CVALQ4X47/details/info
    'tutorial-full-system-instrumentation-with-qflex', # https://app.slack.com/client/TUCSNGTB4/CVALVGRKR/details/info
    'workshop-approximate-computing-across-the-stack', # https://app.slack.com/client/TUCSNGTB4/CV8RRJQ69/details/info
    'tutorial-bigdatabench-and-aibench', # https://app.slack.com/client/TUCSNGTB4/CVB1YBR8W/details/info
    'tutorial-fpga-as-efficient-accelerator-platform-for-neural-networks-and-graphs', # https://app.slack.com/client/TUCSNGTB4/CUXB7QALT/details/info
    'chairs-announcements', # https://app.slack.com/client/TUCSNGTB4/CURLZE0MB/details/info
    'general', # https://app.slack.com/client/TUCSNGTB4/CUCSNHHU2/details/info
    'random', # https://app.slack.com/client/TUCSNGTB4/CUTGDGHCP/details/info
    'hallway', # https://app.slack.com/client/TUCSNGTB4/CV7S51PA6/details/info
    'edge_intermittent_computing_support', # https://app.slack.com/client/TUCSNGTB4/CUP4JNSAE/details/info
    'quantum_computing', # https://app.slack.com/client/TUCSNGTB4/CV1TUB69W/details/info
    'mobile-intermittent_applications', # https://app.slack.com/client/TUCSNGTB4/CV44LCMEJ/details/info
    'tutorial-practical-aspects-of-software-for-noisy-intermediate-scale-quantum' # https://app.slack.com/client/TUCSNGTB4/CV8BN9ECU/details/info
]

channel_members = [
    221, # 'best-paper-awards', # https://app.slack.com/client/TUCSNGTB4/CUFN31465/details/info
    178, # 'waci', # https://app.slack.com/client/TUCSNGTB4/CUEBJBRUK/details/info
    162, # 'most-influential-paper-awards', # https://app.slack.com/client/TUCSNGTB4/CUD1WR8CA/details/info
    132, # 'accelerators' # https://app.slack.com/client/TUCSNGTB4/CUP4PUSM8/details/info
    116, # 'memory_management', # https://app.slack.com/client/TUCSNGTB4/CURR70B89/details/info
    105, # 'jobs', # https://app.slack.com/client/TUCSNGTB4/CV83Z4EKC/details/info
    102, # 'memory_behavior', # https://app.slack.com/client/TUCSNGTB4/CUQE179NX/details/info
    98,  # 'datacenter-cloud_power-performance', # https://app.slack.com/client/TUCSNGTB4/CV1TS3LRW/details/info
    98,  # 'exotic_architectures', # https://app.slack.com/client/TUCSNGTB4/CUQE0HWKD/details/info
    87,  # 'enclaves_and_memory_security', # https://app.slack.com/client/TUCSNGTB4/CV44LL29L/details/info
    86,  # 'speculation_and_security', # https://app.slack.com/client/TUCSNGTB4/CURR56TTK/details/info
    83,  # 'frameworks_for_deep_learning', # https://app.slack.com/client/TUCSNGTB4/CV3PR5C9M/details/info
    83,  # 'security_with_little_performance_loss', # https://app.slack.com/client/TUCSNGTB4/CV1TVCKNC/details/info
    82,  # 'huge_memories_and_distributed_databases', # https://app.slack.com/client/TUCSNGTB4/CV1TR1L4Q/details/info
    82,  # 'privacy_and_security_in_machine_learning', # https://app.slack.com/client/TUCSNGTB4/C0101R453E3/details/info
    81,  # 'vee', # https://app.slack.com/client/TUCSNGTB4/CUWERP5TN/details/info
    78,  # 'dynamic_compilation', # https://app.slack.com/client/TUCSNGTB4/CUQDZ91L3/details/info
    77,  # 'persistence_and_correctness', # https://app.slack.com/client/TUCSNGTB4/CUP4PNMPU/details/info
    74,  # 'evaluation_techniques', # https://app.slack.com/client/TUCSNGTB4/CV1UC2ZJR/details/info
    73,  # 'speculation_and_consistency', # https://app.slack.com/client/TUCSNGTB4/CV1ECGC3E/details/info
    72,  # 'storage', # https://app.slack.com/client/TUCSNGTB4/CV1UDEGLD/details/info
    68,  # 'persistent_data_structures', # https://app.slack.com/client/TUCSNGTB4/CV1UCEM6H/details/info
    66,  # 'simt', # https://app.slack.com/client/TUCSNGTB4/CV44N25HU/details/info
    65,  # 'virtualized_environments', # https://app.slack.com/client/TUCSNGTB4/CUP4MB50A/details/info
    65,  # 'acid', # https://app.slack.com/client/TUCSNGTB4/CV1U9K0JH/details/info
    65,  # 'tensor_computation_and_data_orchestration', # https://app.slack.com/client/TUCSNGTB4/CV1EEV8Q4/details/info
    60,  # 'streaming_computational_models', # https://app.slack.com/client/TUCSNGTB4/CV1EDV24C/details/info
    58,  # 'diversity-and-inclusion', # https://app.slack.com/client/TUCSNGTB4/C0108JB3G5D/details/info
    57,  # 'virtualized_acceleration', # https://app.slack.com/client/TUCSNGTB4/CUQE25Y91/details/info
    57,  # 'automata', # https://app.slack.com/client/TUCSNGTB4/CV1TQPRFS/details/info
    55,  # 'workshop-eurolab4hpc-industry-day-on-convergence-of-ml-and-hpc', # https://app.slack.com/client/TUCSNGTB4/CV8BPQ7GU/details/info
    52,  # 'workshop-the-young-architect-workshop', # https://app.slack.com/client/TUCSNGTB4/CV8R4CCC8/details/info
    51,  # 'smart_peripherals', # https://app.slack.com/client/TUCSNGTB4/CUP4K0EHG/details/info
    43,  # 'tutorial-esp-soc-platform', # https://app.slack.com/client/TUCSNGTB4/CUXBE3HJP/details/info
    39,  # 'feedback', # https://app.slack.com/client/TUCSNGTB4/C0106MZTW7N/details/info
    37,  # 'yarch', # https://app.slack.com/client/TUCSNGTB4/C010BUKN2HJ/details/info
    36,  # 'tutorial-firesim-and-chipyard-end-to-end-architecture-research', # https://app.slack.com/client/TUCSNGTB4/CUXB2L51R/details/info
    34,  # 'tutorial-side-and-covert-channels-attacks-and-defenses', # https://app.slack.com/client/TUCSNGTB4/CV8BUJBC4/details/info
    33,  # 'tutorial-a-deep-dive-into-deep-learning-benchmarking-and-analysis', # https://app.slack.com/client/TUCSNGTB4/CUXBFE42F/details/info
    33,  # 'tutorial-understanding-system-implications-for-neural-recommendation', # https://app.slack.com/client/TUCSNGTB4/CUW1GDW1Y/details/info
    32,  # 'workshop-nope-negative-results-opportunities-perspectives-and-experience', # https://app.slack.com/client/TUCSNGTB4/CVALQ4X47/details/info
    31,  # 'tutorial-full-system-instrumentation-with-qflex', # https://app.slack.com/client/TUCSNGTB4/CVALVGRKR/details/info
    31,  # 'workshop-approximate-computing-across-the-stack', # https://app.slack.com/client/TUCSNGTB4/CV8RRJQ69/details/info
    30,  # 'tutorial-bigdatabench-and-aibench', # https://app.slack.com/client/TUCSNGTB4/CVB1YBR8W/details/info
    29,  # 'tutorial-fpga-as-efficient-accelerator-platform-for-neural-networks-and-graphs', # https://app.slack.com/client/TUCSNGTB4/CUXB7QALT/details/info
    997, # 'chairs-announcements', # https://app.slack.com/client/TUCSNGTB4/CURLZE0MB/details/info
    997, # 'general', # https://app.slack.com/client/TUCSNGTB4/CUCSNHHU2/details/info
    997, # 'random', # https://app.slack.com/client/TUCSNGTB4/CUTGDGHCP/details/info
    126, # 'hallway', # https://app.slack.com/client/TUCSNGTB4/CV7S51PA6/details/info
    107, # 'edge_intermittent_computing_support', # https://app.slack.com/client/TUCSNGTB4/CUP4JNSAE/details/info
    66,  # 'quantum_computing', # https://app.slack.com/client/TUCSNGTB4/CV1TUB69W/details/info
    52,  # 'mobile-intermittent_applications', # https://app.slack.com/client/TUCSNGTB4/CV44LCMEJ/details/info
    26   # 'tutorial-practical-aspects-of-software-for-noisy-intermediate-scale-quantum', # https://app.slack.com/client/TUCSNGTB4/CV8BN9ECU/details/info
]

channel_messages = [
    5,  # 'best-paper-awards', # https://app.slack.com/client/TUCSNGTB4/CUFN31465/details/info
    105,  # 'waci', # https://app.slack.com/client/TUCSNGTB4/CUEBJBRUK/details/info
    2,  # 'most-influential-paper-awards', # https://app.slack.com/client/TUCSNGTB4/CUD1WR8CA/details/info
    3,  # 'accelerators' # https://app.slack.com/client/TUCSNGTB4/CUP4PUSM8/details/info
    39, # 'memory_management', # https://app.slack.com/client/TUCSNGTB4/CURR70B89/details/info
    16,  # 'jobs', # https://app.slack.com/client/TUCSNGTB4/CV83Z4EKC/details/info
    47, # 'memory_behavior', # https://app.slack.com/client/TUCSNGTB4/CUQE179NX/details/info
    12,  # 'datacenter-cloud_power-performance', # https://app.slack.com/client/TUCSNGTB4/CV1TS3LRW/details/info
    33,  # 'exotic_architectures', # https://app.slack.com/client/TUCSNGTB4/CUQE0HWKD/details/info
    4,  # 'enclaves_and_memory_security', # https://app.slack.com/client/TUCSNGTB4/CV44LL29L/details/info
    15, # 'speculation_and_security', # https://app.slack.com/client/TUCSNGTB4/CURR56TTK/details/info
    10,  # 'frameworks_for_deep_learning', # https://app.slack.com/client/TUCSNGTB4/CV3PR5C9M/details/info
    5,  # 'security_with_little_performance_loss', # https://app.slack.com/client/TUCSNGTB4/CV1TVCKNC/details/info
    48, # 'huge_memories_and_distributed_databases', # https://app.slack.com/client/TUCSNGTB4/CV1TR1L4Q/details/info
    13, # 'privacy_and_security_in_machine_learning', # https://app.slack.com/client/TUCSNGTB4/C0101R453E3/details/info
    35,  # 'vee', # https://app.slack.com/client/TUCSNGTB4/CUWERP5TN/details/info
    205 , # 'dynamic_compilation', # https://app.slack.com/client/TUCSNGTB4/CUQDZ91L3/details/info
    8,  # 'persistence_and_correctness', # https://app.slack.com/client/TUCSNGTB4/CUP4PNMPU/details/info
    13, # 'evaluation_techniques', # https://app.slack.com/client/TUCSNGTB4/CV1UC2ZJR/details/info
    15,  # 'speculation_and_consistency', # https://app.slack.com/client/TUCSNGTB4/CV1ECGC3E/details/info
    2,  # 'storage', # https://app.slack.com/client/TUCSNGTB4/CV1UDEGLD/details/info
    5,  # 'persistent_data_structures', # https://app.slack.com/client/TUCSNGTB4/CV1UCEM6H/details/info
    5,  # 'simt', # https://app.slack.com/client/TUCSNGTB4/CV44N25HU/details/info
    6,  # 'virtualized_environments', # https://app.slack.com/client/TUCSNGTB4/CUP4MB50A/details/info
    18,  # 'acid', # https://app.slack.com/client/TUCSNGTB4/CV1U9K0JH/details/info
    2,  # 'tensor_computation_and_data_orchestration', # https://app.slack.com/client/TUCSNGTB4/CV1EEV8Q4/details/info
    18,  # 'streaming_computational_models', # https://app.slack.com/client/TUCSNGTB4/CV1EDV24C/details/info
    8,  # 'diversity-and-inclusion', # https://app.slack.com/client/TUCSNGTB4/C0108JB3G5D/details/info
    4,  # 'virtualized_acceleration', # https://app.slack.com/client/TUCSNGTB4/CUQE25Y91/details/info
    36,  # 'automata', # https://app.slack.com/client/TUCSNGTB4/CV1TQPRFS/details/info
    73,  # 'workshop-eurolab4hpc-industry-day-on-convergence-of-ml-and-hpc', # https://app.slack.com/client/TUCSNGTB4/CV8BPQ7GU/details/info
    0,  # 'workshop-the-young-architect-workshop', # https://app.slack.com/client/TUCSNGTB4/CV8R4CCC8/details/info
    21,  # 'smart_peripherals', # https://app.slack.com/client/TUCSNGTB4/CUP4K0EHG/details/info
    5,  # 'tutorial-esp-soc-platform', # https://app.slack.com/client/TUCSNGTB4/CUXBE3HJP/details/info
    10,  # 'feedback', # https://app.slack.com/client/TUCSNGTB4/C0106MZTW7N/details/info
    4,  # 'yarch', # https://app.slack.com/client/TUCSNGTB4/C010BUKN2HJ/details/info
    1,  # 'tutorial-firesim-and-chipyard-end-to-end-architecture-research', # https://app.slack.com/client/TUCSNGTB4/CUXB2L51R/details/info
    1,  # 'tutorial-side-and-covert-channels-attacks-and-defenses', # https://app.slack.com/client/TUCSNGTB4/CV8BUJBC4/details/info
    0,  # 'tutorial-a-deep-dive-into-deep-learning-benchmarking-and-analysis', # https://app.slack.com/client/TUCSNGTB4/CUXBFE42F/details/info
    4,  # 'tutorial-understanding-system-implications-for-neural-recommendation', # https://app.slack.com/client/TUCSNGTB4/CUW1GDW1Y/details/info
    0,  # 'workshop-nope-negative-results-opportunities-perspectives-and-experience', # https://app.slack.com/client/TUCSNGTB4/CVALQ4X47/details/info
    3,  # 'tutorial-full-system-instrumentation-with-qflex', # https://app.slack.com/client/TUCSNGTB4/CVALVGRKR/details/info
    0,  # 'workshop-approximate-computing-across-the-stack', # https://app.slack.com/client/TUCSNGTB4/CV8RRJQ69/details/info
    1,  # 'tutorial-bigdatabench-and-aibench', # https://app.slack.com/client/TUCSNGTB4/CVB1YBR8W/details/info
    0,  # 'tutorial-fpga-as-efficient-accelerator-platform-for-neural-networks-and-graphs', # https://app.slack.com/client/TUCSNGTB4/CUXB7QALT/details/info
    6,  # 'chairs-announcements', # https://app.slack.com/client/TUCSNGTB4/CURLZE0MB/details/info
    145,  # 'general', # https://app.slack.com/client/TUCSNGTB4/CUCSNHHU2/details/info
    34,  # 'random', # https://app.slack.com/client/TUCSNGTB4/CUTGDGHCP/details/info
    82,  # 'hallway', # https://app.slack.com/client/TUCSNGTB4/CV7S51PA6/details/info
    56,  # 'edge_intermittent_computing_support', # https://app.slack.com/client/TUCSNGTB4/CUP4JNSAE/details/info
    32,  # 'quantum_computing', # https://app.slack.com/client/TUCSNGTB4/CV1TUB69W/details/info
    15,  # 'mobile-intermittent_applications', # https://app.slack.com/client/TUCSNGTB4/CV44LCMEJ/details/info
    1  # 'tutorial-practical-aspects-of-software-for-noisy-intermediate-scale-quantum', # https://app.slack.com/client/TUCSNGTB4/CV8BN9ECU/details/info
]

# Sort results in descending order
channel_names = [x for _,x in sorted(zip(channel_members, channel_names), reverse = True)]
channel_messages = [x for _,x in sorted(zip(channel_members, channel_messages), reverse = True)]
channel_type = [x for _,x in sorted(zip(channel_members, channel_type), reverse = True)]
channel_members = sorted(channel_members, reverse = True)

font_size = 7 # figure font size
width = 0.5 # bar width

plt.figure(figsize = (12, 6)) # figure size
plt.rc('ytick', labelsize = font_size) # change ytick size
y_pos = np.arange(len(channel_members)) # position of bars
ax = plt.subplot() # create subplot
ax.bar(y_pos - width/2, channel_members, width - .1, label = 'Memebers') # plot number of members per channel
ax.bar(y_pos + width/2, channel_messages, width - .1, label = 'Posts') # plot number of messages per channel
ax.set_xlabel('Channel name', fontsize = font_size) # sey y label
ax.set_ylabel('Number', fontsize = font_size) # sey y label
ax.legend(fontsize = font_size) # set legend font size
ax.set_title('asplos2020.slack.com: number of channel members and total posts per channel '
             '(collected manually on March 22, 2020 from 17:04PM to 17:44PM CET '
             '- two days after conference completion)',
             fontsize = font_size, fontweight = 'bold') # set figure title
plt.xticks(y_pos, channel_names, rotation = 90, fontsize = font_size, zorder = 100,
           ha = 'center', color = 'red')  # set x ticks bar properties

# Channel type identifiers
channel_identifier = [
    'techical session',
    'special session',
    'workshop',
    'tutorial',
    'chat',
]

# Colors for individual channel types
color_palette = [
    'red',
    'green',
    'blue',
    'magenta',
    'orange'
]

# annotate the meaning of color symbols for bar ticks
for i in range(0, len(channel_identifier)):
    plt.annotate(channel_identifier[i],
                xy = (0.1, 0.85 - i/10),
                xycoords = 'axes fraction',
                fontsize = font_size,
                color = color_palette[i])
    for j in range(0, len(channel_type)):
        if channel_type[j] == 'techical_session':
            ax.get_xticklabels()[j].set_color(color_palette[0])
        if channel_type[j] == 'special_session':
            ax.get_xticklabels()[j].set_color(color_palette[1])
        if channel_type[j] == 'workshop':
            ax.get_xticklabels()[j].set_color(color_palette[2])
        if channel_type[j] == 'tutorial':
            ax.get_xticklabels()[j].set_color(color_palette[3])
        if channel_type[j] == 'chat':
            ax.get_xticklabels()[j].set_color(color_palette[4])

# calculate statistics (technical sessions only)
channel_members_tech = \
    [channel_members[i] for i in range(len(channel_type)) if channel_type[i] == 'techical_session']
channel_messages_tech = \
    [channel_messages[i] for i in range(len(channel_type)) if channel_type[i] == 'techical_session']

mean_channel_members_tech = round(np.mean(channel_members_tech),1) # mean channel members
median_channel_members_tech = round(np.median(channel_members_tech),1) # median channel members

mean_channel_messages_tech = round(np.mean(channel_messages_tech),1) # mean channel messages
median_channel_messages_tech = round(np.median(channel_messages_tech),1) # median channel messages

# annotate graph with statistics (members)
plt.annotate('for technical sessions only - ',
             xy = (0.25, 0.85),
             xycoords = 'axes fraction',
             fontsize = font_size,
             color = 'red')

text_annotation = 'mean: ' + str(mean_channel_members_tech) + ' channnel members; ' + \
                  ' median: ' + str(median_channel_members_tech) + ' channnel members'

plt.annotate(text_annotation,
             xy = (0.375, 0.85),
             xycoords = 'axes fraction',
             fontsize = font_size,
             color = 'red')

# annotate graph with statistics (messages)
plt.annotate('for technical sessions only - ',
             xy = (0.25, 0.75),
             xycoords = 'axes fraction',
             fontsize = font_size,
             color = 'red')

text_annotation = 'mean: ' + str(mean_channel_messages_tech) + ' channnel messages; ' + \
                  ' median: ' + str(median_channel_messages_tech) + ' channnel messages'

plt.annotate(text_annotation,
             xy = (0.375, 0.75),
             xycoords = 'axes fraction',
             fontsize = font_size,
             color = 'red')

plt.tight_layout() # tight layout
plt.show()