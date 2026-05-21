total_seconds = 0

while True:
    time = input("Enter time in the format HH MM SS (or 'done' to finish): ")
    if time.lower() == 'done':
        break
    h, m, s = map(int, time.split())
    total_seconds += h*3600 + m*60 + s
    print(f"Net time: {total_seconds//3600}:{(total_seconds%3600)//60}:{total_seconds%60}")