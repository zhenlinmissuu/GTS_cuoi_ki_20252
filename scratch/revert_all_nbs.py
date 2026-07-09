import json
import os
import glob

scripts_dir = "scripts"

for root, _, files in os.walk(scripts_dir):
    for filename in files:
        if filename.endswith(".ipynb"):
            filepath = os.path.join(root, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    nb = json.load(f)
                    
                changed = False
                for cell in nb.get('cells', []):
                    if cell.get('cell_type') == 'code':
                        source = cell.get('source', [])
                        new_source = []
                        for line in source:
                            new_line = line
                            if 'display(Markdown(rf"' in new_line:
                                new_line = new_line.replace('display(Markdown(rf"', 'display(Markdown(f"')
                                changed = True
                            if 'display(Math(rf"' in new_line:
                                new_line = new_line.replace('display(Math(rf"', 'display(Math(f"')
                                changed = True
                            if "display(Markdown(rf'" in new_line:
                                new_line = new_line.replace("display(Markdown(rf'", "display(Markdown(f'")
                                changed = True
                            if "display(Math(rf'" in new_line:
                                new_line = new_line.replace("display(Math(rf'", "display(Math(f'")
                                changed = True

                            new_source.append(new_line)
                        
                        if changed:
                            cell['source'] = new_source
                
                if changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(nb, f, indent=1, ensure_ascii=False)
                    
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print("Reverted all notebooks.")
