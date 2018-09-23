import numpy as np
import turtle100

def read_data(c_var):
    d_files = {'max_temp': 'annual_maxTemp.txt', 'min_temp': 'annual_minTemp.txt'}
    data_file = open(d_files[c_var], 'r')
    lines = data_file.readlines()
    n_rows = len(lines)
    n_cols = len(lines[0].split()) - 1
    d_a = np.zeros((n_rows, n_cols), dtype=int)
    for r in range(n_rows):
        p = lines[r].strip().split()[1:]
        for c in range(len(p)):
            d_a[r, c] = p[c]
    return d_a

def clc_ave(list_in):
    total = 0
    count = 0
    for day in list_in:
        if day != -99:
            total += day
            count += 1
    average = total / count
    return average

def julian_2_mn_day(j):
    if j <= 31:
        month = 1
        day_number = j
    if 32 <= j <= 59:
        month = 2
        day_number = j - 31
    if 60 <= j <= 90:
        month = 3
        day_number = j - 59
    if 91 <= j <= 120:
        month = 4
        day_number = j - 90
    if 121 <= j <= 151:
        month = 5
        day_number = j - 120
    if 152 <= j <= 181:
        month = 6
        day_number = j - 151
    if 182 <= j <= 212:
        month = 7
        day_number = j - 181
    if 213 <= j <= 243:
        month = 8
        day_number = j - 212
    if 244 <= j <= 273:
        month = 9
        day_number = j - 243
    if 274 <= j <= 304:
        month = 10
        day_number = j - 273
    if 305 <= j <= 334:
        month = 11
        day_number = j - 304
    if 335 <= j <= 365:
        month = 12
        day_number = j - 334
    return month, day_number

def daily_ave(t_max, t_min):
    for r in range (len(t_max[:, 0])):
        for c in range (len(t_max[0, :])):
            if t_max[r,c] != -99 and t_min[r,c] != -99:
                t_ave = (t_max + t_min) / 2
            else:
                t_ave = -99
    return t_ave

def annual_ave_t(a_in):
    annual_avg = np.mean(a_in, axis = 1)
    return annual_avg

def monthly_ave_t(a_in, m_no, yr_s, yr_e):
    list_month_ave = []
    for year in range(yr_s, yr_e +1):
        if m_no == 1:
            month_range = a_in[year - 1893, :31]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 2:
            month_range = a_in[year - 1893, 31:59]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 3:
            month_range = a_in[year - 1893, 59:90]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 4:
            month_range = a_in[year - 1893, 90:120]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 5:
            month_range = a_in[year - 1893, 120:151]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 6:
            month_range = a_in[year - 1893, 151:181]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 7:
            month_range = a_in[year - 1893, 181:212]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 8:
            month_range = a_in[year - 1893, 212:243]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 9:
            month_range = a_in[year - 1893, 243:273]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 10:
            month_range = a_in[year - 1893, 273:304]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 11:
            month_range = a_in[year - 1893, 304:334]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        if m_no == 12:
            month_range = a_in[year - 1893, 334:365]
            month_avg = clc_ave(month_range)
            list_month_ave.append(month_avg)
        year += 1
    return list_month_ave

def rank_list(l_in, yr_b):
    a_list = []
    temp_idx = 0
    for temp in l_in:
        a_list.append([temp, yr_b + temp_idx])
        temp_idx += 1
    switch_temp = True
    while switch_temp:
        switch_temp = False
        for n in range(len(a_list) - 1):
            if a_list[n][0] < a_list[n+ 1][0]:
                switch_temp = True
                a_list[n], a_list[n + 1] = a_list[n+1], a_list[n]
    switch_year = True
    while switch_year:
        switch_year = False
        for n in range(len(a_list) - 1):
            if a_list[n][0] == a_list[n+1][0] and a_list[n][1] < a_list[n+1][1]:
                switch_year = False
                a_list[n], a_list[n+1] = a_list[n+1], a_list[n]
    return a_list

def plot_temp_vs_day(t_list):
    # Point plot a function with ticked x and y axes
    wn = t.Screen()
    # graph window
    x_min = -5.0
    x_max = 370.0
    y_min = -100.0
    y_max = 100.0
    # tick info
    t_l = 0.2
    x_t_space = 0.5
    y_t_space = 0.5
    wn.setworldcoordinates(x_min, y_min, x_max, y_max)
    alex = t.Turtle()
    # Draw x axis
    alex.up()
    alex.goto(x_min, 0.0)
    alex.down()
    alex.goto(x_max, 0.0)
    alex.up()
    # Draw the y axis
    alex.goto(0.0, y_min)
    alex.down()
    alex.goto(0.0, y_max)
    alex.up()
    # Draw the x tick marks
    n_x_ticks = int((x_max - x_min) / x_t_space) + 1
    for tick in range(n_x_ticks):
        loc = x_min + tick * x_t_space
        alex.up()
        alex.goto(loc, -t_l * 0.5)
        alex.down()
        alex.goto(loc, t_l * 0.5)
        alex.up()
        # Draw the y tick marks
    n_y_ticks = int((y_max - y_min) / y_t_space) + 1
    for tick in range(n_y_ticks):
        loc = y_min + tick * y_t_space
        alex.up()
        alex.goto(-t_l * 0.5, loc)
        alex.down()
        alex.goto(t_l * 0.5, loc)
        alex.up()
        # Plot the function points
    alex.color('blue')
    alex.up()
    for tick in range(n_x_ticks):
        x = x_min + tick * x_t_space
        alex.goto(x, x * x / 10 - 5)
        alex.dot(2)
        # always the last line
    wn.exitonclick()

def n_day_average(a_in, n):
    a_flat = a_in.flatten()
    b_flat = np.zeros(len(a_flat), dtype=float)
    for i in range(len(a_flat)):
        if i < n - 1:
            day_ave = - 99
        else:
            if -99 in a_flat[(i - n): i]:
                day_ave = -99
            else:
                sum = 0
                for x in range((i - n), i):
                    sum += a_flat[x]
                day_ave = sum/n
        b_flat[i] = day_ave
    n_ave = b_flat.reshape(len(a_in[:,0]), len(a_in[0, :]))

    return n_ave



def main():
    t_max = read_data('max_temp')
    t_min = read_data('min_temp')
    print(daily_ave(t_max, t_min))
    print(n_day_average(t_max, 3))






main()
