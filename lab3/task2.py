# TODO Напишите функцию find_common_participants
def find_common_participants(paticipants1, paticipants2, sep=','):
    paticipants1 = paticipants1.split("|")
    paticipants2 = paticipants2.split("|")
    common_participants = set(paticipants1).intersection(paticipants2)
    list_ = list(common_participants)
   # list_ = list_.sort() - если включить эту строку, то выдаёт None почему-то
    return list_                        #sep.join(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
