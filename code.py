import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
height_list = df['gender'].to_list()
weight_list = df['race/ethnicity'].to_list()

parental_list = df['parental level of education'].to_list()
lunch_list = df['lunch'].to_list()
test_list  = df["test preparation course"].to_list()
math_list = df["math score"].to_list()
writing_list = df['writing score'].to_list()
reading_list = df['reading score'].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)
parental_mean = statistics.mean(parental_list)
lunch_mean = statistics.mean(lunch_list)
test_mean = statistics.mean(test_list)
math_mean = statistics.mean(math_list)
writing_mean = statistics.mean(writing_list)
reading_mean = statistics.mean(reading_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)
parental_median = statistics.median(parental_list)
lunch_median = statistics.median(lunch_list)
test_median = statistics.median(test_list)
math_median = statistics.median(math_list)
writing_median = statistics.median(writing_list)
reading_median = statistics.median(reading_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)
parental_mode = statistics.mode(parental_list)
lunch_mode= statistics.mode(lunch_list)
test_mode = statistics.mode(test_list)
math_mode = statistics.mode(math_list)
writing_mode = statistics.mode(writing_list)
reading_mode = statistics.mode(reading_list)

height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)
parental_std_deviation = statistics.stdev(parental_list)
lunch_std_deviation = statistics.stdev(lunch_list)
test_std_deviation = statistics.stdev(test_list)
math_std_deviation = statistics.stdev(math_list)
writing_std_deviation = statistics.stdev(writing_list)
reading_std_deviation = statistics.stdev(reading_list)

height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)

parental_first_std_deviation_start, parental_first_std_deviation_end = parental_mean-parental_std_deviation, parental_mean+parental_std_deviation
parental_second_std_deviation_start, parental_second_std_deviation_end = parental_mean-(2*parental_std_deviation), parental_mean+(2*parental_std_deviation)
parental_third_std_deviation_start, parental_third_std_deviation_end = parental_mean-(3*parental_std_deviation), parental_mean+(3*parental_std_deviation)

lunch_first_std_deviation_start, lunch_first_std_deviation_end = lunch_mean-lunch_std_deviation, lunch_mean+lunch_std_deviation
lunch_second_std_deviation_start, lunch_second_std_deviation_end = lunch_mean-(2*lunch_std_deviation), lunch_mean+(2*lunch_std_deviation)
lunch_third_std_deviation_start, lunch_third_std_deviation_end = lunch_mean-(3*lunch_std_deviation), lunch_mean+(3*lunch_std_deviation)

test_first_std_deviation_start, test_first_std_deviation_end = test_mean-test_std_deviation, test_mean+test_std_deviation
test_second_std_deviation_start, test_second_std_deviation_end = test_mean-(2*test_std_deviation), test_mean+(2*test_std_deviation)
test_third_std_deviation_start, test_third_std_deviation_end = test_mean-(3*test_std_deviation), test_mean+(3*test_std_deviation)

math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean-writing_std_deviation, writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean-weight_std_deviation, weight_mean+weight_std_deviation
weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean-(2*weight_std_deviation), weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean-(3*weight_std_deviation), weight_mean+(3*weight_std_deviation)

height_list_of_data_within_1_std_deviation = [result for result in height_list if result >height_first_std_deviation_start and result< height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result >height_second_std_deviation_start and result< height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result >height_third_std_deviation_start and result< height_third_std_deviation_end]

parental_list_of_data_within_1_std_deviation = [result for result in parental_list if result >parental_first_std_deviation_start and result< parental_first_std_deviation_end]
parental_list_of_data_within_2_std_deviation = [result for result in parental_list if result >parental_second_std_deviation_start and result< parental_second_std_deviation_end]
parental_list_of_data_within_3_std_deviation = [result for result in parental_list if result >parental_third_std_deviation_start and result< parental_third_std_deviation_end]

lunch_list_of_data_within_1_std_deviation = [result for result in lunch_list if result >lunch_first_std_deviation_start and result< lunch_first_std_deviation_end]
lunch_list_of_data_within_2_std_deviation = [result for result in lunch_list if result >lunch_second_std_deviation_start and result< lunch_second_std_deviation_end]
lunch_list_of_data_within_3_std_deviation = [result for result in lunch_list if result >lunch_third_std_deviation_start and result< lunch_third_std_deviation_end]

test_list_of_data_within_1_std_deviation = [result for result in test_list if result >test_first_std_deviation_start and result< test_first_std_deviation_end]
test_list_of_data_within_2_std_deviation = [result for result in test_list if result >test_second_std_deviation_start and result< test_second_std_deviation_end]
test_list_of_data_within_3_std_deviation = [result for result in test_list if result >test_third_std_deviation_start and result< test_third_std_deviation_end]

math_list_of_data_within_1_std_deviation = [result for result in math_list if result >math_first_std_deviation_start and result< math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_list if result >math_second_std_deviation_start and result< math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_list if result >math_third_std_deviation_start and result< math_third_std_deviation_end]

writing_list_of_data_within_1_std_deviation = [result for result in writing_list if result >writing_first_std_deviation_start and result< writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing_list if result >writing_second_std_deviation_start and result< writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in writing_list if result >writing_third_std_deviation_start and result< writing_third_std_deviation_end]

reading_list_of_data_within_1_std_deviation = [result for result in reading_list if result >reading_first_std_deviation_start and result< reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading_list if result >reading_second_std_deviation_start and result< reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading_list if result >reading_third_std_deviation_start and result< reading_third_std_deviation_end]

weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result >weight_first_std_deviation_start and result< weight_first_std_deviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result >weight_second_std_deviation_start and result< weight_second_std_deviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result >weight_third_std_deviation_start and result< weight_third_std_deviation_end]

print('{}% of data for height lies within 1 standard deviation'. format(len(height_list_of_data_within_1_std_deviation)*100/len(height_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))

print('{}% of data for parental lies within 1 standard deviation'. format(len(parental_list_of_data_within_1_std_deviation)*100/len(parental_list)))
print("{}% of data for parental lies within 2 standard deviations".format(len(parental_list_of_data_within_2_std_deviation)*100.0/len(parental_list)))
print("{}% of data for parental lies within 3 standard deviations".format(len(parental_list_of_data_within_3_std_deviation)*100.0/len(parental_list)))

print('{}% of data for lunch lies within 1 standard deviation'. format(len(lunch_list_of_data_within_1_std_deviation)*100/len(lunch_list)))
print("{}% of data for lunch lies within 2 standard deviations".format(len(lunch_list_of_data_within_2_std_deviation)*100.0/len(lunch_list)))
print("{}% of data for lunch lies within 3 standard deviations".format(len(lunch_list_of_data_within_3_std_deviation)*100.0/len(lunch_list)))

print('{}% of data for test lies within 1 standard deviation'. format(len(test_list_of_data_within_1_std_deviation)*100/len(test_list)))
print("{}% of data for test lies within 2 standard deviations".format(len(test_list_of_data_within_2_std_deviation)*100.0/len(test_list)))
print("{}% of data for test lies within 3 standard deviations".format(len(test_list_of_data_within_3_std_deviation)*100.0/len(test_list)))


print('{}% of data for math lies within 1 standard deviation'. format(len(math_list_of_data_within_1_std_deviation)*100/len(math_list)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_list)))


print('{}% of data for writing lies within 1 standard deviation'. format(len(writing_list_of_data_within_1_std_deviation)*100/len(writing_list)))
print("{}% of data for writing lies within 2 standard deviations".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing lies within 3 standard deviations".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing_list)))


print('{}% of data for reading lies within 1 standard deviation'. format(len(reading_list_of_data_within_1_std_deviation)*100/len(reading_list)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviations".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviations".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))