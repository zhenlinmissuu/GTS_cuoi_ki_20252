import json

def update_notebook():
    with open('Giai_tich_so.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            src = ''.join(cell['source'])
            if '### Lặp đơn nhiều chiều' in src:
                # The next cell should be the # TODO code cell.
                # Update markdown
                nb['cells'][i]['source'] = [
                    "### Lặp đơn nhiều chiều\n",
                    "\n",
                    "Phương pháp biến đổi hệ phương trình phi tuyến $F(X) = 0$ thành hệ $X = G(X)$ sao cho thỏa mãn điều kiện hội tụ (hệ số co $q < 1$).\n",
                    "\n",
                    "*   **Input:** Hàm lặp $G(X) = (g_1(X), g_2(X), \\dots, g_n(X))^T$, xấp xỉ ban đầu $X^{(0)}$, hệ số co $q < 1$, sai số cho phép $\\epsilon$.\n",
                    "*   **Thuật toán:**\n",
                    "    *   **B1:** Lặp tính xấp xỉ mới $X^{(k+1)} = G(X^{(k)})$.\n",
                    "    *   **B2:** Đánh giá sai số hậu nghiệm: $\\text{err} = \\frac{q}{1-q} \\|X^{(k+1)} - X^{(k)}\\|_\\infty$.\n",
                    "    *   **B3:** Nếu $\\text{err} < \\epsilon$, thuật toán dừng và trả về nghiệm $X^{(k+1)}$."
                ]
                
                # Check next cell
                if i + 1 < len(nb['cells']) and nb['cells'][i+1]['cell_type'] == 'code':
                    code_src = ''.join(nb['cells'][i+1]['source'])
                    if '# TODO' in code_src:
                        nb['cells'][i+1]['source'] = [
                            "import numpy as np\n",
                            "\n",
                            "def lap_don_phi_tuyen_he(G, X0, q, epsilon, max_iter=20):\n",
                            "    print(\"=\"*60)\n",
                            "    print(\"PHƯƠNG PHÁP LẶP ĐƠN (HỆ PHƯƠNG TRÌNH PHI TUYẾN)\")\n",
                            "    print(\"=\"*60)\n",
                            "    \n",
                            "    print(\"Bước 1: Khởi tạo và kiểm tra hệ số co\")\n",
                            "    print(f\"  Hệ số co q = {q}\")\n",
                            "    if q >= 1:\n",
                            "        print(\"  => Cảnh báo: q >= 1, phương pháp có thể không hội tụ.\")\n",
                            "    \n",
                            "    X_k = np.array(X0, dtype=float)\n",
                            "    n = len(X0)\n",
                            "    \n",
                            "    print(\"\\nBước 2: Bảng tính\")\n",
                            "    header = f\"{'k':<5} | \" + \" | \".join([f\"x_{j+1:<8}\" for j in range(n)]) + \" | ||X_k - X_{k-1}||_inf\"\n",
                            "    print(\"-\" * len(header))\n",
                            "    print(header)\n",
                            "    print(\"-\" * len(header))\n",
                            "    \n",
                            "    X_prev = None\n",
                            "    for k in range(max_iter):\n",
                            "        if k > 0:\n",
                            "            diff = np.linalg.norm(X_k - X_prev, np.inf)\n",
                            "            row = f\"{k:<5} | \" + \" | \".join([f\"{xi:<10.5f}\" for xi in X_k]) + f\" | {diff:.5f}\"\n",
                            "            print(row)\n",
                            "            \n",
                            "            sai_so_hau_nghiem = (q / (1 - q)) * diff if q < 1 else diff\n",
                            "            \n",
                            "            if sai_so_hau_nghiem < epsilon:\n",
                            "                print(\"-\" * len(header))\n",
                            "                print(f\"\\nBước 3: Kết luận\")\n",
                            "                print(f\"  Hội tụ tại bước {k}.\")\n",
                            "                print(f\"  Nghiệm X ≈ {np.round(X_k, 5)}\")\n",
                            "                print(f\"  Sai số hậu nghiệm: {sai_so_hau_nghiem:.5f} < {epsilon}\")\n",
                            "                return\n",
                            "        else:\n",
                            "            row = f\"{k:<5} | \" + \" | \".join([f\"{xi:<10.5f}\" for xi in X_k]) + \" | -\"\n",
                            "            print(row)\n",
                            "            \n",
                            "        X_prev = X_k\n",
                            "        X_k = G(X_k)\n",
                            "\n",
                            "# Test thử bài toán\n",
                            "def G_demo(X):\n",
                            "    x, y = X[0], X[1]\n",
                            "    return np.array([\n",
                            "        (x**2 + y**2 + 8) / 10,\n",
                            "        (x * y + x + 8) / 10\n",
                            "    ])\n",
                            "\n",
                            "lap_don_phi_tuyen_he(G_demo, [0.5, 0.5], 0.2, 0.001)\n"
                        ]
                break

    with open('Giai_tich_so.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

if __name__ == '__main__':
    update_notebook()
