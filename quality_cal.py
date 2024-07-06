class QualityCal:
    def __init__(self, mc, ac, ec, activities, i, e_lq):
        self.i = i
        self.mc = mc
        self.ac = ac
        self.ec = ec
        self.activities = activities
        self.e_lq = e_lq

    def computee(self):
        administartion = {1: {'Option1': {'Cost': 220, 'Quality': 0.7},
                              'Option2': {'Cost': 275, 'Quality': 0.85},
                              'Option3': {'Cost': 330, 'Quality': 1.0}},
                          2: {'Option1': {'Cost': 104.8, 'Quality': 0.7},
                              'Option2': {'Cost': 131, 'Quality': 0.85},
                              'Option3': {'Cost': 157.2, 'Quality': 1.0}},
                          3: {'Option1': {'Cost': 16, 'Quality': 0.7},
                              'Option2': {'Cost': 20, 'Quality': 0.85},
                              'Option3': {'Cost': 24, 'Quality': 1.0}},
                          4: {'Option1': {'Cost': 52, 'Quality': 0.7},
                              'Option2': {'Cost': 65, 'Quality': 0.85},
                              'Option3': {'Cost': 78, 'Quality': 1.0}},
                          5: {'Option1': {'Cost': 58.4, 'Quality': 0.7},
                              'Option2': {'Cost': 73, 'Quality': 0.85},
                              'Option3': {'Cost': 87.6, 'Quality': 1.0}},
                          6: {'Option1': {'Cost': 686.4, 'Quality': 0.7},
                              'Option2': {'Cost': 858, 'Quality': 0.85},
                              'Option3': {'Cost': 1029.6, 'Quality': 1.0}},
                          7: {'Option1': {'Cost': 80, 'Quality': 0.7},
                              'Option2': {'Cost': 100, 'Quality': 0.85},
                              'Option3': {'Cost': 120, 'Quality': 1.0}},
                          8: {'Option1': {'Cost': 28, 'Quality': 0.7},
                              'Option2': {'Cost': 35, 'Quality': 0.85},
                              'Option3': {'Cost': 42, 'Quality': 1.0}},
                          9: {'Option1': {'Cost': 42.4, 'Quality': 0.7},
                              'Option2': {'Cost': 53, 'Quality': 0.85},
                              'Option3': {'Cost': 63.6, 'Quality': 1.0}},
                          10: {'Option1': {'Cost': 71.2, 'Quality': 0.7},
                               'Option2': {'Cost': 89, 'Quality': 0.85},
                               'Option3': {'Cost': 106.8, 'Quality': 1.0}},
                          11: {'Option1': {'Cost': 6.4, 'Quality': 0.7},
                               'Option2': {'Cost': 8, 'Quality': 0.85},
                               'Option3': {'Cost': 9.6, 'Quality': 1.0}},
                          12: {'Option1': {'Cost': 127.2, 'Quality': 0.7},
                               'Option2': {'Cost': 159, 'Quality': 0.85},
                               'Option3': {'Cost': 190.8, 'Quality': 1.0}},
                          13: {'Option1': {'Cost': 64.8, 'Quality': 0.7},
                               'Option2': {'Cost': 81, 'Quality': 0.85},
                               'Option3': {'Cost': 97.2, 'Quality': 1.0}},
                          14: {'Option1': {'Cost': 62.4, 'Quality': 0.7},
                               'Option2': {'Cost': 78, 'Quality': 0.85},
                               'Option3': {'Cost': 93.6, 'Quality': 1.0}},
                          15: {'Option1': {'Cost': 98.4, 'Quality': 0.7},
                               'Option2': {'Cost': 123, 'Quality': 0.85},
                               'Option3': {'Cost': 147.6, 'Quality': 1.0}},
                          16: {'Option1': {'Cost': 147.2, 'Quality': 0.7},
                               'Option2': {'Cost': 184, 'Quality': 0.85},
                               'Option3': {'Cost': 220.8, 'Quality': 1.0}},
                          17: {'Option1': {'Cost': 28, 'Quality': 0.7},
                               'Option2': {'Cost': 35, 'Quality': 0.85},
                               'Option3': {'Cost': 42, 'Quality': 1.0}},
                          18: {'Option1': {'Cost': 185.6, 'Quality': 0.7},
                               'Option2': {'Cost': 232, 'Quality': 0.85},
                               'Option3': {'Cost': 278.4, 'Quality': 1.0}},
                          19: {'Option1': {'Cost': 148.8, 'Quality': 0.7},
                               'Option2': {'Cost': 186, 'Quality': 0.85},
                               'Option3': {'Cost': 223.2, 'Quality': 1.0}},
                          20: {'Option1': {'Cost': 28, 'Quality': 0.7},
                               'Option2': {'Cost': 35, 'Quality': 0.85},
                               'Option3': {'Cost': 42, 'Quality': 1.0}}}

        material = {
            1: {"Option1": {"Cost": 1760, "Quality": 0.7},
                "Option2": {"Cost": 2200, "Quality": 0.85},
                "Option3": {"Cost": 2640, "Quality": 1.0}},
            2: {"Option1": {"Cost": 837.6, "Quality": 0.7},
                "Option2": {"Cost": 1047, "Quality": 0.85},
                "Option3": {"Cost": 1256.4, "Quality": 1.0}},
            3: {"Option1": {"Cost": 128, "Quality": 0.7},
                "Option2": {"Cost": 160, "Quality": 0.85},
                "Option3": {"Cost": 192, "Quality": 1.0}},
            4: {"Option1": {"Cost": 419.2, "Quality": 0.7},
                "Option2": {"Cost": 524, "Quality": 0.85},
                "Option3": {"Cost": 628.8, "Quality": 1.0}},
            5: {"Option1": {"Cost": 464, "Quality": 0.7},
                "Option2": {"Cost": 580, "Quality": 0.85},
                "Option3": {"Cost": 696, "Quality": 1.0}},
            6: {"Option1": {"Cost": 5493.6, "Quality": 0.7},
                "Option2": {"Cost": 6867, "Quality": 0.85},
                "Option3": {"Cost": 8240.4, "Quality": 1.0}},
            7: {"Option1": {"Cost": 642.4, "Quality": 0.7},
                "Option2": {"Cost": 803, "Quality": 0.85},
                "Option3": {"Cost": 936.6, "Quality": 1.0}},
            8: {"Option1": {"Cost": 225.6, "Quality": 0.7},
                "Option2": {"Cost": 282, "Quality": 0.85},
                "Option3": {"Cost": 338.4, "Quality": 1.0}},
            9: {"Option1": {"Cost": 337.6, "Quality": 0.7},
                "Option2": {"Cost": 422, "Quality": 0.85},
                "Option3": {"Cost": 506.4, "Quality": 1.0}},
            10: {"Option1": {"Cost": 567.2, "Quality": 0.7},
                 "Option2": {"Cost": 709, "Quality": 0.85},
                 "Option3": {"Cost": 850.8, "Quality": 1.0}},
            11: {"Option1": {"Cost": 52, "Quality": 0.7},
                 "Option2": {"Cost": 65, "Quality": 0.85},
                 "Option3": {"Cost": 78, "Quality": 1.0}},
            12: {"Option1": {"Cost": 1020, "Quality": 0.7},
                 "Option2": {"Cost": 1275, "Quality": 0.85},
                 "Option3": {"Cost": 1530, "Quality": 1.0}},
            13: {"Option1": {"Cost": 516, "Quality": 0.7},
                 "Option2": {"Cost": 645, "Quality": 0.85},
                 "Option3": {"Cost": 774, "Quality": 1.0}},
            14: {"Option1": {"Cost": 501.6, "Quality": 0.7},
                 "Option2": {"Cost": 627, "Quality": 0.85},
                 "Option3": {"Cost": 752.4, "Quality": 1.0}},
            15: {"Option1": {"Cost": 785.6, "Quality": 0.7},
                 "Option2": {"Cost": 982, "Quality": 0.85},
                 "Option3": {"Cost": 1178.4, "Quality": 1.0}},
            16: {"Option1": {"Cost": 1178.4, "Quality": 0.7},
                 "Option2": {"Cost": 1473, "Quality": 0.85},
                 "Option3": {"Cost": 1767.6, "Quality": 1.0}},
            17: {"Option1": {"Cost": 224, "Quality": 0.7},
                 "Option2": {"Cost": 280, "Quality": 0.85},
                 "Option3": {"Cost": 336, "Quality": 1.0}},
            18: {"Option1": {"Cost": 1484, "Quality": 0.7},
                 "Option2": {"Cost": 1855, "Quality": 0.85},
                 "Option3": {"Cost": 2226, "Quality": 1.0}},
            19: {"Option1": {"Cost": 1191.2, "Quality": 0.7},
                 "Option2": {"Cost": 1489, "Quality": 0.85},
                 "Option3": {"Cost": 1786.8, "Quality": 1.0}},
            20: {"Option1": {"Cost": 224, "Quality": 0.7},
                 "Option2": {"Cost": 280, "Quality": 0.85},
                 "Option3": {"Cost": 336, "Quality": 1.0}}
        }

        equipment = {
            1: {"Option1": {"Cost": 1540, "Quality": 0.7},
                "Option2": {"Cost": 1925, "Quality": 0.85},
                "Option3": {"Cost": 2310, "Quality": 1.0}},
            2: {"Option1": {"Cost": 732.8, "Quality": 0.7},
                "Option2": {"Cost": 916, "Quality": 0.85},
                "Option3": {"Cost": 1099.2, "Quality": 1.0}},
            3: {"Option1": {"Cost": 112, "Quality": 0.7},
                "Option2": {"Cost": 140, "Quality": 0.85},
                "Option3": {"Cost": 168, "Quality": 1.0}},
            4: {"Option1": {"Cost": 366.4, "Quality": 0.7},
                "Option2": {"Cost": 458, "Quality": 0.85},
                "Option3": {"Cost": 549.6, "Quality": 1.0}},
            5: {"Option1": {"Cost": 406.4, "Quality": 0.7},
                "Option2": {"Cost": 508, "Quality": 0.85},
                "Option3": {"Cost": 609.6, "Quality": 1.0}},
            6: {"Option1": {"Cost": 4807.2, "Quality": 0.7},
                "Option2": {"Cost": 6009, "Quality": 0.85},
                "Option3": {"Cost": 7210.8, "Quality": 1.0}},
            7: {"Option1": {"Cost": 562.4, "Quality": 0.7},
                "Option2": {"Cost": 703, "Quality": 0.85},
                "Option3": {"Cost": 843.6, "Quality": 1.0}},
            8: {"Option1": {"Cost": 197.6, "Quality": 0.7},
                "Option2": {"Cost": 247, "Quality": 0.85},
                "Option3": {"Cost": 296.4, "Quality": 1.0}},
            9: {"Option1": {"Cost": 295.2, "Quality": 0.7},
                "Option2": {"Cost": 369, "Quality": 0.85},
                "Option3": {"Cost": 442.8, "Quality": 1.0}},
            10: {"Option1": {"Cost": 496, "Quality": 0.7},
                 "Option2": {"Cost": 620, "Quality": 0.85},
                 "Option3": {"Cost": 744, "Quality": 1.0}},
            11: {"Option1": {"Cost": 45.6, "Quality": 0.7},
                 "Option2": {"Cost": 57, "Quality": 0.85},
                 "Option3": {"Cost": 68.4, "Quality": 1.0}},
            12: {"Option1": {"Cost": 892.8, "Quality": 0.7},
                 "Option2": {"Cost": 1116, "Quality": 0.85},
                 "Option3": {"Cost": 1339.2, "Quality": 1.0}},
            13: {"Option1": {"Cost": 452, "Quality": 0.7},
                 "Option2": {"Cost": 565, "Quality": 0.85},
                 "Option3": {"Cost": 678, "Quality": 1.0}},
            14: {"Option1": {"Cost": 439.2, "Quality": 0.7},
                 "Option2": {"Cost": 549, "Quality": 0.85},
                 "Option3": {"Cost": 658.8, "Quality": 1.0}},
            15: {"Option1": {"Cost": 687.2, "Quality": 0.7},
                 "Option2": {"Cost": 859, "Quality": 0.85},
                 "Option3": {"Cost": 1030.8, "Quality": 1.0}},
            16: {"Option1": {"Cost": 1031.2, "Quality": 0.7},
                 "Option2": {"Cost": 1289, "Quality": 0.85},
                 "Option3": {"Cost": 1546.8, "Quality": 1.0}},
            17: {"Option1": {"Cost": 196, "Quality": 0.7},
                 "Option2": {"Cost": 245, "Quality": 0.85},
                 "Option3": {"Cost": 294, "Quality": 1.0}},
            18: {"Option1": {"Cost": 1298.4, "Quality": 0.7},
                 "Option2": {"Cost": 1623, "Quality": 0.85},
                 "Option3": {"Cost": 1947.6, "Quality": 1.0}},
            19: {"Option1": {"Cost": 1042.4, "Quality": 0.7},
                 "Option2": {"Cost": 1303, "Quality": 0.85},
                 "Option3": {"Cost": 1563.6, "Quality": 1.0}},
            20: {"Option1": {"Cost": 196, "Quality": 0.7},
                 "Option2": {"Cost": 245, "Quality": 0.85},
                 "Option3": {"Cost": 294, "Quality": 1.0}}
        }

        quality_of_material = material[self.i + 1]["Option{}".format(self.mc)]["Quality"]
        quality_of_administartion = administartion[self.i + 1]["Option{}".format(self.ac)]["Quality"]
        quality_of_equipment = equipment[self.i + 1]["Option{}".format(self.ec)]["Quality"]
        list_labor_quality = self.e_lq
        quality_of_labor = list_labor_quality[self.i]

        total_quality = (quality_of_material + quality_of_administartion + quality_of_equipment + quality_of_labor) / 80

        return total_quality

# activities = {'1': 2}
# e_lq = [0.25]
# NB = QualityCal(2,2,2,activities,0,e_lq)
# ZX = print(NB.computee())