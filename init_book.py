from pathlib import Path

book_dir = str(Path(__file__).parent.absolute()) + '/book'
book_path = Path(book_dir)

print('book path: %s' % book_dir)

for i in book_path.glob('**/*'):
    if i.is_file():
        continue

    dir_name = i.name

    l_s = '[#%s]\n' \
          '== %s\n\n' % (dir_name, dir_name)

    sub_dir = book_path / dir_name

    for file in sub_dir.glob('**/*'):
        if file.suffix == '.asc':
            l_s += 'include::%s/%s[]\n' % (dir_name, file.name)

    filename = book_dir + '/%s.asc' % dir_name
    print('写入 %s' % filename)
    with open(filename, 'w', encoding='utf8') as f:
        f.write(l_s)
