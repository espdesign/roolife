# Evan Pendergraft
# CITA 180_0W1_BURL - Intro to Programming (Spring 2024)
# Programming Assignment 04

#Input
integer_tuple = (1, -3, 0, 189, -744, 800, 960, 593, -705, -470, 
            286, -229, -380, 394, 285, -681, 889, 35, 906, -662, 
            715, -377, -647, -627, 348)

#Processing 
integer_values = [] 
integer_sum = 0

integer_count = 0
integer_count_negative = 0
integer_count_even = 0
integer_count_odd = 0

integer_highest = integer_tuple[0]
integer_lowest = integer_tuple[0]


for index in integer_tuple:
    integer_values.append(index)

    integer_sum += index

    integer_count += 1

    if index < 0:
        integer_count_negative += 1
    
    if index > integer_highest:
        integer_highest = index

    if index < integer_lowest:
        integer_lowest = index

    if (index % 2) ==0:
        integer_count_even += 1
    else:
        integer_count_odd += 1

integer_average = integer_sum / integer_count

#Output
print('{:_^50}'.format('Tuple Integer Values'))
print(integer_values)
print('{:_^50}'.format('Tuple Integer Statistics'))

print('{::<40} {:<10}'.format('Total number of integers ', integer_count))
print('{::<40} {:<10}'.format('Sum of integers ', integer_sum))
print('{::<40} {:<10.0f}'.format('Average of integers ', integer_average))
print('{::<40} {:<10}'.format('Largest integer ', integer_highest))
print('{::<40} {:<10}'.format('Smallest integer ', integer_lowest))
print('{::<40} {:<10}'.format('Total number of negative integers ', integer_count_negative))
print('{::<40} {:<10} '.format('Total number of even integers ', integer_count_even))
print('{::<40} {:<10}'.format('Total number of odd integers ', integer_count_odd))