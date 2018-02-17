'''
Your monthly phone bill has just arrived, and it's unexpectedly large. You decide to verify the amount by recalculating the bill
based on your phone call logs and the phone company's charges.

The logs are given as a string S consisting of N lines separated by end-of-lie characters (ASCII code 10). Each line describes
one phone call using the following format: "hh:mm:ss,nnn-nnn-nnn", where "hh:mm:ss" denotes the duration of the call (in "hh"
hours, "mm" minutes and "ss" seconds) and "nnn-nnn-nnn" denotes the 9-digit phone number of the recipient (with no leading zeros).

Each call is billed separately. The billing rules are as follows:

    - If the call was shorter than 5 minutes, then pay 3 cents for every started second of the call (e.g. for duration "00:01:07"
        you pay 67 * 3 = 201 cents).
    - If the call was at least 5 minutes long, then you pay 150 cents for every started minute of the call (e.g. for duration
        "00:05:00" you pay 5 * 150 = 750 cents and for duration "00:05:01" you pay 6 * 150 = 900 cents).
    - All calls to the phone number that has the longest total duration of calls are free. In the case of a tie, if more than one phone
        number shares the longest total duration, the promotion is applied only to the phone numebr whose numerical value is the smallest
        among these phone numbers.


Write a function:

    def solution(S)

that, given a string S describe phone call logs, return the amount of money you have to pay in cents.

For example, given string  S with N = 3 lines:

    "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090"

The function should return 900 (the total duration for number 400-234-090 is 6 minutes 7 seconds, and the total duration for number
701-080-080 is 5 minutes 1 second; therefore, the free promotion applies to the former phone number).
'''

def solution(S):
    logs = S.split("\n")
    total_charge = 0
    call_length_map = {}

    for log in logs:
        log = log.split(",")
        call_duration_in_seconds = parse_duration_in_seconds(log[0])
        phone_number = log[1]

        if phone_number not in call_length_map:
            call_length_map[phone_number] = call_duration_in_seconds
        else:
            call_length_map[phone_number] += call_duration_in_seconds


    # Delete the one with the longest value in dictionary. 
    # Only when there is more than one phone number, this case applies.
    call_length_map = promotion(call_length_map)



    for v in call_length_map.values():
        total_charge += calculate_charge(v)

    return total_charge


def promotion(call_length_map):
    if len(call_length_map) > 1:
        val_to_delete = max(call_length_map.values())
        keys_to_delete = [k for k, v in call_length_map.items() if v == val_to_delete]
        min_number = min(keys_to_delete)
        del call_length_map[min_number]

    return call_length_map


def calculate_charge(duration_in_seconds):
    if duration_in_seconds < 300:
        return duration_in_seconds * 3

    if duration_in_seconds % 60:
        duration_in_minutes = duration_in_seconds // 60 + 1
        return duration_in_minutes * 150
    else:
        return duration_in_seconds / 60 * 150


def parse_duration_in_seconds(call_duration):
    time = call_duration.split(":")
    return int(time[1][1]) * 60 + int(time[2])
