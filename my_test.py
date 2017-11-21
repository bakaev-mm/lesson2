school_score = [{'school_class': '1a', 'scores': [3,4,4,5,2]}, {'school_class': '1b', 'scores': [3,3,5,5,5]}, {'school_class': '4c', 'scores': [4,4,4,4,2]}, {'school_class': '4d', 'scores': [2,2,1,2,3]}]
a_user1 = (school_score[0]['scores'][0])
a_user2 = (school_score[0]['scores'][1])
a_user3 = (school_score[0]['scores'][2])
a_user4 = (school_score[0]['scores'][3])
a_user5 = (school_score[0]['scores'][4])
a_len = len(school_score[0]['scores'])

averge_class_a_score = (a_user1 + a_user2 + a_user3 + a_user4 + a_user5) / a_len
print('Средний балл А класса =' + ' ' + str(averge_class_a_score))

b_user1 = (school_score[1]['scores'][0])
b_user2 = (school_score[1]['scores'][1])
b_user3 = (school_score[1]['scores'][2])
b_user4 = (school_score[1]['scores'][3])
b_user5 = (school_score[1]['scores'][4])
b_len = len(school_score[1]['scores'])

averge_class_b_score = (b_user1 + b_user2 + b_user3 + b_user4 + b_user5) / b_len
print('Средний балл Б класса =' + ' ' + str(averge_class_b_score))

c_user1 = (school_score[2]['scores'][0])
c_user2 = (school_score[2]['scores'][1])
c_user3 = (school_score[2]['scores'][2])
c_user4 = (school_score[2]['scores'][3])
c_user5 = (school_score[2]['scores'][4])
c_len = len(school_score[2]['scores'])

averge_class_c_score = (c_user1 + c_user2 + c_user3 + c_user4 + c_user5) / c_len
print('Средний балл C класса =' + ' ' + str(averge_class_c_score))

d_user1 = (school_score[3]['scores'][0])
d_user2 = (school_score[3]['scores'][1])
d_user3 = (school_score[3]['scores'][2])
d_user4 = (school_score[3]['scores'][3])
d_user5 = (school_score[3]['scores'][4])
d_len = len(school_score[3]['scores'])

averge_class_d_score = (d_user1 + d_user2 + d_user3 + d_user4 + d_user5) / d_len
print('Средний балл Д класса =' + ' ' + str(averge_class_d_score))

averge_scool_score = (averge_class_a_score + averge_class_b_score + averge_class_c_score + averge_class_d_score) / 4
print('Средний балл школы =' + ' ' + str(averge_scool_score))