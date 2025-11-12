# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# def knapsack_01(values, weights, capacity):
#     n = len(values)
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for w in range(1, capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
#             else:
#                 dp[i][w] = dp[i - 1][w]
#     res = dp[n][capacity]
#     w = capacity
#     selected_items = []
#     for i in range(n, 0, -1):
#         if res <= 0:
#             break
#         if res == dp[i - 1][w]:
#             continue
#         else:
#             selected_items.append(i)
#             res -= values[i - 1]
#             w -= weights[i - 1]
#     return dp[n][capacity], selected_items[::-1]

# def fractional_knapsack(values, weights, capacity):
#     n = len(values)
#     ratio = [(values[i] / weights[i], i) for i in range(n)]
#     ratio.sort(reverse=True)
#     total_value = 0
#     selected_items = []
#     for r, i in ratio:
#         if weights[i] <= capacity:
#             total_value += values[i]
#             capacity -= weights[i]
#             selected_items.append((i + 1, 1))  # Full item
#         else:
#             if capacity == 0:
#                 break
#             fraction = capacity / weights[i]
#             total_value += values[i] * fraction
#             selected_items.append((i + 1, round(fraction, 2)))
#             break
#     return total_value, selected_items

# def display_selected_items(items, values, weights, frame, algo_name, is_fractional=False):
#     for widget in frame.winfo_children():
#         widget.destroy()
#     hdr_text = f"Selected Items ({algo_name})"
#     tk.Label(frame, text=hdr_text, font=("Calibri", 12, "bold"), fg="#2E8B57", bg="#F5F5F5").grid(row=0, columnspan=(4 if is_fractional else 3), pady=(0, 5))
#     headers = ["Index", "Value", "Weight"]
#     if is_fractional:
#         headers.append("Fraction Taken")
#     for col, txt in enumerate(headers):
#         tk.Label(frame, text=txt, bg="#F5F5F5", font=("Calibri", 11, "bold")).grid(row=1, column=col)
#     for i, item in enumerate(items):
#         if is_fractional:
#             idx, frac = item
#             idx0 = idx - 1
#             tk.Label(frame, text=str(idx), bg="#F5F5F5").grid(row=i + 2, column=0)
#             tk.Label(frame, text=str(values[idx0]), bg="#F5F5F5").grid(row=i + 2, column=1)
#             tk.Label(frame, text=str(weights[idx0]), bg="#F5F5F5").grid(row=i + 2, column=2)
#             tk.Label(frame, text=f"{frac}", bg="#F5F5F5").grid(row=i + 2, column=3)
#         else:
#             idx = item
#             idx0 = idx - 1
#             tk.Label(frame, text=str(idx), bg="#F5F5F5").grid(row=i + 2, column=0)
#             tk.Label(frame, text=str(values[idx0]), bg="#F5F5F5").grid(row=i + 2, column=1)
#             tk.Label(frame, text=str(weights[idx0]), bg="#F5F5F5").grid(row=i + 2, column=2)

# def compare_algorithms():
#     try:
#         values = [int(x.strip()) for x in entry_values.get().split(',') if x.strip()]
#         weights = [int(x.strip()) for x in entry_weights.get().split(',') if x.strip()]
#         capacity = int(entry_capacity.get().strip())
#         if len(values) != len(weights):
#             messagebox.showerror("Input Error", "Values and Weights must have same length.")
#             return
#         if not values or not weights or capacity <= 0:
#             messagebox.showerror("Input Error", "Inputs cannot be empty and capacity must be positive.")
#             return
#         if any(w <= 0 for w in weights):
#             messagebox.showerror("Input Error", "Weights must be positive numbers.")
#             return
#         val_01, items_01 = knapsack_01(values, weights, capacity)
#         val_frac, items_frac = fractional_knapsack(values, weights, capacity)
#         result_01.config(text=f"0/1 Knapsack → Max Value: {val_01} | Items: {items_01}")
#         result_frac.config(text=f"Fractional Knapsack → Max Value: {round(val_frac, 2)} | Items: {items_frac}")
#         if val_frac > val_01:
#             statement = "Fractional Knapsack gives better result because it allows taking fractions of items."
#         elif val_frac == val_01:
#             statement = "Both algorithms give same result for this case."
#         else:
#             statement = "0/1 Knapsack gives better result for this dataset."
#         explanation_label.config(
#             text=statement,
#             fg="#1E90FF",
#             font=("Helvetica", 12, "bold italic")
#         )
#         fig, ax = plt.subplots(figsize=(4.5, 3))
#         algorithms = ['0/1 Knapsack', 'Fractional Knapsack']
#         values_ = [val_01, val_frac]
#         ax.bar(algorithms, values_, color=['#4CAF50', '#2196F3'])
#         ax.set_title("Comparison of Algorithm Outcomes")
#         ax.set_ylabel("Maximum Value")
#         for widget in chart_frame.winfo_children():
#             widget.destroy()
#         canvas = FigureCanvasTkAgg(fig, master=chart_frame)
#         canvas.draw()
#         canvas.get_tk_widget().pack()
#         display_selected_items(items_01, values, weights, selected_items_frame_01, "0/1 Knapsack", is_fractional=False)
#         display_selected_items(items_frac, values, weights, selected_items_frame_frac, "Fractional Knapsack", is_fractional=True)
#     except Exception as ex:
#         messagebox.showerror("Invalid Input", f"Error: {ex}")

# def toggle_theory_panel():
#     if theory_panel.winfo_ismapped():
#         theory_panel.pack_forget()
#         theory_btn.config(text="Show Theory Info")
#     else:
#         theory_panel.pack(pady=10, fill="x")
#         theory_btn.config(text="Hide Theory Info")

# def setup_theory_panel():
#     for widget in theory_panel.winfo_children():
#         widget.destroy()
#     tk.Label(theory_panel, text="Algorithm Theory & Complexity", font=("Verdana", 14, "bold"),
#              bg="#D7EDFA", fg="#005A9C").pack(pady=(5, 6))
#     txts = [
#         ("0/1 Knapsack Algorithm", "NP-complete problem\n- Algo: Dynamic Programming\n- Time Complexity: O(nC)\n- Space Complexity: O(nC)"),
#         ("Fractional Knapsack Algorithm", "In P (Polynomial Time)\n- Algo: Greedy\n- Time Complexity: O(n log n)\n- Space: O(n)"),
#         ("Complexity Classes", "P: Efficiently solvable\nNP: Efficiently verifiable\nNP-complete: Hardest NP\n(0/1 Knapsack is NP-complete; Fractional Knapsack is in P)")
#     ]
#     for head, content in txts:
#         tk.Label(theory_panel, text=head, font=("Calibri", 12, "bold"), bg="#D7EDFA", fg="#007ACC").pack(anchor="w", padx=15, pady=(2, 0))
#         tk.Label(theory_panel, text=content, font=("Calibri", 11), bg="#D7EDFA", justify="left").pack(anchor="w", padx=30, pady=(0, 4))

# window = tk.Tk()
# window.title("🎒 Knapsack Algorithm Comparator")
# window.geometry("850x750")
# window.config(bg="#F5F5F5")

# tk.Label(window, text="Knapsack Algorithm Comparator", font=("Verdana", 18, "bold"), bg="#F5F5F5", fg="#2E8B57").pack(pady=10)
# frame = tk.Frame(window, bg="#F5F5F5")
# frame.pack(pady=10)
# tk.Label(frame, text="Enter Values (comma-separated):", font=("Calibri", 12), bg="#F5F5F5").grid(row=0, column=0, sticky="w")
# entry_values = tk.Entry(frame, width=45)
# entry_values.grid(row=0, column=1, padx=10, pady=5)
# tk.Label(frame, text="Enter Weights (comma-separated):", font=("Calibri", 12), bg="#F5F5F5").grid(row=1, column=0, sticky="w")
# entry_weights = tk.Entry(frame, width=45)
# entry_weights.grid(row=1, column=1, padx=10, pady=5)
# tk.Label(frame, text="Enter Capacity:", font=("Calibri", 12), bg="#F5F5F5").grid(row=2, column=0, sticky="w")
# entry_capacity = tk.Entry(frame, width=45)
# entry_capacity.grid(row=2, column=1, padx=10, pady=5)
# tk.Button(window, text="Run Comparison", command=compare_algorithms, bg="#2E8B57", fg="white",
#           font=("Calibri", 13, "bold"), padx=10, pady=5).pack(pady=10)

# result_01 = tk.Label(window, text="", font=("Calibri", 12), bg="#F5F5F5")
# result_01.pack()
# result_frac = tk.Label(window, text="", font=("Calibri", 12), bg="#F5F5F5")
# result_frac.pack()
# explanation_label = tk.Label(window, text="", bg="#F5F5F5")
# explanation_label.pack(pady=10)
# chart_frame = tk.Frame(window, bg="#F5F5F5")
# chart_frame.pack(pady=10)
# selected_items_frame_01 = tk.Frame(window, bg="#F5F5F5")
# selected_items_frame_01.pack(pady=5)
# selected_items_frame_frac = tk.Frame(window, bg="#F5F5F5")
# selected_items_frame_frac.pack(pady=5)

# theory_panel = tk.Frame(window, bg="#D7EDFA", bd=2, relief="groove")
# setup_theory_panel()
# theory_btn = tk.Button(window, text="Show Theory Info", command=toggle_theory_panel,
#                        bg="#1E90FF", fg="white", font=("Calibri", 12, "bold"))
# theory_btn.pack(pady=5)

# window.mainloop()




import tkinter as tk
from tkinter import messagebox
import heapq
import threading
import time
import random

# ------------------- Graph Data -------------------
NODES = {
    'A': (100, 150), 'B': (300, 100), 'C': (500, 150), 'D': (700, 100),
    'E': (200, 350), 'F': (400, 300), 'G': (600, 350), 'H': (350, 520)
}
EDGES = {
    'A': [('B', 2), ('E', 1)],
    'B': [('A', 2), ('C', 3), ('F', 5), ('E', 4)],
    'C': [('B', 3), ('D', 2), ('F', 1)],
    'D': [('C', 2), ('G', 4)],
    'E': [('A', 1), ('B', 4), ('F', 1), ('H', 6)],
    'F': [('B', 5), ('C', 1), ('E', 1), ('G', 2), ('H', 2)],
    'G': [('D', 4), ('F', 2), ('H', 1)],
    'H': [('E', 6), ('F', 2), ('G', 1)]
}

# Predefine node colors for vibrancy
NODE_COLORS = ["#F94144", "#F3722C", "#F8961E", "#F9C74F", "#90BE6D",
               "#43AA8B", "#577590", "#9D4EDD"]
node_color_map = {name: NODE_COLORS[i % len(NODE_COLORS)] for i, name in enumerate(NODES)}

# ------------------- Dijkstra Algorithm -------------------
def dijkstra(graph, start, end):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return (cost, path)
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path))
    return (float('inf'), [])

# ------------------- Drawing -------------------
def draw_static_graph():
    """Draw nodes and edges once (static background)."""
    # Safe gradient background
    for i in range(0, 600, 2):
        r = min(255, 100 + i // 3)
        g = max(0, 200 - i // 6)
        b = max(0, 255 - i // 8)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_rectangle(0, i, 900, i+2, outline=color, fill=color)

    # Draw edges
    for src in NODES:
        for dst, weight in EDGES.get(src, []):
            x1, y1 = NODES[src]
            x2, y2 = NODES[dst]
            canvas.create_line(x1, y1, x2, y2, fill="#B0BEC5", width=2, smooth=True, tags=f"edge_{src}_{dst}")
            cx, cy = (x1 + x2)//2, (y1 + y2)//2
            canvas.create_text(cx, cy, text=str(weight), fill='navy', font=('Arial', 10, 'bold'))

    # Draw colorful nodes
    for name, (x, y) in NODES.items():
        color = node_color_map[name]
        outline = "#FFD700" if (name == var_start.get() or name == var_end.get()) else "black"
        canvas.create_oval(x-25, y-25, x+25, y+25, fill=color, outline=outline, width=3, tags=f"node_{name}")
        canvas.create_text(x, y, text=name, fill='white', font=('Comic Sans MS', 15, 'bold'), tags=f"text_{name}")


def reset_colors():
    """Reset graph to initial colorful state."""
    for name, color in node_color_map.items():
        canvas.itemconfig(f"node_{name}", fill=color)
    for src in NODES:
        for dst, _ in EDGES.get(src, []):
            canvas.itemconfig(f"edge_{src}_{dst}", fill="#B0BEC5", width=2)

def highlight_path(path):
    """Animate highlighting the shortest path."""
    glow_colors = ["#FF007F", "#FF4500", "#FFD700", "#00FA9A", "#1E90FF"]
    for i in range(len(path) - 1):
        src, dst = path[i], path[i + 1]
        edge_color = random.choice(glow_colors)
        node_color = edge_color

        canvas.itemconfig(f"edge_{src}_{dst}", fill=edge_color, width=5)
        canvas.itemconfig(f"edge_{dst}_{src}", fill=edge_color, width=5)
        canvas.itemconfig(f"node_{src}", fill=node_color)
        canvas.itemconfig(f"node_{dst}", fill=node_color)
        window.update()
        time.sleep(0.4)

def on_find_shortest():
    source = var_start.get()
    dest = var_end.get()
    if source == dest:
        messagebox.showwarning("Invalid", "Source and destination must be different.")
        return
    cost, path = dijkstra(EDGES, source, dest)
    if not path:
        result_label.config(text="❌ No path available", fg="red")
        reset_colors()
    else:
        result_label.config(
            text=f"🌟 Shortest path: {' → '.join(path)}  |  Cost: {cost}",
            fg="#6A1B9A"
        )
        reset_colors()
        threading.Thread(target=lambda: highlight_path(path), daemon=True).start()

def reset_graph():
    result_label.config(text="", fg="black")
    reset_colors()

# ------------------- GUI Setup -------------------
window = tk.Tk()
window.title("🌈 Dijkstra's Shortest Path Visualizer")
window.geometry("960x780")
window.configure(bg="#FFF8E1")

# Title
title = tk.Label(window, text="🌟 Dijkstra's Shortest Path Visualizer 🌟",
                 font=('Verdana', 20, 'bold'), fg="#2E7D32", bg="#FFF8E1")
title.pack(pady=15)

# Control frame
frame = tk.Frame(window, bg="white", relief='ridge', bd=4, highlightbackground="#FFB74D", highlightthickness=2)
frame.pack(pady=10, ipadx=10, ipady=8)

tk.Label(frame, text="Start Node:", font=('Calibri', 13, 'bold'), bg="white").grid(row=0, column=0, padx=10)
var_start = tk.StringVar(value='A')
drop_start = tk.OptionMenu(frame, var_start, *NODES.keys())
drop_start.config(font=('Calibri', 12), bg="#E1F5FE", relief='ridge')
drop_start.grid(row=0, column=1, padx=10)

tk.Label(frame, text="End Node:", font=('Calibri', 13, 'bold'), bg="white").grid(row=0, column=2, padx=10)
var_end = tk.StringVar(value='H')
drop_end = tk.OptionMenu(frame, var_end, *NODES.keys())
drop_end.config(font=('Calibri', 12), bg="#FCE4EC", relief='ridge')
drop_end.grid(row=0, column=3, padx=10)

# Vibrant button styles
def hover_in(e): e.widget.config(bg="#FF7043")
def hover_out(e): e.widget.config(bg="#FF5722")

find_btn = tk.Button(frame, text="Find Shortest Path", command=on_find_shortest,
                     font=("Calibri", 13, "bold"), bg="#FF5722", fg="white",
                     relief='raised', padx=14, pady=4)
find_btn.grid(row=0, column=4, padx=15)
find_btn.bind("<Enter>", hover_in)
find_btn.bind("<Leave>", hover_out)

reset_btn = tk.Button(frame, text="Reset Graph", command=reset_graph,
                      font=("Calibri", 13, "bold"), bg="#4DB6AC", fg="white",
                      relief='raised', padx=14, pady=4)
reset_btn.grid(row=0, column=5, padx=10)
reset_btn.bind("<Enter>", lambda e: e.widget.config(bg="#00897B"))
reset_btn.bind("<Leave>", lambda e: e.widget.config(bg="#4DB6AC"))

# Result label
result_label = tk.Label(window, text="", font=('Comic Sans MS', 13, "bold"), bg="#FFF8E1")
result_label.pack(pady=10)

# Canvas area
canvas_frame = tk.Frame(window, bg="white", relief='sunken', bd=3, highlightbackground="#9C27B0", highlightthickness=2)
canvas_frame.pack(pady=10)
canvas = tk.Canvas(canvas_frame, width=900, height=580, bg="#E3F2FD", highlightthickness=0)
canvas.pack()

draw_static_graph()

# Footer
tk.Label(window, text="Created by Sahil kumar  | Algorithm Visualizer © 2025",
         font=("Arial", 9, "italic"), bg="#FFF8E1", fg="#424242").pack(side="bottom", pady=8)

window.mainloop()





