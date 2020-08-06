from pathlib import Path

book_dir = Path(__file__).absolute() / 'book'
book_path = Path(book_dir)

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

    with open(book_dir + '%s.asc' % dir_name, 'w', encoding='utf8') as f:
        f.write(l_s)
