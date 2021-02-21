import jsonlines

with jsonlines.open(r"C:\Users\Dell-2\Documents\projects\Assignment3\data\annotations.jsonl") as f:
    line = f.read()
    print(line)
    print(line["img_fn"])
    # idx = 2
    # while idx > 0:
    #     line = f.read()
    #     print(line)
    #     idx = idx-1
    # print(line)