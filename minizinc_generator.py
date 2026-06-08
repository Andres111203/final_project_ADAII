def generate_minizinc(N, M, cities):

    x_values = [str(city["x"]) for city in cities]
    y_values = [str(city["y"]) for city in cities]

    model = f"""
int: N = {N};
int: M = {M};

array[1..M] of int: cityX = [{",".join(x_values)}];
array[1..M] of int: cityY = [{",".join(y_values)}];

var 0..N: x;
var 0..N: y;

array[1..M] of var int: d;

constraint
forall(i in 1..M)(
    d[i] = abs(x - cityX[i]) + abs(y - cityY[i])
);

constraint
forall(i in 1..M)(
    x != cityX[i] \\/ y != cityY[i]
);

var 0..(2*N): maxDist;
var 0..(2*N): minDist;

constraint maxDist = max(d);
constraint minDist = min(d);

solve minimize 1000 * maxDist + (maxDist - minDist);

output [
    "Concierto en: (",
    show(x),
    ",",
    show(y),
    ")\\n",
    "MaxDist = ",
    show(maxDist),
    "\\n",
    "MinDist = ",
    show(minDist)
];
"""

    return model