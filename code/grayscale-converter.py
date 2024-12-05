import os
import sys
from PIL import Image

def generate_output_filename(input_file_path):
    # もし出力先ディレクトリがなければ作成
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    file_name, file_etx = os.path.splitext(os.path.basename(input_file_path))

    return os.path.join(output_dir, f"{file_name}-converted{file_etx}")

def process_image(input_file_path):
    # 画像を取得してグレースケールにする
    target_image = Image.open(input_file_path)
    converted_image = target_image.convert("L")

    # 出力先パス・ファイル名を取得して保存
    output_file_path = generate_output_filename(input_file_path)
    converted_image.save(output_file_path)
    print(f"saved at: {output_file_path}")

if  __name__ == "__main__":
    # 画像パスが指定されなかった場合
    if len(sys.argv) < 2:
        print("Script needs file_path.")
        sys.exit(1)

    process_image(sys.argv[1])