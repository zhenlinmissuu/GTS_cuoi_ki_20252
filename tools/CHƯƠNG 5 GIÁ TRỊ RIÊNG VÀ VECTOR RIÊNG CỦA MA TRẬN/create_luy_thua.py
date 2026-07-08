import json
import os

notebook_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN/Phương pháp Lũy thừa.ipynb"

nb = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Phương pháp Lũy thừa (Power Method)\n",
    "Dùng để tìm Trị riêng có giá trị tuyệt đối lớn nhất (Trị riêng trội) và Véctơ riêng tương ứng của ma trận $A$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from IPython.display import display, Math\n",
    "\n",
    "def Power_Method(A_input, x0_input=None, tol=1e-5, max_iter=20):\n",
    "    def matrix_to_latex(M, precision=4):\n",
    "        if not isinstance(M, np.ndarray): return str(M)\n",
    "        elif M.ndim == 1:\n",
    "            inner = \" \\\\\\\\ \".join([f\"{x:.{precision}f}\" for x in M])\n",
    "            return f\"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}\"\n",
    "        else:\n",
    "            rows = \" \\\\\\\\ \".join([\" & \".join([f\"{x:.{precision}f}\" for x in row]) for row in M])\n",
    "            return f\"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}\"\n",
    "\n",
    "    A = np.array(A_input, dtype=float)\n",
    "    n = A.shape[0]\n",
    "    \n",
    "    if x0_input is None:\n",
    "        x_k = np.ones(n)\n",
    "    else:\n",
    "        x_k = np.array(x0_input, dtype=float).flatten()\n",
    "        \n",
    "    print(\"=\"*60)\n",
    "    print(\"PHƯƠNG PHÁP LŨY THỪA TÌM TRỊ RIÊNG TRỘI\")\n",
    "    print(\"=\"*60)\n",
    "    \n",
    "    lam_prev = 0\n",
    "    \n",
    "    for k in range(1, max_iter + 1):\n",
    "        print(f\"\\n--- BƯỚC {k} ---\")\n",
    "        \n",
    "        # Tính y = A * x_k\n",
    "        y_k = A @ x_k\n",
    "        \n",
    "        # Trị riêng xấp xỉ theo tỉ số chuẩn (hoặc tỉ số Rayleigh)\n",
    "        # Ở đây ta dùng phần tử có trị tuyệt đối lớn nhất của y_k\n",
    "        idx = np.argmax(np.abs(y_k))\n",
    "        lam_k = y_k[idx] / x_k[idx] if x_k[idx] != 0 else np.linalg.norm(y_k)\n",
    "        \n",
    "        # Chuẩn hóa (lấy phần tử lớn nhất làm mốc để chia, hoặc chia cho chuẩn)\n",
    "        # Thường trong thi tự luận, ta chia cho phần tử max để x_k luôn có số 1\n",
    "        c = y_k[idx]\n",
    "        x_new = y_k / c\n",
    "        \n",
    "        display(Math(f\"y_{{{k}}} = A x_{{{k-1}}} = {matrix_to_latex(y_k, precision=5)}\"))\n",
    "        display(Math(f\"\\\\lambda_{{{k}}} \\\\approx {lam_k:.5f}\"))\n",
    "        display(Math(f\"x_{{{k}}} = \\\\frac{{1}}{{{c:.5f}}} y_{{{k}}} = {matrix_to_latex(x_new, precision=5)}\"))\n",
    "        \n",
    "        sai_so = np.abs(lam_k - lam_prev)\n",
    "        print(f\"> Sai số trị riêng: |λ_k - λ_prev| = {sai_so:.5e}\")\n",
    "        \n",
    "        if sai_so < tol:\n",
    "            print(f\"\\n✅ HỘI TỤ SAU {k} BƯỚC LẶP!\")\n",
    "            break\n",
    "            \n",
    "        x_k = x_new\n",
    "        lam_prev = lam_k\n",
    "        \n",
    "    print(\"\\n\" + \"=\"*60)\n",
    "    print(\"KẾT LUẬN:\")\n",
    "    display(Math(f\"\\\\lambda_{{max}} \\\\approx {lam_k:.5f}\"))\n",
    "    display(Math(f\"v_{{max}} \\\\approx {matrix_to_latex(x_k, precision=5)}\"))\n",
    "\n",
    "# Ví dụ ma trận A\n",
    "A = np.array([\n",
    "    [4, 1, 0],\n",
    "    [1, 20, 1],\n",
    "    [0, 1, 4]\n",
    "], dtype=float)\n",
    "\n",
    "# Véctơ xấp xỉ ban đầu\n",
    "x0 = np.array([1, 1, 1])\n",
    "\n",
    "Power_Method(A, x0, tol=1e-4, max_iter=10)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
