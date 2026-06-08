def parse_input(text):
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]

    N = int(lines[0])
    M = int(lines[1])

    cities = []

    for i in range(M):
        parts = lines[i + 2].split()

        name = " ".join(parts[:-2])
        x = int(parts[-2])
        y = int(parts[-1])

        cities.append({
            "name": name,
            "x": x,
            "y": y
        })

    return N, M, cities