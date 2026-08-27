# Hướng dẫn sử dụng Template Báo cáo Tuần Đồ Án Chuyên Ngành (DACN)

Cấu trúc dự án LaTeX báo cáo tiến độ hàng tuần được module hóa theo chuẩn học thuật, giúp việc soạn thảo báo cáo nhanh chóng, dễ quản lý và đồng nhất xuyên suốt quá trình làm đồ án.

---

## 1. Hướng dẫn cài đặt môi trường (Environment Setup)

Để biên dịch và làm việc với LaTeX hiệu quả trên Windows, cần cài đặt các thành phần sau:

### 1.1. Cài đặt MiKTeX (LaTeX Engine)
- **Tải bộ cài đặt:** Truy cập [https://miktex.org/download](https://miktex.org/download) và tải bản **MiKTeX Windows Installer**.
- **Lưu ý quan trọng khi cài đặt:**
  - Ở bước thiết lập **"Install missing packages on-the-fly"**, hãy chọn **`Yes`** (thay vì `Ask me first`). Tùy chọn này giúp MiKTeX tự động tải các package còn thiếu trong quá trình biên dịch mà không hiện hộp thoại hỏi xác nhận.
  - Sau khi cài xong, mở **MiKTeX Console** từ Start Menu và chọn **"Check for updates"** để cập nhật package lên bản mới nhất.

---

### 1.2. Cài đặt Strawberry Perl (Hỗ trợ `latexmk`)
Công cụ `latexmk` (tự động biên dịch nhiều lần để cập nhật cross-reference và dọn dẹp file phụ) yêu cầu môi trường Perl trên Windows.
- **Cách 1 (Cài qua Terminal / PowerShell):**
  ```powershell
  winget install StrawberryPerl.StrawberryPerl
  ```
- **Cách 2:** Tải file cài đặt `.msi` tại [https://strawberryperl.com/](https://strawberryperl.com/).

---

### 1.3. Cài đặt Extension LaTeX Workshop trên VS Code
- Mở VS Code, nhấn tổ hợp phím `Ctrl + Shift + X` để mở mục Extensions.
- Tìm kiếm extension: **`LaTeX Workshop`** (Extension ID: `James-Yu.latex-workshop`) của tác giả **James Yu**.
- Nhấn **Install**.

> [!NOTE]
> Dự án đã được cấu hình sẵn file [`.vscode/settings.json`](file:///.vscode/settings.json). Khi mở thư mục dự án bằng VS Code, LaTeX Workshop sẽ tự động:
> - Xem trước file PDF ngay trong tab bên cạnh (`View PDF in tab`).
> - Tự động dọn dẹp các file trung gian (`.aux`, `.log`, `.fls`,...) sau khi build.
> - Hỗ trợ điều hướng 2 chiều giữa mã nguồn TeX và PDF (**SyncTeX**).

---

### 1.4. Các phím tắt thông dụng trong VS Code

| Thao tác | Phím tắt / Cách thực hiện |
| :--- | :--- |
| **Biên dịch (Build PDF)** | `Ctrl + Alt + B` (hoặc nhấn nút Play ở góc trên bên phải) |
| **Xem PDF (View PDF Preview)** | `Ctrl + Alt + V` (hoặc biểu tượng tab PDF ở góc trên) |
| **SyncTeX (Từ TeX sang PDF)** | `Ctrl + Alt + J` (con trỏ tại dòng TeX sẽ nhảy tới trang PDF tương ứng) |
| **SyncTeX (Từ PDF về TeX)** | Giữ phím `Ctrl` + Click chuột trái vào chữ bất kỳ trên PDF |
| **Dọn dẹp file phụ (.aux, .log)** | `Ctrl + Alt + C` |

---

## 2. Cấu trúc thư mục dự án

```text
weekly-report-DACN/
│
├── .gitignore                      # Bỏ qua các file phụ sinh ra khi biên dịch
├── .latexmkrc                      # Cấu hình lệnh latexmk
├── .vscode/                        # Cấu hình workspace cho VS Code
│   └── settings.json
├── README.md                       # Tài liệu hướng dẫn
│
├── style/                          # [DÙNG CHUNG] Định dạng giao diện & Macro
│   ├── weeklyreport.sty            # Package định nghĩa gói lệnh, font, màu sắc, header/footer
│   └── macros.tex                  # Macro tiện ích (\badge, \pbar, \takeaway, issuebox,...)
│
├── template/                       # [KHUÔN MẪU] Template sạch (clean skeleton)
│   ├── main.tex                    # File biên dịch chính (nạp các module)
│   ├── config.tex                  # Metadata của tuần (Số tuần, thời gian, tác giả,...)
│   └── sections/                   # Các phần nội dung của báo cáo
│       ├── 01_summary.tex          # 1. Executive Summary & Progress tracker
│       ├── 02_completed.tex        # 2. Completed Tasks & Time log
│       ├── 03_results.tex          # 3. Results & Visualization
│       ├── 04_issues.tex           # 4. Issues & Blockers
│       ├── 05_next_week.tex        # 5. Next Week's Plan
│       ├── 06_references.tex       # 6. References & Datasets
│       └── appendix.tex            # Phụ lục (Detailed daily time log)
│
├── reports/                        # [BÁO CÁO TỪNG TUẦN]
│   ├── week-01/                    # Thư mục báo cáo Tuần 1
│   │   ├── main.tex
│   │   ├── config.tex
│   │   ├── figures/                # Hình ảnh riêng của Tuần 1
│   │   └── sections/
│   └── week-02/ ...
│
├── shared-assets/                  # [TÀI NGUYÊN CHUNG CHO TOÀN DỰ ÁN]
│   ├── figures/                    # Logo, sơ đồ kiến trúc hệ thống dùng chung
│   ├── bib/
│   │   └── references.bib          # File BibTeX chứa tài liệu tham khảo chung
│   └── examples/
│       └── gallery.tex             # Kho mẫu code TikZ, bảng biểu, biểu đồ, subfigure
│
└── scripts/
    └── new_week.ps1                # Script PowerShell tự động tạo tuần mới
```

---

## 3. Quy trình làm việc hàng tuần

### Bước 1: Tạo thư mục tuần mới
Chạy script PowerShell từ thư mục gốc của dự án:
```powershell
# Tạo báo cáo cho Tuần 3
.\scripts\new_week.ps1 3

# Tạo báo cáo cho Tuần 4
.\scripts\new_week.ps1 4
```
Script sẽ tự động:
- Tạo thư mục `reports/week-XX/` với các khung section sạch.
- Cập nhật số tuần trong `config.tex`.
- Tạo sẵn thư mục `reports/week-XX/figures/`.

### Bước 2: Cập nhật thông tin và viết nội dung
1. Mở file `reports/week-XX/config.tex` để cập nhật khoảng thời gian báo cáo (`WeekRange`) và giai đoạn đồ án (`PhaseName`).
2. Mở từng file trong `reports/week-XX/sections/` để viết nội dung tương ứng:
   - `01_summary.tex`: Tóm tắt tiến độ, mục tiêu và bảng `Progress tracker`.
   - `02_completed.tex`: Các đầu việc đã hoàn thành (`C1`, `C2`,...) kèm link bằng chứng (commit/PR).
   - `03_results.tex`: Kết quả thực nghiệm, hình ảnh, bảng dữ liệu, biểu đồ.
   - `04_issues.tex`: Khó khăn gặp phải, mức độ ảnh hưởng, vấn đề cần GVHD hướng dẫn.
   - `05_next_week.tex`: Kế hoạch các đầu việc tuần tới.

### Bước 3: Biên dịch ra PDF
Mở file `reports/week-XX/main.tex` và nhấn `Ctrl + Alt + B` trong VS Code (hoặc gõ lệnh `latexmk -pdf main.tex` / `pdflatex main.tex`).

---

## 4. Hướng dẫn thêm Hình ảnh và Trích dẫn

### 4.1. Thêm hình ảnh
- **Hình ảnh riêng của tuần:** Chép file ảnh vào `reports/week-XX/figures/` (ví dụ: `loss.png`). Gọi trực tiếp tên file trong TeX mà không cần gõ thêm đường dẫn thư mục:
  ```latex
  \begin{figure}[H]
  \centering
  \includegraphics[width=0.8\linewidth]{loss.png}
  \caption{Đồ thị hàm mất mát theo từng epoch.}
  \label{fig:loss}
  \end{figure}
  \takeaway{Hàm loss hội tụ ổn định sau epoch 40 mà không bị overfitting.}
  ```
- **Hình ảnh dùng chung nhiều tuần:** Chép file ảnh vào `shared-assets/figures/` (ví dụ: `logo.png`). Gọi trực tiếp: `\includegraphics[width=0.3\linewidth]{logo.png}`.

### 4.2. Mẫu định dạng tham khảo (Gallery)
Khi cần chèn sơ đồ TikZ phức tạp, 2 ảnh cạnh nhau (`subfigure`), ảnh cạnh bảng (`minipage`), văn bản quấn quanh ảnh (`wrapfigure`), biểu đồ cột (`pgfplots`), hoặc khung code Python:
👉 Mở file [`shared-assets/examples/gallery.tex`](file:///f:/latex/weekly-report-DACN/shared-assets/examples/gallery.tex), sao chép đoạn code mẫu cần dùng và dán vào `03_results.tex`.

### 4.3. Thêm trích dẫn BibTeX
- Dán citation vào file `shared-assets/bib/references.bib`.
- Trong bài viết, sử dụng lệnh `\cite{key_name}` để trích dẫn.

---

## 5. Bảng tra cứu các Macro có sẵn

| Macro | Ý nghĩa / Ví dụ sử dụng |
| :--- | :--- |
| `\badge{ok}{Done}` | Nhãn trạng thái màu: `\Done`, `\WIP`, `\Blocked`, `\Planned` |
| `\pbar{75}` | Thanh tiến độ trực quan 75% |
| `\takeaway{...}` | 1–2 câu nhận xét/kết luận bắt buộc bên dưới hình hoặc bảng |
| `\evi{url}{label}` | Link dẫn tới bằng chứng (commit / PR / notebook) |
| `\ph[width]{text}` | Khung placeholder tạm thời khi chưa có hình ảnh |
| `\begin{issuebox}{Title}` | Khung nổi bật để mô tả một issue/khó khăn |
| `\begin{notebox}[Title]` | Khung ghi chú / quyết định thiết kế |
