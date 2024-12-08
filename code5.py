def find_strongest_trainees():
    print("Enter the strength levels (12 values):")
    strength_levels = [int(input()) for _ in range(12)]
    
    if any(level < 1 or level > 200 for level in strength_levels):
        print("INVALID INPUT")
        return
    trainees = [strength_levels[i::4] for i in range(4)]
    averages = [round(sum(trainee) / 3) for trainee in trainees]
    max_average = max(averages)
    if max_average < 100:
        print("All trainees are unfit")
        return
    strongest_trainees = [i + 1 for i, avg in enumerate(averages) if avg == max_average]
    for trainee in strongest_trainees:
        print(f"Trainee Number : {trainee}")
find_strongest_trainees()
