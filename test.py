# Tải mô hình đã lưu
model = load_model('my_model.h5')

image_path = None

def load_image():
    global image_path
    file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_path = file_path  # Lưu đường dẫn ảnh
        display_image(file_path)  # Hiển thị ảnh lên giao diện

def predict_number():
    global image_path
    if image_path:
        try:
            img = Image.open(image_path).convert('L')  # Chuyển sang grayscale
            img = img.resize((28, 28))  # Đảm bảo kích thước 28x28
            img_array = np.array(img) / 255.0  # Chia cho 255 để chuẩn hóa
            img_array = img_array.reshape(1, 28, 28, 1)  # Định dạng lại cho mô hình

            # Dự đoán
            predictions = model.predict(img_array)
            predicted_number = np.argmax(predictions)  # Lấy chỉ số của lớp có xác suất cao nhất

            # Hiển thị kết quả
            messagebox.showinfo("Kết quả dự đoán", f"Chữ số dự đoán: {int(predicted_number)}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xử lý hình ảnh: {e}")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng tải ảnh trước khi dự đoán.")

def display_image(file_path):
    img = Image.open(file_path).resize((200, 200))  # Thay đổi kích thước để hiển thị
    img_tk = ImageTk.PhotoImage(img)
    img_label.config(image=img_tk)
    img_label.image = img_tk  # Giữ tham chiếu đến ảnh để tránh bị garbage collection

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Nhận diện chữ số qua ảnh")

# Nút dự đoán
predict_button = tk.Button(root, text="Dự đoán", command=predict_number)
predict_button.pack(pady=10)

# Nút tải ảnh
load_button = tk.Button(root, text="Tải ảnh", command=load_image)
load_button.pack(pady=20)

# Nhãn để hiển thị ảnh
img_label = tk.Label(root)
img_label.pack(pady=10)

# Bắt đầu vòng lặp sự kiện (main loop)
root.mainloop()