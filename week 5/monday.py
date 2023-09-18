import pathlib

# the "normal way"

# infile = open('text.ihatezoom', 'r', encoding='utf-8')
# text = infile.read()
# infile.close()

# more advanced just read a file in

with open('text.ihatezoom', 'r', encoding='utf-8') as infile:
    text = infile.read()

p = pathlib.Path('text.ihatezoom')

# print(p, p.stem, p.parent, p.parts, p.suffix)
# print(p.absolute())
# print(type(p))
# print(type(p.parent), p.parent.absolute())
# for something in pathlib.Path('data.tar.gz').parents:
#     print(something)

print(pathlib.Path('data.tar.gz').suffixes)

# folder = pathlib.Path('..')
# print(folder.absolute())

target = pathlib.Path('outputdata')

print(target, target.absolute())

target.mkdir(exist_ok=True)
# print(target.exists())
# print(target.is_dir())

p1 = pathlib.Path('data1.txt')
# print(p1.exists())
p1.write_text("here's some text")

for i in range(8, 25):
    fname = "data-" + str(i).zfill(3) + ".txt"
    p = pathlib.Path(fname)
    final_outfile = target / fname
    # print(final_outfile)
    if final_outfile.exists():
        print("already done")
    else:
        final_outfile.write_text(str(i).zfill(20) + "hello")

# print(list(target.glob("*.txt")))

for p in target.glob("*.txt"):
    print(p.read_text())