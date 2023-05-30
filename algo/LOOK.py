

tracks = [15, 4, 40, 11, 35, 7, 14]
FIRST_TRACK = min(tracks)
LAST_TRACK = max(tracks)
INITIAL_POS = tracks[0]

def total_number_of_tracks(tracks):
    tr = tracks.copy()
    global directional_bit
    cur = INITIAL_POS
    sum_ = 0
    tr.remove(cur)
    for i in range(INITIAL_POS, LAST_TRACK):
        if i in tr:
            sum_ += abs(cur-i)
            cur = i
            tr.remove(cur)
    for i in range(LAST_TRACK, FIRST_TRACK-1, -1):
        if i in tr:
            sum_ += abs(cur-i)
            cur = i
            tr.remove(cur)
    return sum_

def average_number_of_tracks(tracks):
    return total_number_of_tracks(tracks)/(len(tracks)-1)


def main():
    print("Total Number of Tracks Traveled = {0} ms".format(total_number_of_tracks(tracks)))
    print("Average Number of Tracks Traveled = {0} ms".format(average_number_of_tracks(tracks)))
main()