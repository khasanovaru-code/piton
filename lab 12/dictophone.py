import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import tkinter as tk
from tkinter import filedialog
import threading

class Dictaphone:

    def __init__(self, sample_rate=44100, channels=1):
        self.sample_rate = sample_rate
        self.channels = channels
        self.audio_chunks = []
        self.audio_data = None
        self.is_recording = False

    def record(self):
        self.is_recording = True
        self.audio_chunks = []

        print("Началась запись")

        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            callback=self.callback):

            while self.is_recording:
                sd.sleep(100)

    def callback(self, indata, frames, time, status):
        self.audio_chunks.append(indata.copy())

    def stop(self):
        self.is_recording = False

        if self.audio_chunks:
            self.audio_data = np.concatenate(self.audio_chunks)

        print("Запись остановлена")

    def save(self, filename="output.wav"):
        if self.audio_data is None:
            print("Нет данных для сохранения")
            return

        write(
            filename,
            self.sample_rate,
            (self.audio_data * 32767).astype(np.int16)
        )

        print("Файл сохранён:", filename)

    def detect_animal(self):
        if self.audio_data is None:
            return "Запись не найдена"

        audio = self.audio_data[:, 0]

        spectrum = np.abs(np.fft.rfft(audio))
        freqs = np.fft.rfftfreq(len(spectrum), 1 / self.sample_rate)

        peak_freq = freqs[np.argmax(spectrum)]

        print("Основная частота:", int(peak_freq), "Гц")

        if peak_freq > 600:
            return "Кот (мяу)"
        else:
            return "Собака (гав)"

class DictaphoneApp:

    def __init__(self, master):

        self.master = master
        master.title('Диктофон + распознавание')
        master.geometry('300x250')

        self.dictaphone = Dictaphone()

        tk.Button(master, text='Record',
                  command=self.start_recording).pack(pady=5)

        tk.Button(master, text='Stop',
                  command=self.stop_recording).pack(pady=5)

        tk.Button(master, text='Save',
                  command=self.save_recording).pack(pady=5)

        self.label = tk.Label(
            master,
            text="Результат: ---",
            font=("Arial", 16)
        )
        self.label.pack(pady=15)

    def start_recording(self):
        t = threading.Thread(target=self.dictaphone.record)
        t.start()

    def stop_recording(self):
        self.dictaphone.stop()
        result = self.dictaphone.detect_animal()
        self.label.config(text=f"Результат: {result}")
        print(result)

    def save_recording(self):
        filename = filedialog.asksaveasfilename(
            defaultextension='.wav',
            filetypes=[("WAV files", '*.wav')]
        )

        if filename:
            self.dictaphone.save(filename)

if __name__ == '__main__':
    root = tk.Tk()
    app = DictaphoneApp(root)
    root.mainloop()
