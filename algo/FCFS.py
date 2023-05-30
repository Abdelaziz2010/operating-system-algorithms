
tracks = [15, 4, 40, 11, 35, 7, 14]
initial_pos = tracks[0]
final_pos = tracks[-1]

def total_number_of_tracks(tracks):
    sum_ = 0
    for i in range(len(tracks) - 1):
        sum_ += abs(tracks[i] - tracks[i+1])
    return sum_

def average_number_of_tracks(tracks):
    return total_number_of_tracks(tracks)/(len(tracks)-1)


def main():
    print("Total Number of Tracks Traveled = {0} ms".format(total_number_of_tracks(tracks)))
    print("Average Number of Tracks Traveled = {0} ms".format(average_number_of_tracks(tracks)))
    print("Final Arm Postion: {0}".format(final_pos))
main()