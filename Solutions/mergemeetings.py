def merge(meetings):
    sorted_meetings = sorted(meetings)
    merged_meetings = [sorted_meetings[0]]
    for sorted_meetings_start, sorted_meetings_end in sorted_meetings:
        last_merged_meetings_start, last_merged_meeting_end = merged_meetings[-1]
        if sorted_meetings_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meetings_start, sorted_meetings_end)
        else:
            merged_meetings.append((sorted_meetings_start, sorted_meetings_end))
    return merged_meetings

arr = [(0, 6), (2, 6), (7, 10)]
print(merge(arr))
