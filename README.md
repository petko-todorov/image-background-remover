## 📷 Batch Background Remover

A Python script to batch-remove image backgrounds using two different `rembg` models (`isnet-general-use` and `u2netp`).
The script automatically compares results from both models and saves the best output based on non-transparent pixel
counts.

---

### ✨ Features

* Supports multiple image formats (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.webp`)
* Automatically processes all images in a folder
* Chooses the best result between two background removal models
* Saves processed images to an `Output` subdirectory
* Opens the output folder after the process

---

### 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/petko-todorov/image-background-remover.git
   cd image-background-remover
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install requirements**

   ```bash
   pip install -r requirements.txt
   ```

---

### ▶️ Usage

Run the script (after activating your virtual environment):

```bash
python background_remover.py
```

You'll be prompted to enter the directory containing images.

* Leave it empty to use the current directory.
* Processed images will be saved in a subfolder called `Output`.

---

### 🖼️ Supported Formats

* `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.webp`

---

### ⚐️ How It Works

* Loads each image and runs two background removal models:
    * `isnet-general-use`
    * `u2netp`
* Compares the two outputs by counting non-transparent pixels.
* Saves the better output as a `.png` in the `Output` folder.
* Automatically opens the output directory in your default web browser.

---

### 📁 Project Structure

```
image-background-remover/
├── LICENSE
├── README.md
├── background_remover.py
└── requirements.txt
```

---

### ⚙️ Requirements

* Python 3.9+
* See `requirements.txt` for all dependencies.

---

### 📄 License

This project is licensed under the MIT License.
