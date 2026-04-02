import cv2
import imageio
import argparse
import numpy as np

def create_gif(input_path, output_path, num_frames, width=None):
    cap = cv2.VideoCapture(input_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if total_frames <= 0:
        print("Ошибка: Не удалось прочитать видео.")
        return

    # Рассчитываем индексы кадров равномерно
    indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)
    frames = []

    print(f"Обработка {num_frames} кадров...")

    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if not ret:
            break
        
        # Конвертация в RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Изменение размера, если указано
        if width:
            height = int(frame.shape[0] * (width / frame.shape[1]))
            frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
            
        frames.append(frame)

    cap.release()

    print(f"Сохранение в {output_path}...")
    imageio.mimsave(output_path, frames, fps=10, loop=0)
    print("Готово!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Входное видео")
    parser.add_argument("-o", "--output", default="result.gif", help="Выходной GIF")
    parser.add_argument("-n", "--num", type=int, default=20, help="Кол-во кадров")
    parser.add_argument("-w", "--width", type=int, help="Ширина (опционально)")

    args = parser.parse_args()
    create_gif(args.input, args.output, args.num, args.width)