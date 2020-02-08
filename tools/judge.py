import test
import glob

def message():
    print('入力ファイルと出力ファイルの数を等しくしてください。')
    exit(1)

if __name__ == '__main__':
    in_paths = glob.glob('./input/*.txt')
    out_paths = glob.glob('./output/*.txt')
    if len(in_paths) != len(out_paths):
        message()
    for in_path, out_path in zip(in_paths, out_paths):
        with open(in_path) as in_f:
            output = str(test.test(input=in_f))
        with open(out_path) as out_file:
            ans = out_file.read()
        res = 'AC!' if ans == output else 'WA...'
        print(f'テスト{in_paths.index(in_path) + 1}: {res}')
        print(f'期待される出力: {ans}')
        print(f'あなたの出力: {output}')