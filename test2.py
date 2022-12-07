list_of_tuples = [(5, 'Alice'), (10, 'Bob'), (15, 'Carl'), (20, 'Dean')]


result_1 = [tup[1] for tup in list_of_tuples].index('Dean')

print(result_1)  # 👉️ 2
