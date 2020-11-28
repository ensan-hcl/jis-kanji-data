with open("resource/kanji.txt") as f:
    string = f.read()
lines = string.split('\n')
data = [line.split('\t') for line in lines]


result = []
for line in data[1:]:
    if len(line[4]) != 0:
        result.append([chr(int(line[3][2:], 16)), line[3], line[27], line[28]])

for target in ["jis1", "jis2", "jis3", "jis4"]:
    with open(f"result/{target}.txt") as f:
        kanjis = f.read()

    filtered = list(filter(lambda x: x[0] in kanjis, result))

    write_string = '\n'.join(['\t'.join(line) for line in filtered])
    with open(f"result/kanji_{target}.tsv", mode='w') as f:
        f.write(write_string)
