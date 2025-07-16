from PIL import Image
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python convert_icon.py <input_png_path> <output_ico_path>")
        sys.exit(1)

    input_png_path = sys.argv[1]
    output_ico_path = sys.argv[2]

    try:
        img = Image.open(input_png_path)
        img.save(output_ico_path, format="ICO")
        print(f"Imagem {input_png_path} convertida com sucesso para {output_ico_path}")
    except Exception as e:
        print(f"Erro ao converter imagem: {e}")
        sys.exit(1)


