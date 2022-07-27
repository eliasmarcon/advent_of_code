with open("input") as f:
    flight_seats = f.read().splitlines()


# print(flight_seats)
# test = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

def get_seat(flight_input):
    seat_ids = []

    for flight_seat in flight_input:
        row_string = flight_seat[:7]
        col_string = flight_seat[7:]
        row_numbers = list(range(128))
        col_numbers = list(range(8))
        row_number = 0
        col_number = 0

        for char_row in row_string:
            if char_row == "F":
                until_rf = int(len(row_numbers) / 2)
                row_numbers = row_numbers[:until_rf]
            else:
                until_rb = int(len(row_numbers) / 2)
                row_numbers = row_numbers[until_rb:]
            if len(row_numbers) == 1:
                for row in row_numbers:
                    row_number = row

        for char_col in col_string:
            if char_col == "L":
                until_cl = int(len(col_numbers) / 2)
                col_numbers = col_numbers[:until_cl]
            else:
                until_cr = int(len(col_numbers) / 2)
                col_numbers = col_numbers[until_cr:]
            if len(col_numbers) == 1:
                for col in col_numbers:
                    col_number = col

        seat_ids.append(row_number * 8 + col_number)

    return seat_ids


all_seats = get_seat(flight_seats)
all_seats.sort()
max_seat_id = max(all_seats)

print("Solution Part 1:", max_seat_id)


# Part 2
my_seat = 0

for i in range(min(all_seats), max(all_seats) + 1):
    if i not in all_seats:
        my_seat = i

print("Solution Part 2:", my_seat)
