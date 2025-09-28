import os 
from block_operations import markdown_to_html_node


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_page(from_path, template_path, dest_path):
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    from_file = open(from_path, "r")
    from_file_content = from_file.read()
    from_file.close()
    
    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()
    
    node = markdown_to_html_node(from_file_content)
    html = node.to_html()
    
    title = extract_title(from_file_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    template_content = template_content.replace('href="/', 'href="' + dest_path)
    template_content = template_content.replace('src="/', 'src="' + dest_path)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template_content)